from django.contrib import admin
from .models import *

admin.site.register((Driver, CaFO, BaTrip, DrvLicence, DrvEmergecyContact, DrvLeave, Customer, CustomerContact, FbStsCat, BbMtrl,
                     AbTruck, AaFleetNo, UserActionLog))
admin.site.register(Trailer)
admin.site.register(Condition)