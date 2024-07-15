from django.contrib import admin

# Register your models here.

from main_APP import models

admin.site.register(models.Skills)
admin.site.register(models.Company)
admin.site.register(models.Resume)
admin.site.register(models.Request)
admin.site.register(models.Vacancy)
