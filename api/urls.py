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


urlpatterns = [
    path('', include(router.urls)),
]
