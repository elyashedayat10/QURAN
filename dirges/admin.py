from django.contrib import admin

from .models import Dirge, DirgeCategory

# Register your models here.
admin.site.register(DirgeCategory)
admin.site.register(Dirge)
