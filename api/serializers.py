from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')


class DrvEmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrvEmergecyContact
        fields = '__all__'

class TrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        fields = '__all__'


class DrvLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrvLeave
        fields = '__all__'


class CustomerContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerContact
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class FbStsCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = FbStsCat
        fields = '__all__'


class BbMtrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = BbMtrl
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class DrvLicenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrvLicence
        fields = '__all__'


class CustomerContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerContact
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class FbStsCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = FbStsCat
        fields = '__all__'


class BbMtrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = BbMtrl
        fields = '__all__'


class BaTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaTrip
        fields = '__all__'


class DjboutiPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjboutiPass
        fields = '__all__'


class AbTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbTruck
        fields = '__all__'


class AaFleetNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AaFleetNo
        fields = '__all__'


class DbFuelStnSerializer(serializers.ModelSerializer):
    class Meta:
        model = DbFuelStn
        fields = '__all__'


class CaFOSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaFO
        fields = '__all__'
        read_only_fields = ['ShipmentCode']


class DaFuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaFuel
        fields = '__all__'


class DrvPassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrvPassport
        fields = '__all__'


class FaStsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaSts
        fields = '__all__'


class FltBoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = FltBolo
        fields = '__all__'


class TRLBoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = TRLBolo
        fields = '__all__'


class FltComesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FltComesa
        fields = '__all__'


class TRLComesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TRLComesa
        fields = '__all__'


class FltInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FltInsurance
        fields = '__all__'


class TRLInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TRLInsurance
        fields = '__all__'


class FltThirdPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = FltThirdParty
        fields = '__all__'


class TRLThirdPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = TRLThirdParty
        fields = '__all__'


class TyerNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TyerNew
        fields = '__all__'


class TyerReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = TyerReturn
        fields = '__all__'


class EaPerdiuemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EaPerdiuem
        fields = '__all__'


class EbAdvanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EbAdvance
        fields = '__all__'


class EcSettlmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcSettlement
        fields = '__all__'
