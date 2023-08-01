from django.contrib import admin
from .models import *

admin.site.register((Driver, CaFO, BaTrip, DrvLicence, DrvEmergecyContact, DrvLeave, Customer, CustomerContact, FbStsCat, BbMtrl,
                     AbTruck, AaFleetNo))
admin.site.register(Trailer)
admin.site.register(Condition)