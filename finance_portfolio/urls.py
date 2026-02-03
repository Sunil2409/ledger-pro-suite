"""
URL configuration for finance_portfolio project.
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from transactions.views import DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashboardView.as_view(), name='dashboard'),
    path('transactions/', include('transactions.urls')),
    path('watchlist/', include('watchlist.urls')),
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', include('django.contrib.auth.urls')),
]
