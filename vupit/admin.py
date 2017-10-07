from django.contrib import admin
from vupit.models import *

admin.site.site_header = "Vupit Dashboard"
admin.site.register(Message)
