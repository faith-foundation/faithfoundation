from django.contrib import admin
from .models import smallEvent, eventForm
# Register your models here.

admin.site.register([smallEvent, eventForm])