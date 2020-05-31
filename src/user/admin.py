from django.contrib import admin
from .models import Profile
from import_export.admin import ImportExportModelAdmin

# admin.site.register(Profile)
@admin.register(Profile)
class ProfileImportExport(ImportExportModelAdmin):
    pass
