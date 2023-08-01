from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from django.conf import settings
import random
from django.contrib.auth import get_user_model


class UserAccountManager(BaseUserManager):
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Username field is required to open an Account')

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)

        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)

        user.set_password(password)
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserAccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']


class Driver(models.Model):
    driver_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    permanent_residence = models.CharField(max_length=255)
    driver_dmc_id = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    Job_title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    employment_status = models.CharField(max_length=255)
    note_on_driver = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.driver_name


class DrvEmergecyContact(models.Model):
    driverID = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)
    drvContactName = models.CharField(max_length=255)
    drvContactPhone = models.CharField(max_length=255)
    drvContactRelatinship = models.EmailField(max_length=255)
    drvContactAdress = models.CharField(max_length=255)
    drvContactActiveStatus = models.BooleanField(default=False)
    fkUserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.drvContactName


class DrvLicence(models.Model):
    driverID = models.OneToOneField(Driver, related_name='licence', on_delete=models.CASCADE, null=True, blank=True)
    drvLicenceNumber = models.CharField(max_length=255)
    drvLicenceAuthority = models.CharField(max_length=255)
    drvLicenceIssueDate = models.DateField()
    drvLicenceExpiryDate = models.DateField()
    drvLicenceActiveStatus = models.BooleanField(default=False)
    fkUserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.drvLicenceNumber


class DrvLeave(models.Model):
    driverID = models.ForeignKey(Driver, on_delete=models.CASCADE)
    drvLeaveType = models.CharField(max_length=255)
    AddressDuringLeave = models.CharField(max_length=255)
    drvLeaveStartDate = models.DateField(null=True, blank=True)
    drvLeaveEndDate = models.DateField(null=True, blank=True)
    LastworkDate = models.DateField(null=True, blank=True)
    FirstWorkDate = models.DateField(null=True, blank=True)
    leavefilledDate = models.DateField(null=True, blank=True)
    leavedays = models.CharField(max_length=255)
    fkUserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.drvLeaveType


class Condition(models.Model):
    condition = models.CharField(max_length=255)

    def __str__(self):
        return self.condition


class Trailer(models.Model):
    fleet_number = models.CharField(max_length=255)
    plate_number = models.CharField(max_length=255)
    trailer_type = models.CharField(max_length=255)
    capacity = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    chasis_number = models.CharField(max_length=255)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, null=True, blank=True)
    remarks = models.TextField(max_length=255, null=True, blank=True)
    trailer_model = models.CharField(max_length=255)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.fleet_number


class DrvPassport(models.Model):
    DrvId = models.OneToOneField(Driver, related_name='passport', on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    drvPassportNo = models.CharField(max_length=255)
    drvPassportIssuanceDate = models.DateField()
    drvPassportExpireDate = models.DateField()
    drvPassportActiveStatus = models.BooleanField()


class CustomerContact(models.Model):
    cntName = models.CharField(max_length=255)
    cntPhone = models.CharField(max_length=20)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.cntName


class Customer(models.Model):
    cmrName = models.CharField(max_length=255)
    cmrTIN = models.CharField(max_length=255)
    cmrAddress = models.CharField(max_length=255)
    cmrPhone = models.CharField(max_length=20)
    cmrCode = models.CharField(max_length=255)
    contactID = models.ForeignKey(CustomerContact, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)


class FbStsCat(models.Model):
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    stsCatCol = models.CharField(max_length=255)
    stsCatDesc = models.CharField(max_length=255)


class BbMtrl(models.Model):
    mtrName = models.CharField(max_length=255)
    mtrCat = models.CharField(max_length=255)
    mtrPackaging = models.CharField(max_length=255)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)


