from django.contrib import admin
from .models import LabResult

@admin.register(LabResult)
class LabResultAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'organism', 'antibiotic', 'susceptibility', 'test_date', 'facility']
    list_filter = ['organism', 'antibiotic', 'susceptibility', 'facility', 'test_date']
    search_fields = ['patient_id', 'organism', 'antibiotic']
    date_hierarchy = 'test_date'
    
    fieldsets = (
        ('Patient Information', {
            'fields': ('patient_id', 'patient_age', 'patient_sex')
        }),
        ('Specimen Details', {
            'fields': ('specimen_type', 'organism')
        }),
        ('Antibiotic Testing', {
            'fields': ('antibiotic', 'susceptibility')
        }),
        ('Administrative', {
            'fields': ('test_date', 'facility')
        }),
    )
