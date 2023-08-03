from django.contrib import admin
from .models.users import user_registration


# Register your models here.

class user(admin.ModelAdmin):
    list_display = ['updated_on','Name','Last_Name','Phone_number','Email','password','created_on']
    search_fields = ['Email']
admin.site.register(user_registration,user)
