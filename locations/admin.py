from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Location

admin.site.register(Location, SimpleHistoryAdmin)
