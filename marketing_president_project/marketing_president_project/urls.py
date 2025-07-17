from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # <- tambahkan baris ini

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('profile/', include('users.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('funnel/', include('funnel.urls')),
    path('testing/', include('testing.urls')),
    path('approval/', include('approval.urls')),
    path('adminpanel/', include('adminpanel.urls')),

    # Auth login/logout
    path('profile/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