class BaTrip(models.Model):
    trpOrigin = models.CharField(max_length=255)
    trpDestination = models.CharField(max_length=255)
    trpDistanceKm = models.IntegerField()
    trpRouteName = models.CharField(max_length=255)
    trpTurnaroundTime = models.IntegerField()
    trpAvrgFuel = models.IntegerField()
    trpDays = models.IntegerField()
    trpLBltr = models.IntegerField()
    trpRltr = models.IntegerField()
    trpSltr = models.IntegerField()
    trpTltr = models.IntegerField()
    trpUltr = models.IntegerField()
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.trpRouteName


class DjboutiPass(models.Model):
    DrvId = models.ForeignKey(Driver, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    drvDjiboutiPassNo = models.CharField(max_length=255)
    drvDjiboutiPIssuanceDate = models.DateField()
    drvDjiboutiPExpDate = models.DateField()
    drvDjiboutiPActiveStatus = models.BooleanField()


class AaFleetNo(models.Model):
    fltFleetNo = models.CharField(max_length=255)
    fltPlateNo = models.CharField(max_length=255)
    fltCapacity = models.CharField(max_length=255)
    fltMake = models.CharField(max_length=255)
    fltModel = models.CharField(max_length=255)
    fltActive = models.BooleanField()
    fltYear = models.DateField()
    fltTrkEngineNo = models.CharField(max_length=255)
    fltTrkChasNo = models.CharField(max_length=255)
    fltType = models.CharField(max_length=255)
    fltAxleNo = models.IntegerField()
    fltEngineType = models.CharField(max_length=255)
    fltEnginePower = models.IntegerField()
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.fltFleetNo


class AbTruck(models.Model):
    FltId = models.ForeignKey(AaFleetNo, on_delete=models.CASCADE)
    DrvId = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    TrlId = models.ForeignKey(Trailer, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    trkActive = models.BooleanField()

    def __str__(self):
        return f'{self.FltId} : {self.TrlId}'


class DbFuelStn(models.Model):
    fkUserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    stnName = models.CharField(max_length=255)


class CaFO(models.Model):
    TrkId = models.ForeignKey(AbTruck, on_delete=models.CASCADE)
    TrpId = models.ForeignKey(BaTrip, on_delete=models.CASCADE)
    MtrId = models.ForeignKey(BbMtrl, on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ShipmentCode = models.CharField(max_length=255)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    foNo = models.CharField(max_length=25)
    foDate = models.DateField()
    foTime = models.TimeField()
    foOpenKm = models.IntegerField()
    foRmk = models.TextField()
    foRtnDate = models.DateField()
    foRtnTime = models.TimeField()
    foCloseKm = models.IntegerField()
    foMtrQuantity = models.DecimalField(max_digits=10, decimal_places=2)
    foWbNo = models.CharField(max_length=255)
    foWbBill = models.CharField(max_length=255)
    foFuelLock = models.BooleanField(default=False)
    foPerdiumLock = models.BooleanField(default=False)
    foAdvanceLock = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.foNo}'

    def save(self, *args, **kwargs):
        # Set the ShipmentCode based on the given format (foNo - cmrcode - last two digits of the year)
        if not self.ShipmentCode:
            customer_code = self.CustomerID.cmrCode if self.CustomerID else ''
            year_last_digits = str(self.foDate.year)[-2:]
            self.ShipmentCode = f"{self.foNo}-{customer_code}-{year_last_digits}"
        super().save(*args, **kwargs)


class DaFuel(models.Model):
    FoId = models.ForeignKey(CaFO, on_delete=models.CASCADE, null=True)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    fuelStationID = models.IntegerField()
    fuelPmtType = models.CharField(max_length=255)
    fuelCapNo = models.CharField(max_length=255)
    fuelAmt = models.DecimalField(max_digits=10, decimal_places=2)
    fuelCashBirr = models.DecimalField(max_digits=10, decimal_places=2)
    fuelCapRmk = models.TextField()
    fuelCashRmk = models.TextField()


class FaSts(models.Model):
    TrkId = models.ForeignKey(AbTruck, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    stsDate = models.DateField()
    stsCatOne = models.CharField(max_length=255)
    stsCatTwo = models.CharField(max_length=255)
    stsCatThree = models.CharField(max_length=255)
    stsCatFour = models.CharField(max_length=255)
    stsLocation = models.CharField(max_length=255)
    stsRemark = models.TextField()


class FltBolo(models.Model):
    FltId = models.ForeignKey(AaFleetNo, on_delete=models.CASCADE)
    TrkId = models.ForeignKey(AbTruck, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    FltBolo_no = models.CharField(max_length=255)
    FltBoloissuedate = models.DateField()
    FltBoloExpireDate = models.DateField()
    FltBoloActive = models.BooleanField()


class TRLBolo(models.Model):
    TrlId = models.ForeignKey(Trailer, on_delete=models.CASCADE)
    TrkId = models.ForeignKey(AbTruck, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    trlBolo_no = models.CharField(max_length=255)
    trlBoloissuedate = models.DateField()
    trlBoloExpireDate = models.DateField()
    trlBoloActive = models.BooleanField()


class FltComesa(models.Model):
    FltId = models.ForeignKey(AaFleetNo, on_delete=models.CASCADE)
    TrkId = models.ForeignKey(AbTruck, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    FltComesaNo = models.CharField(max_length=255)
    FltComesaYellowNo = models.CharField(max_length=255)
    FltComesaIssuanceDate = models.DateField()
    FltComesaExpireDate = models.DateField()
    FltComesaCountry = models.CharField(max_length=255)
    FltComesaActive = models.BooleanField()


class TRLComesa(models.Model):
    TrlId = models.ForeignKey(Trailer, on_delete=models.CASCADE)
    TrkId = models.ForeignKey(AbTruck, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    trlComesaNo = models.CharField(max_length=255)
    trlComesaYellowNo = models.CharField(max_length=255)
    trlComesaIssuanceDate = models.DateField()
    trlComesaValidDate = models.DateField()
    trlComesaCountry = models.CharField(max_length=255)
    trlComesaActive = models.BooleanField()


class FltInsurance(models.Model):
    FltId = models.ForeignKey(AaFleetNo, on_delete=models.CASCADE)
    TrkId = models.ForeignKey(AbTruck, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    FltInsRegistrationNo = models.CharField(max_length=255)
    FltInsIssuanceDate = models.DateField()
    FltInsExpireDate = models.DateField()
    FltInsPolicyNo = models.CharField(max_length=255)
    FltInscActive = models.CharField(max_length=255)


class TRLInsurance(models.Model):
    TrlId = models.ForeignKey(Trailer, on_delete=models.CASCADE)
    TrkId = models.ForeignKey(AbTruck, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    trlInsRegistrationNo = models.CharField(max_length=255)
    trlInsIssuanceDate = models.DateField()
    trlInsValidationDate = models.DateField()
    trlInsPolicyNo = models.CharField(max_length=255)
    trlInscActive = models.CharField(max_length=255)


class FltThirdParty(models.Model):
    FltId = models.ForeignKey(AaFleetNo, on_delete=models.CASCADE)
    TrkId = models.ForeignKey(AbTruck, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    FltThirdInsNo = models.CharField(max_length=255)
    FltThirdPolicyNo = models.CharField(max_length=255)
    FltThirdIssuanceDate = models.DateField()
    FltThirdExpireDate = models.DateField()
    FltThirdActive = models.CharField(max_length=255)


class TRLThirdParty(models.Model):
    TrlId = models.ForeignKey(Trailer, on_delete=models.CASCADE)
    TrkId = models.ForeignKey(AbTruck, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    trlThirdInsNo = models.CharField(max_length=255)
    trlThirdPolicyNo = models.CharField(max_length=255)
    trlThirdIssuanceDate = models.DateField()
    trlThirdValidationDate = models.DateField()
    trlThirdActive = models.CharField(max_length=255)


class TyerNew(models.Model):
    TrkId = models.ForeignKey(AbTruck, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    NewTyerIssuNo = models.CharField(max_length=255)
    NewTyerDate = models.DateField()
    NewTyerKM = models.IntegerField()
    NewTyerBrand = models.CharField(max_length=255)
    NewTyerSerialNo = models.CharField(max_length=255)
    NewTyerRemark = models.TextField()
    NewTyerActive = models.BooleanField()
    NewTyerTableLock = models.CharField(max_length=255)


class TyerReturn(models.Model):
    NewTyerID = models.ForeignKey(TyerNew, on_delete=models.CASCADE)
    TrkId = models.ForeignKey(AbTruck, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    ReturningIssuNo = models.CharField(max_length=255)
    RtrnTyerClosingDate = models.DateField()
    RtrnTyerClosingKM = models.IntegerField()
    TyerClosingRemark = models.TextField()
    RtrnTyerActive = models.CharField(max_length=255)
    RtrnTyerTableLock = models.CharField(max_length=255)


class EaPerdiuem(models.Model):
    FoId = models.ForeignKey(CaFO, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    prdDate = models.DateField()
    prdNoDays = models.IntegerField()
    prdIsTaxable = models.CharField(max_length=255)
    prdPmtPerDay = models.DecimalField(max_digits=10, decimal_places=2)
    prdTaxblAmt = models.DecimalField(max_digits=10, decimal_places=2)
    prdDeduct = models.DecimalField(max_digits=10, decimal_places=2)
    prdNetPmt = models.DecimalField(max_digits=10, decimal_places=2)
    prdRemark = models.TextField()


class EbAdvance(models.Model):
    FoId = models.ForeignKey(CaFO, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    advDate = models.DateField()
    advParking = models.DecimalField(max_digits=10, decimal_places=2)
    advDjiboEnter = models.DecimalField(max_digits=10, decimal_places=2)
    advLoadUnload = models.DecimalField(max_digits=10, decimal_places=2)
    advTyerRepair = models.DecimalField(max_digits=10, decimal_places=2)
    advCarWash = models.DecimalField(max_digits=10, decimal_places=2)
    advFuelOnCash = models.DecimalField(max_digits=10, decimal_places=2)
    advOther = models.DecimalField(max_digits=10, decimal_places=2)
    advTotalAdv = models.DecimalField(max_digits=10, decimal_places=2)
    advRemark = models.TextField()


class EcSettlement(models.Model):
    FoId = models.ForeignKey(CaFO, on_delete=models.CASCADE)
    advID = models.ForeignKey(EbAdvance, on_delete=models.CASCADE)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    stlmDate = models.DateField()
    stlmDjiboEnter = models.DecimalField(max_digits=10, decimal_places=2)
    stlmDjiboParking = models.DecimalField(max_digits=10, decimal_places=2)
    stlmLoadUnload = models.DecimalField(max_digits=10, decimal_places=2)
    stlmLocalParking = models.DecimalField(max_digits=10, decimal_places=2)
    stlmTyerRepair = models.DecimalField(max_digits=10, decimal_places=2)
    stlmCarWash = models.DecimalField(max_digits=10, decimal_places=2)
    stlmFuelOnCash = models.DecimalField(max_digits=10, decimal_places=2)
    stlmInnerTube = models.DecimalField(max_digits=10, decimal_places=2)
    stlmOther = models.DecimalField(max_digits=10, decimal_places=2)
    stlmTotalWorkFund = models.DecimalField(max_digits=10, decimal_places=2)
    stlmTotalAdvancePaid = models.DecimalField(max_digits=10, decimal_places=2)
    stlmFinalFundToDriver = models.DecimalField(max_digits=10, decimal_places=2)
    stlmFinalFundToCompany = models.DecimalField(max_digits=10, decimal_places=2)
    stlmWorkFundRemark = models.TextField()
    stlmOtherExpenseRemark = models.TextField()
