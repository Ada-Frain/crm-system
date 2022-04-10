from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',
    'contract_number',
    'brand',
    'contractor',
    'contractor_contract',
    'advance_payment1',
    'advance_payment2',
    'advance_payment3',
    'final_sum',
    'cs_upd',
    'adress',
    'contacts',
    'engineer',
    'status']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Project, ProjectAdmin)
