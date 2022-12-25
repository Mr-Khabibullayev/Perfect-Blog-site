from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeFrom ,CustomUserCreationForm
from .models import CustomUser


# Register your models here.

class CuStomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeFrom
    model = CustomUser
    list_display = ['email','username','first_name','last_name','age','is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None ,{'fields':('age',)}),
    )
    
    
admin.site.register(CustomUser,CuStomUserAdmin)