from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test
from functools import wraps
from accounts.models import Manager

def manager_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Allow superuser access
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
            
        try:
            manager = Manager.objects.get(user=request.user)
            return view_func(request, *args, **kwargs)
        except (Manager.DoesNotExist, TypeError):
            return redirect('login')
    return _wrapped_view 