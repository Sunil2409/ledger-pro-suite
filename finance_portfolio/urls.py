"""
URL configuration for finance_portfolio project.
Complete working version with custom logout
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import redirect
from transactions.views import DashboardView, SignUpView


# Custom logout view function
def custom_logout(request):
    """Custom logout view that logs out user and redirects to login"""
    logout(request)
    return redirect('login')


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Main dashboard
    path('', DashboardView.as_view(), name='dashboard'),
    
    # App URLs
    path('transactions/', include('transactions.urls')),
    path('watchlist/', include('watchlist.urls')),
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
    
    # Custom logout - redirects to login page
    path('logout/', custom_logout, name='logout'),
    
    # Signup
    path('signup/', SignUpView.as_view(), name='signup'),
]