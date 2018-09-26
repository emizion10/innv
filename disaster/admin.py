from django.contrib import admin
from .models import *
admin.site.register(User)
admin.site.register(Disasters)
admin.site.register(Volunteer)
admin.site.register(Help)
admin.site.register(DisasterDetails)

# Register your models here.
