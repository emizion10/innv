from django.contrib import admin
from .models import *
admin.site.register(User)
admin.site.register(Disasters)
admin.site.register(Volunteer)
admin.site.register(Help)

# Register your models here.
