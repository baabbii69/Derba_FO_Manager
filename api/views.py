from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class DriverViewSet(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def retrieve(self, request, pk=None):
        if pk is not None:
            try:
                driver = Driver.objects.get(pk=pk)
                driver_serializer = DriverSerializer(driver)
                emergency_contact = DrvEmergecyContact.objects.get(driverID=driver)
                emergency_contact_serializer = DrvEmergencyContactSerializer(emergency_contact)
                licence = DrvLicence.objects.get(driverID=driver)
                licence_serializer = DrvLicenceSerializer(licence)

                data = {
                    'driver': driver_serializer.data,
                    'emergency_contact': emergency_contact_serializer.data,
                    'licence': licence_serializer.data
                }
                return Response(data)
            except Driver.DoesNotExist:
                return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)
            except (DrvEmergecyContact.DoesNotExist, DrvLicence.DoesNotExist):
                return Response({'error': 'Driver information not found'}, status=status.HTTP_404_NOT_FOUND)

        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data)

    def create(self, request):
        driver_serializer = DriverSerializer(data=request.data['driver'])
        emergency_contact_serializer = DrvEmergencyContactSerializer()
        licence_serializer = DrvLicenceSerializer()

        if driver_serializer.is_valid():
            driver = driver_serializer.save()
            emergency_contact_serializer = DrvEmergencyContactSerializer(data=request.data['emergency_contact'])
            licence_serializer = DrvLicenceSerializer(data=request.data['licence'])

            if emergency_contact_serializer.is_valid() and licence_serializer.is_valid():
                emergency_contact = emergency_contact_serializer.save(driverID=driver, fkUserId=request.user.id)
                licence = licence_serializer.save(driverID=driver, fkUserId=request.user.id)

                return Response({
                    'driver': driver_serializer.data,
                    'emergency_contact': emergency_contact_serializer.data,
                    'licence': licence_serializer.data
                }, status=status.HTTP_201_CREATED)

        errors = {}
        errors.update(driver_serializer.errors)
        errors.update(emergency_contact_serializer.errors)
        errors.update(licence_serializer.errors)
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            driver = Driver.objects.get(pk=pk)
            emergency_contact = DrvEmergecyContact.objects.get(driverID=driver)
            licence = DrvLicence.objects.get(driverID=driver)
        except Driver.DoesNotExist:
            return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

        driver_serializer = DriverSerializer(driver, data=request.data.get('driver'))
        emergency_contact_serializer = DrvEmergencyContactSerializer(emergency_contact,
                                                                    data=request.data.get('emergency_contact'))
        licence_serializer = DrvLicenceSerializer(licence, data=request.data.get('licence'))

        if driver_serializer.is_valid() and emergency_contact_serializer.is_valid() and licence_serializer.is_valid():
            driver_serializer.save()
            emergency_contact_serializer.save()
            licence_serializer.save()
            return Response(driver_serializer.data)
        else:
            return Response({
                'driver_errors': driver_serializer.errors,
                'emergency_contact_errors': emergency_contact_serializer.errors,
                'licence_errors': licence_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            driver = self.get_object()
            emergency_contact = DrvEmergecyContact.objects.get(driverID=driver)
            licence = DrvLicence.objects.get(driverID=driver)
        except Driver.DoesNotExist:
            return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

        driver.delete()
        emergency_contact.delete()
        licence.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TrailerViewSet(ModelViewSet):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer

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
            serializer.save()
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
