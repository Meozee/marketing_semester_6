from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    """
    Custom user creation form with staff and superuser flags.
    """
    is_staff = forms.BooleanField(required=False, label="Staff status")
    is_superuser = forms.BooleanField(required=False, label="Superuser status")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")  # password1 & password2 already included by UserCreationForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = False

class CustomUserAdmin(BaseUserAdmin):
    """
    Enhanced User Admin with better organization and usability.
    """
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm  # Also use for change form
    
    # Fields for add user page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 
                       'is_staff', 'is_superuser'),
        }),
    )
    
    # Fields for change user page
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 
                       'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    list_display = ('username', 'email', 'first_name', 'last_name', 
                    'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
    
    def get_form(self, request, obj=None, **kwargs):
        """
        Use custom form for both add and change pages.
        """
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

admin.site.register(User, CustomUserAdmin)
