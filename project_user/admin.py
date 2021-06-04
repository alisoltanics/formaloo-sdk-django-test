from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import ProjectUser


class ProjectUserAdmin(DjangoUserAdmin, admin.ModelAdmin):
    list_display = ('username', 'id', 'formaloo_customer_slug', )
    search_fields = ('username', 'id')


admin.site.register(ProjectUser, ProjectUserAdmin)
