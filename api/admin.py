from django.contrib import admin
from .models import *

admin.site.register((Driver, DrvLicence, DrvEmergecyContact, DrvLeave, Customer, CustomerContact, FbStsCat, BbMtrl))
admin.site.register(Trailer)
admin.site.register(Condition)