from idlelib.multicall import r

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# PATCH /api/fo/{id}/update_fo_fuel_lock/: Updates the foFuelLock field of a CaFO object by its ID. "foFuelLock": true
# PATCH /api/fo/{id}/update_fo_perdium_lock/: Updates the foPerdiumLock field of a CaFO object by its ID. "foPerdiumLock": true
# PATCH /api/fo/{id}/update_fo_advance_lock/: Updates the foAdvanceLock field of a CaFO object by its ID. "foAdvanceLock": true

router = DefaultRouter()
router.register(r'trailers', TrailerViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'drvery', DrvEmergecyContactViewSet)
router.register(r'drvls', DrvLicenceViewSet)
router.register(r'drvlv', DrvLeaveViewSet)
router.register(r'drvps', DrvPassportViewSet)
router.register(r'fleet', FleetNoViewSet)
router.register(r'truck', AbTruckViewSet)
router.register(r'trip', BaTripViewSet)
router.register(r'fo', CaFOViewSet)
router.register(r'advance', EbAdvanceViewSet)
router.register(r'fuel', DaFuelViewSet)
router.register(r'perdiuem', EaPerdiuemViewSet)
router.register(r'condition', ConditionViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'customercontact', CustomerContactViewSet)
# router.register(r'fbstscat', FbStsCatViewSet)
router.register(r'bbmtrl', BbMtrlViewSet)
router.register(r'mtrcat', BcMtrlViewSet)
router.register(r'djiboutipass', DrvDjiboutiViewSet)
router.register(r'fltbolo', FltBoloViewSet)
router.register(r'trlbolo', TRLBoloViewSet)
router.register(r'fltcomesa',FltComesaViewSet)
router.register(r'trlcomesa',TRLComesaViewSet)
router.register(r'trlinsurance', TRLInsuranceViewSet)
router.register(r'fltinsurance', FltInsuranceViewSet)
router.register(r'trlthirdparty', TRLThirdPartyViewSet)
router.register(r'fltthirdparty', FltThirdPartyViewSet)
router.register(r'tireprovision', TyerNewViewSet)
router.register(r'tirereturn', TyerReturnViewSet)
router.register(r'al', UserActionLogView)
router.register(r'infratype', InfractionTypeViewSet)
router.register(r'infra', InfractionViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
