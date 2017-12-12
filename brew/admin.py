from django.contrib import admin
from brew.models import *

admin.site.site_header = "Vupit Dashboard"
admin.site.register(Message)
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Request)
