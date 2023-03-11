from django.contrib import admin
from . import models 
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class stateAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...

admin.site.register(models.States,stateAdmin)

