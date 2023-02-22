from django.contrib import admin
from .models import Identity, Job, Quotation, Photo
# Register your models here.
admin.site.register(Identity)
admin.site.register(Job)
admin.site.register(Quotation)
admin.site.register(Photo)