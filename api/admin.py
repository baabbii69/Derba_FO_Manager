from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
User = get_user_model()

admin.site.unregister(Group)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('cmrName', 'cmrCode')


admin.site.register(Customer, CustomerAdmin)
admin.site.register((UserAccount, Driver, CaFO, BaTrip, DrvLicence, DrvEmergecyContact, DrvLeave, CustomerContact,
                     FbStsCat, DrvPassport, MtrCat, BbMtrl, AbTruck, AaFleetNo, UserActionLog, DjboutiPass, FltBolo,
                     TRLBolo, FltComesa, TRLComesa, TRLInsurance, FltInsurance, TRLThirdParty, FltThirdParty, TyerNew,
                     TyerReturn, EbAdvance, EaPerdiuem, DaFuel, FaSts, Infraction, InfractionType))
admin.site.register(Trailer)
admin.site.register(Condition)