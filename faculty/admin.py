from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from faculty.models import Proctor

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username','last_login', 'is_admin')
    search_fields = ('email', 'username')
    readonly_fields = ('id','date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Proctor, AccountAdmin)