"""
URL configuration for finance_portfolio project.
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from transactions.views import DashboardView, SignUpView

# Simple logout function
def custom_logout(request):
    from django.contrib.auth import logout
    from django.shortcuts import redirect
    logout(request)
    return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashboardView.as_view(), name='dashboard'),
    path('transactions/', include('transactions.urls')),
    path('watchlist/', include('watchlist.urls')),
    
    # ✅ Individual auth URLs at root level
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
    
    path('logout/', custom_logout, name='logout'),  # ✅ Now at /logout/
    
    path('signup/', SignUpView.as_view(), name='signup'),
    
    # ❌ REMOVED: path('signup/', include('django.contrib.auth.urls'))
]