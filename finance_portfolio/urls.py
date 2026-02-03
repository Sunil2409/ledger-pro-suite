from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login  # ✅ Add this
from transactions.views import DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashboardView.as_view(), name='dashboard'),
    path('transactions/', include('transactions.urls')),
    path('watchlist/', include('watchlist.urls')),
    
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # ✅ THIS VERSION WORKS 100%
    path('logout/', lambda request: logout_then_login(request, login_url='/login/'), name='logout'),
    
    path('signup/', include('django.contrib.auth.urls')),
]