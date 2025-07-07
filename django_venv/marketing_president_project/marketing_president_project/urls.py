from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Homepage
    path('dashboard/', include('dashboard.urls')),
    path('funnel/', include('funnel.urls')),
    path('testing/', include('testing.urls')),
    path('profile/', include('users.urls')),
    path('approval/', include('approval.urls')),
    path('admin/panel/', include('adminpanel.urls')),
]
