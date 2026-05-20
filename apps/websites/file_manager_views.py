import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required
def file_manager(request):
    # Determine base path for the user
    # In a real system, this would be /home/username
    # For local dev, we'll use a dummy path
    user_home = os.path.join(settings.BASE_DIR, 'media', 'user_homes', request.user.username)
    
    current_path = request.GET.get('path', '')
    full_path = os.path.join(user_home, current_path)
    
    # Security: Ensure user doesn't escape their home
    if not os.path.abspath(full_path).startswith(os.path.abspath(user_home)):
        full_path = user_home
        current_path = ''

    if not os.path.exists(full_path):
        os.makedirs(full_path, exist_ok=True)

    items = []
    try:
        for entry in os.scandir(full_path):
            info = entry.stat()
            items.append({
                'name': entry.name,
                'is_dir': entry.is_dir(),
                'size': info.st_size,
                'modified': info.st_mtime,
                'path': os.path.join(current_path, entry.name)
            })
    except Exception as e:
        print(f"Error reading directory: {e}")

    return render(request, 'websites/file_manager.html', {
        'items': sorted(items, key=lambda x: (not x['is_dir'], x['name'])),
        'current_path': current_path,
        'parent_path': os.path.dirname(current_path) if current_path else None
    })
