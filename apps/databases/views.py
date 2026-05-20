from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Database, DatabaseUser
from .forms import DatabaseForm, DatabaseUserForm
from apps.services.mysql_service import MySQLService

@login_required
def database_list(request):
    databases = Database.objects.filter(user=request.user)
    db_users = DatabaseUser.objects.filter(user=request.user)
    return render(request, 'databases/list.html', {
        'databases': databases,
        'db_users': db_users
    })

@login_required
def database_create(request):
    if request.method == 'POST':
        form = DatabaseForm(request.POST)
        if form.is_valid():
            database = form.save(commit=False)
            database.user = request.user
            
            # System automation
            db_name = f"{request.user.username}_{database.name}"
            if MySQLService.create_database(db_name):
                database.name = db_name # Store the full name
                database.save()
                messages.success(request, f"Database {db_name} created successfully!")
                return redirect('databases:list')
            else:
                messages.error(request, "Failed to create database on the system.")
    else:
        form = DatabaseForm()
    return render(request, 'databases/create.html', {'form': form})

@login_required
def database_user_create(request):
    if request.method == 'POST':
        form = DatabaseUserForm(request.POST)
        if form.is_valid():
            db_user = form.save(commit=False)
            db_user.user = request.user
            
            # System automation
            username = f"{request.user.username}_{db_user.username}"
            password = db_user.password
            
            # Just use the first selected database for simplicity in this example
            # In real scenario, loop through all selected databases
            selected_dbs = form.cleaned_data.get('databases')
            success = True
            for db in selected_dbs:
                if not MySQLService.create_user(username, password, db.name):
                    success = False
                    break
            
            if success:
                db_user.username = username
                db_user.save()
                form.save_m2m() # Save ManyToMany relationships
                messages.success(request, f"Database user {username} created successfully!")
                return redirect('databases:list')
            else:
                messages.error(request, "Failed to create database user on the system.")
    else:
        form = DatabaseUserForm()
    return render(request, 'databases/user_create.html', {'form': form})
