from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import UserProfile

def is_admin(user):
    return user.is_superuser or (hasattr(user, 'profile') and user.profile.role == 'admin')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            
            # Check if 2FA is enabled for this user
            try:
                if hasattr(user, 'profile') and user.profile.two_factor_enabled:
                    return redirect('accounts:security_2fa')
            except Exception:
                pass
                
            return redirect('dashboard:index')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
                    break
                break
            if not form.errors:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('accounts:login')

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard:index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def reseller_list(request):
    resellers = UserProfile.objects.filter(role='reseller')
    return render(request, 'accounts/reseller_list.html', {'resellers': resellers})

@login_required
@user_passes_test(is_admin)
def user_list(request):
    hosting_users = UserProfile.objects.filter(role='user')
    return render(request, 'accounts/user_list.html', {'hosting_users': hosting_users})

@login_required
def security_2fa(request):
    return render(request, 'accounts/security_2fa.html')
