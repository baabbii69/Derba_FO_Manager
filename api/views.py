import logging

from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.schemas import coreapi
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
# from .user_activity import log_user_activity
from rest_framework import filters


class DriverViewSet(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    # permission_classes = IsAuthenticated

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(fkUserId=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DrvEmergecyContactViewSet(ModelViewSet):
    queryset = DrvEmergecyContact.objects.all()
    serializer_class = DrvEmergencyContactSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['driverID']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(fkUserId=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DrvLicenceViewSet(ModelViewSet):
    queryset = DrvLicence.objects.all()
    serializer_class = DrvLicenceSerializer

    def create(self, request):
        drv_id = request.data.get('driverID', None)
        drv_licence_exists = DrvLicence.objects.filter(driverID=drv_id).exists()

        if drv_licence_exists:
            return Response({'error': 'Driver already has a licence. if there is new information try updating the '
                                      'registered  licence of the driver!'},
                            status=status.HTTP_409_CONFLICT)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(fkUserId=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DrvLeaveViewSet(ModelViewSet):
    queryset = DrvLeave.objects.all()
    serializer_class = DrvLeaveSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(fkUserId=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DrvPassportViewSet(ModelViewSet):
    queryset = DrvPassport.objects.all()
    serializer_class = DrvPassportSerializer

    def create(self, request):
        drv_id = request.data.get('DrvId', None)
        drv_licence_exists = DrvPassport.objects.filter(DrvId=drv_id).exists()

        if drv_licence_exists:
            return Response({'error': 'Driver already has a Passport. if there is new information try updating the '
                                      'registered  Passport of the driver!'},
                            status=status.HTTP_409_CONFLICT)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(fkUserId=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TrailerViewSet(ModelViewSet):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        driver_id = self.request.query_params.get('driver')
        if driver_id is not None:
            queryset = queryset.filter(driver=driver_id)
        return queryset

    def retrieve(self, request, pk=None):
        try:
            trailer = self.get_object()
            serializer = self.get_serializer(trailer)
            return Response(serializer.data)
        except Trailer.DoesNotExist:
            return Response({'error': 'Trailer not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            trailer = self.get_object()
        except Trailer.DoesNotExist:
            return Response({'error': 'Trailer not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(trailer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            trailer = self.get_object()
        except Trailer.DoesNotExist:
            return Response({'error': 'Trailer not found'}, status=status.HTTP_404_NOT_FOUND)

        trailer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FleetNoViewSet(ModelViewSet):
    queryset = AaFleetNo.objects.all()
    serializer_class = AaFleetNoSerializer

    def retrieve(self, request, pk=None):
        if pk is not None:
            try:
                fleet = AaFleetNo.objects.get(pk=pk)
                fleet_serializer = AaFleetNoSerializer(fleet)

                return Response(fleet_serializer.data)
            except AaFleetNo.DoesNotExist:
                return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

        fleet = AaFleetNo.objects.all()
        serializer = AaFleetNoSerializer(fleet, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            flt_id = serializer.validated_data['fltFleetNo']
            plt_id = serializer.validated_data['fltPlateNo']

            # Check if a Truck with the same TrlId, DrvId, and FltId already exists
            if AaFleetNo.objects.filter(fltPlateNo=plt_id, fltFleetNo=flt_id).exists():
                raise ValidationError("A Fleet with the same Plate Number and Fleet Number already exists.")

            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            fleet = self.get_object()
        except AaFleetNo.DoesNotExist:
            return Response({'error': 'Fleet not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(fleet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            fleet = self.get_object()
        except AaFleetNo.DoesNotExist:
            return Response({'error': 'Fleet not found'}, status=status.HTTP_404_NOT_FOUND)

        fleet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AbTruckViewSet(ModelViewSet):
    queryset = AbTruck.objects.all()
    serializer_class = AbTruckSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        fleet_id = self.request.query_params.get('FltId')
        driver_id = self.request.query_params.get('DrvId')
        if fleet_id is not None:
            queryset = queryset.filter(FltId=fleet_id)
        if driver_id is not None:
            queryset = queryset.filter(DrvId=driver_id)
        return queryset

    def retrieve(self, request, pk=None):
        if pk is not None:
            try:
                truck = AbTruck.objects.get(pk=pk)
                truck_serializer = AbTruckSerializer(truck)

                return Response(truck_serializer.data)
            except AbTruck.DoesNotExist:
                return Response({'error': 'Truck not found'}, status=status.HTTP_404_NOT_FOUND)

        truck = AbTruck.objects.all()
        serializer = AbTruckSerializer(truck, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            trl_id = serializer.validated_data['TrlId']
            drv_id = serializer.validated_data['DrvId']
            flt_id = serializer.validated_data['FltId']
            user = User.objects.get(id=request.user.id)
            serializer.validated_data['UserId'] = user
            # Check if a Truck with the same TrlId, DrvId, and FltId already exists
            if AbTruck.objects.filter(TrlId=trl_id, DrvId=drv_id, FltId=flt_id).exists():
                raise ValidationError("A Truck with the same TrlId, DrvId, and FltId already exists.")

                # set active status of the truck to false for previous records if any
            if (AbTruck.objects.filter(TrlId=trl_id, FltId=flt_id).exists() and serializer.validated_data['trkActive']):
                AbTruck.objects.filter(TrlId=trl_id, FltId=flt_id).update(trkActive=False)

            serializer.save(fkUserId=request.user)
            print(AbTruck.objects.filter(TrlId=trl_id, FltId=flt_id))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BaTripViewSet(ModelViewSet):
    queryset = BaTrip.objects.all()
    serializer_class = BaTripSerializer

    def retrieve(self, request, pk=None):
        if pk is not None:
            try:
                trip = BaTrip.objects.get(pk=pk)
                trip_serializer = BaTripSerializer(trip)

                return Response(trip_serializer.data)
            except AbTruck.DoesNotExist:
                return Response({'error': 'trip not found'}, status=status.HTTP_404_NOT_FOUND)

        trip = BaTrip.objects.all()
        serializer = BaTripSerializer(trip, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            trip = self.get_object()
        except BaTrip.DoesNotExist:
            return Response({'error': 'Fleet not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(trip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            trip = self.get_object()
        except BaTrip.DoesNotExist:
            return Response({'error': 'Trip not found'}, status=status.HTTP_404_NOT_FOUND)

        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EbAdvanceViewSet(ModelViewSet):
    queryset = EbAdvance.objects.all()
    serializer_class = EbAdvanceSerializer

    def retrieve(self, request, pk=None):
        if pk is not None:
            try:
                advance = EbAdvance.objects.get(pk=pk)
                advance_serializer = EbAdvanceSerializer(advance)

                return Response(advance_serializer.data)
            except AbTruck.DoesNotExist:
                return Response({'error': 'Advance not found'}, status=status.HTTP_404_NOT_FOUND)

        advance = EbAdvance.objects.all()
        serializer = EbAdvanceSerializer(advance, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            advance = self.get_object()
        except EbAdvance.DoesNotExist:
            return Response({'error': 'Trip not found'}, status=status.HTTP_404_NOT_FOUND)

        advance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CaFOViewSet(ModelViewSet):
    queryset = CaFO.objects.all()
    serializer_class = CaFOSerializer

    def retrieve(self, request, pk=None):
        if pk is not None:
            try:
                fo = CaFO.objects.get(pk=pk)
                fo_serializer = CaFOSerializer(fo)

                return Response(fo_serializer.data)
            except CaFO.DoesNotExist:
                return Response({'error': 'FO not found'}, status=status.HTTP_404_NOT_FOUND)

        fo = CaFO.objects.all()
        serializer = CaFOSerializer(fo, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            fo = self.get_object()
        except CaFO.DoesNotExist:
            return Response({'error': 'FO not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(fo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            fo = self.get_object()
        except CaFO.DoesNotExist:
            return Response({'error': 'FO not found'}, status=status.HTTP_404_NOT_FOUND)

        fo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['patch'], detail=True)
    def update_fo_fuel_lock(self, request, pk=None):
        return self._update_lock(request, pk, 'foFuelLock')

    @action(methods=['patch'], detail=True)
    def update_fo_perdium_lock(self, request, pk=None):
        return self._update_lock(request, pk, 'foPerdiumLock')

    @action(methods=['patch'], detail=True)
    def update_fo_advance_lock(self, request, pk=None):
        return self._update_lock(request, pk, 'foAdvanceLock')

    def _update_lock(self, request, pk, field_name):
        try:
            cafo = self.get_object()
        except CaFO.DoesNotExist:
            return Response({'error': 'FO not found'}, status=status.HTTP_404_NOT_FOUND)

        field_value = request.data.get(field_name, None)
        if field_value is not None:
            setattr(cafo, field_name, field_value)
            cafo.save()

            serializer = self.get_serializer(cafo)
            return Response(serializer.data)

        return Response({f'error': f'{field_name} value is required'}, status=status.HTTP_400_BAD_REQUEST)


class DaFuelViewSet(ModelViewSet):
    queryset = DaFuel.objects.all()
    serializer_class = DaFuelSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            fo = serializer.validated_data['FoId']
            try:
                foo = CaFO.objects.filter(foNo=fo)
                for fo in foo:
                    FuelLock = fo.foFuelLock
            except CaFO.DoesNotExist:
                return Response({'error': 'FO not found'}, status=status.HTTP_404_NOT_FOUND)

            if not FuelLock:
                serializer.save(fkUserId=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'error': 'Someone is Working Fuel for this FO'}, status=status.HTTP_409_CONFLICT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EaPerdiuemViewSet(ModelViewSet):
    queryset = EaPerdiuem.objects.all()
    serializer_class = EaPerdiuemSerializer

    # def create(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     fo = serializer.validated_data['FoId']
    #     try:
    #         foo = CaFO.objects.filter(FoId=fo)
    #         fuel = DaFuel.objects.filter(FoId=fo)
    #     except CaFO.DoesNotExist:
    #         return Response({'error': 'FO not found'}, status=status.HTTP_404_NOT_FOUND)
    #
    #     if fuel is not None:
    #         if not foo.foPerdiumLock:
    #             if serializer.is_valid():
    #                 serializer.save(UserId=request.user.id)
    #                 return Response(serializer.data, status=status.HTTP_201_CREATED)
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #         return Response({'error': 'Someone is Working Fuel for this FO'}, status=status.HTTP_409_CONFLICT)
    #     else:
    #         return Response({'error': 'You have to do Fuel 1st'}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            fo = serializer.validated_data['FoId']
            try:
                foo = CaFO.objects.filter(foNo=fo)
                for fo in foo:
                    PerdiumLock = fo.foPerdiumLock
                    fid = fo.id
                fuel = DaFuel.objects.filter(FoId=fid)
                print(fuel)
                print(fid)
            except CaFO.DoesNotExist:
                return Response({'error': 'FO not found'}, status=status.HTTP_404_NOT_FOUND)

            if fuel:
                if not PerdiumLock:
                    serializer.save(fkUserId=request.user)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response({'error': 'Someone is Working Fuel for this FO'}, status=status.HTTP_409_CONFLICT)
            else:
                return Response({'error': 'You have to do Fuel 1st'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FaStsViewSet(ModelViewSet):
    queryset = FaSts.objects.all()
    serializer_class = FaStsSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FltBoloViewSet(ModelViewSet):
    queryset = FltBolo.objects.all()
    serializer_class = FltBoloSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TRLBoloViewSet(ModelViewSet):
    queryset = TRLBolo.objects.all()
    serializer_class = TRLBoloSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FltComesaViewSet(ModelViewSet):
    queryset = FltComesa.objects.all()
    serializer_class = FltComesaSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TRLComesaViewSet(ModelViewSet):
    queryset = TRLComesa.objects.all()
    serializer_class = TRLComesaSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FltInsuranceViewSet(ModelViewSet):
    queryset = FltInsurance.objects.all()
    serializer_class = FltInsuranceSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TRLInsuranceViewSet(ModelViewSet):
    queryset = TRLInsurance.objects.all()
    serializer_class = TRLInsuranceSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FltThirdPartyViewSet(ModelViewSet):
    queryset = FltThirdParty.objects.all()
    serializer_class = FltThirdPartySerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TRLThirdPartyViewSet(ModelViewSet):
    queryset = TRLThirdParty.objects.all()
    serializer_class = TRLThirdPartySerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TyerNewViewSet(ModelViewSet):
    queryset = TyerNew.objects.all()
    serializer_class = TyerNewSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TyerReturnViewSet(ModelViewSet):
    queryset = TyerReturn.objects.all()
    serializer_class = TyerReturnSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        customer = self.get_object()
        serializer = self.get_serializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(UserId=User.objects.get(id=request.user.id))
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerContactViewSet(ModelViewSet):
    queryset = CustomerContact.objects.all()
    serializer_class = CustomerContactSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        customer = self.get_object()
        serializer = self.get_serializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BbMtrlViewSet(ModelViewSet):
    queryset = BbMtrl.objects.all()
    serializer_class = BbMtrlSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BcMtrlViewSet(ModelViewSet):
    queryset = MtrCat.objects.all()
    serializer_class = MtrlCatSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DrvDjiboutiViewSet(ModelViewSet):
    queryset = DjboutiPass.objects.all()
    serializer_class = DrvDjiboutiPassSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        driver_id = self.request.query_params.get('DrvId')
        if driver_id is not None:
            queryset = queryset.filter(DrvId=driver_id)
        return queryset

    def retrieve(self, request, pk=None):
        try:
            djbouti_pass = self.get_object()
            serializer = self.get_serializer(djbouti_pass)
            return Response(serializer.data)
        except DjboutiPass.DoesNotExist:
            return Response({'error: Djibouti Passport not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            drv_id = serializer.validated_data['DrvId']
            # Check if a Truck with the same TrlId, DrvId, and FltId already exists
            if DjboutiPass.objects.filter(DrvId=drv_id).exists():
                raise ValidationError("A Djibouti Passport with the same Driver ID already exists.")

            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            djbouti_pass = self.get_object()
        except DjboutiPass.DoesNotExist:
            return Response({'error': 'Djibouti Passport not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(djbouti_pass, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConditionViewSet(ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    # permission_classes = IsAuthenticated

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserActionLogView(ModelViewSet):
    queryset = UserActionLog.objects.all()
    serializer_class = UserActionLogSerializer


class InfractionTypeViewSet(ModelViewSet):
    queryset = InfractionType.objects.all()
    serializer_class = InfractionTypeSerializer
    # permission_classes = IsAuthenticated

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class InfractionViewSet(ModelViewSet):
    queryset = Infraction.objects.all()
    serializer_class = InfractionSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fkUserId=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




