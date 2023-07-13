# Generated by Django 4.2.3 on 2023-07-12 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_condition_trailer'),
    ]

    operations = [
        migrations.CreateModel(
            name='AaFleetNo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fltFleetNo', models.CharField(max_length=255)),
                ('fltPlateNo', models.CharField(max_length=255)),
                ('fltCapacity', models.CharField(max_length=255)),
                ('fltMake', models.CharField(max_length=255)),
                ('fltModel', models.CharField(max_length=255)),
                ('fltActive', models.BooleanField()),
                ('fltYear', models.DateField()),
                ('fltTrkEngineNo', models.CharField(max_length=255)),
                ('fltTrkChasNo', models.CharField(max_length=255)),
                ('fltType', models.CharField(max_length=255)),
                ('fltAxleNo', models.IntegerField()),
                ('fltEngineType', models.CharField(max_length=255)),
                ('fltEnginePower', models.IntegerField()),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AbTruck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trkActive', models.BooleanField()),
                ('DrvId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.driver')),
                ('FltId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.aafleetno')),
                ('TrlId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.trailer')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BaTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trpOrigin', models.CharField(max_length=255)),
                ('trpDestination', models.CharField(max_length=255)),
                ('trpDistanceKm', models.IntegerField()),
                ('trpRouteName', models.CharField(max_length=255)),
                ('trpTurnaroundTime', models.IntegerField()),
                ('trpAvrgFuel', models.IntegerField()),
                ('trpDays', models.IntegerField()),
                ('trpLBltr', models.IntegerField()),
                ('trpRltr', models.IntegerField()),
                ('trpSltr', models.IntegerField()),
                ('trpTltr', models.IntegerField()),
                ('trpUltr', models.IntegerField()),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BbMtrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mtrName', models.CharField(max_length=255)),
                ('mtrCat', models.CharField(max_length=255)),
                ('mtrPackaging', models.CharField(max_length=255)),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CaFO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foNo', models.IntegerField()),
                ('foDate', models.DateField()),
                ('foTime', models.TimeField()),
                ('foOpenKm', models.IntegerField()),
                ('foRmk', models.TextField()),
                ('foRtnDate', models.DateField()),
                ('foRtnTime', models.TimeField()),
                ('foCloseKm', models.IntegerField()),
                ('foMtrQuantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('foWbNo', models.CharField(max_length=255)),
                ('foWbBill', models.CharField(max_length=255)),
                ('foFuelLock', models.BooleanField()),
                ('foPerdiumLock', models.BooleanField()),
                ('foAdvanceLock', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='EbAdvance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advDate', models.DateField()),
                ('advParking', models.DecimalField(decimal_places=2, max_digits=10)),
                ('advDjiboEnter', models.DecimalField(decimal_places=2, max_digits=10)),
                ('advLoadUnload', models.DecimalField(decimal_places=2, max_digits=10)),
                ('advTyerRepair', models.DecimalField(decimal_places=2, max_digits=10)),
                ('advCarWash', models.DecimalField(decimal_places=2, max_digits=10)),
                ('advFuelOnCash', models.DecimalField(decimal_places=2, max_digits=10)),
                ('advOther', models.DecimalField(decimal_places=2, max_digits=10)),
                ('advTotalAdv', models.DecimalField(decimal_places=2, max_digits=10)),
                ('advRemark', models.TextField()),
                ('FoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cafo')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TyerNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NewTyerIssuNo', models.CharField(max_length=255)),
                ('NewTyerDate', models.DateField()),
                ('NewTyerKM', models.IntegerField()),
                ('NewTyerBrand', models.CharField(max_length=255)),
                ('NewTyerSerialNo', models.CharField(max_length=255)),
                ('NewTyerRemark', models.TextField()),
                ('NewTyerActive', models.BooleanField()),
                ('NewTyerTableLock', models.CharField(max_length=255)),
                ('TrkId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.abtruck')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TyerReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReturningIssuNo', models.CharField(max_length=255)),
                ('RtrnTyerClosingDate', models.DateField()),
                ('RtrnTyerClosingKM', models.IntegerField()),
                ('TyerClosingRemark', models.TextField()),
                ('RtrnTyerActive', models.CharField(max_length=255)),
                ('RtrnTyerTableLock', models.CharField(max_length=255)),
                ('NewTyerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tyernew')),
                ('TrkId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.abtruck')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TRLThirdParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trlThirdInsNo', models.CharField(max_length=255)),
                ('trlThirdPolicyNo', models.CharField(max_length=255)),
                ('trlThirdIssuanceDate', models.DateField()),
                ('trlThirdValidationDate', models.DateField()),
                ('trlThirdActive', models.CharField(max_length=255)),
                ('TrkId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.abtruck')),
                ('TrlId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.trailer')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TRLInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trlInsRegistrationNo', models.CharField(max_length=255)),
                ('trlInsIssuanceDate', models.DateField()),
                ('trlInsValidationDate', models.DateField()),
                ('trlInsPolicyNo', models.CharField(max_length=255)),
                ('trlInscActive', models.CharField(max_length=255)),
                ('TrkId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.abtruck')),
                ('TrlId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.trailer')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TRLComesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trlComesaNo', models.CharField(max_length=255)),
                ('trlComesaYellowNo', models.CharField(max_length=255)),
                ('trlComesaIssuanceDate', models.DateField()),
                ('trlComesaValidDate', models.DateField()),
                ('trlComesaCountry', models.CharField(max_length=255)),
                ('trlComesaActive', models.BooleanField()),
                ('TrkId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.abtruck')),
                ('TrlId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.trailer')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TRLBolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trlBolo_no', models.CharField(max_length=255)),
                ('trlBoloissuedate', models.DateField()),
                ('trlBoloExpireDate', models.DateField()),
                ('trlBoloActive', models.BooleanField()),
                ('TrkId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.abtruck')),
                ('TrlId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.trailer')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FltThirdParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FltThirdInsNo', models.CharField(max_length=255)),
                ('FltThirdPolicyNo', models.CharField(max_length=255)),
                ('FltThirdIssuanceDate', models.DateField()),
                ('FltThirdExpireDate', models.DateField()),
                ('FltThirdActive', models.CharField(max_length=255)),
                ('FltId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.aafleetno')),
                ('TrkId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.abtruck')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FltInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FltInsRegistrationNo', models.CharField(max_length=255)),
                ('FltInsIssuanceDate', models.DateField()),
                ('FltInsExpireDate', models.DateField()),
                ('FltInsPolicyNo', models.CharField(max_length=255)),
                ('FltInscActive', models.CharField(max_length=255)),
                ('FltId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.aafleetno')),
                ('TrkId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.abtruck')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FltComesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FltComesaNo', models.CharField(max_length=255)),
                ('FltComesaYellowNo', models.CharField(max_length=255)),
                ('FltComesaIssuanceDate', models.DateField()),
                ('FltComesaExpireDate', models.DateField()),
                ('FltComesaCountry', models.CharField(max_length=255)),
                ('FltComesaActive', models.BooleanField()),
                ('FltId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.aafleetno')),
                ('TrkId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.abtruck')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FltBolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FltBolo_no', models.CharField(max_length=255)),
                ('FltBoloissuedate', models.DateField()),
                ('FltBoloExpireDate', models.DateField()),
                ('FltBoloActive', models.BooleanField()),
                ('FltId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.aafleetno')),
                ('TrkId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.abtruck')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FbStsCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stsCatCol', models.CharField(max_length=255)),
                ('stsCatDesc', models.CharField(max_length=255)),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FaSts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stsDate', models.DateField()),
                ('stsCatOne', models.CharField(max_length=255)),
                ('stsCatTwo', models.CharField(max_length=255)),
                ('stsCatThree', models.CharField(max_length=255)),
                ('stsCatFour', models.CharField(max_length=255)),
                ('stsLocation', models.CharField(max_length=255)),
                ('stsRemark', models.TextField()),
                ('TrkId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.abtruck')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EcSettlement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stlmDate', models.DateField()),
                ('stlmDjiboEnter', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stlmDjiboParking', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stlmLoadUnload', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stlmLocalParking', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stlmTyerRepair', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stlmCarWash', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stlmFuelOnCash', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stlmInnerTube', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stlmOther', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stlmTotalWorkFund', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stlmTotalAdvancePaid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stlmFinalFundToDriver', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stlmFinalFundToCompany', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stlmWorkFundRemark', models.TextField()),
                ('stlmOtherExpenseRemark', models.TextField()),
                ('FoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cafo')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('advID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ebadvance')),
            ],
        ),
        migrations.CreateModel(
            name='EaPerdiuem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prdDate', models.DateField()),
                ('prdNoDays', models.IntegerField()),
                ('prdIsTaxable', models.CharField(max_length=255)),
                ('prdPmtPerDay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prdTaxblAmt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prdDeduct', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prdNetPmt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prdRemark', models.TextField()),
                ('FoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cafo')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DrvPassport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drvPassportNo', models.CharField(max_length=255)),
                ('drvPassportIssuanceDate', models.DateField()),
                ('drvPassportExpireDate', models.DateField()),
                ('drvPassportActiveStatus', models.BooleanField()),
                ('DrvId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.driver')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DrvLicence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drvLicenceNumber', models.CharField(max_length=255)),
                ('drvLicenceAuthority', models.CharField(max_length=255)),
                ('drvLicenceIssueDate', models.DateField()),
                ('drvLicenceExpiryDate', models.DateField()),
                ('drvLicenceActiveStatus', models.BooleanField(default=False)),
                ('driverID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.driver')),
                ('fkUserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DrvLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressDuringLeave', models.CharField(max_length=255)),
                ('leaveType', models.CharField(max_length=255)),
                ('leaveStartingDate', models.DateField()),
                ('leaveEndingDate', models.DateField()),
                ('lastWorkDate', models.DateField()),
                ('firstWorkDate', models.DateField()),
                ('leaveFilledDate', models.DateField()),
                ('leaveDays', models.IntegerField()),
                ('DrvId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.driver')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DrvEmergecyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drvContactName', models.CharField(max_length=255)),
                ('drvContactPhone', models.CharField(max_length=255)),
                ('drvContactRelatinship', models.EmailField(max_length=255)),
                ('drvContactAdress', models.CharField(max_length=255)),
                ('drvContactActiveStatus', models.BooleanField(default=False)),
                ('driverID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.driver')),
                ('fkUserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DjboutiPass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drvDjiboutiPassNo', models.CharField(max_length=255)),
                ('drvDjiboutiPIssuanceDate', models.DateField()),
                ('drvDjiboutiPExpDate', models.DateField()),
                ('drvDjiboutiPActiveStatus', models.BooleanField()),
                ('DrvId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.driver')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DbFuelStn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stnName', models.CharField(max_length=255)),
                ('fkUserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DaFuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuelStationID', models.IntegerField()),
                ('fuelPmtType', models.CharField(max_length=255)),
                ('fuelCapNo', models.CharField(max_length=255)),
                ('fuelAmt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fuelCashBirr', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fuelCapRmk', models.TextField()),
                ('fuelCashRmk', models.TextField()),
                ('FoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cafo')),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cntName', models.CharField(max_length=255)),
                ('cntPhone', models.CharField(max_length=20)),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmrTIN', models.CharField(max_length=255)),
                ('cmrAddress', models.CharField(max_length=255)),
                ('cmrPhone', models.CharField(max_length=20)),
                ('cmrCode', models.CharField(max_length=255)),
                ('UserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('contactID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customercontact')),
            ],
        ),
        migrations.AddField(
            model_name='cafo',
            name='CustomerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer'),
        ),
        migrations.AddField(
            model_name='cafo',
            name='MtrId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bbmtrl'),
        ),
        migrations.AddField(
            model_name='cafo',
            name='TrkId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.abtruck'),
        ),
        migrations.AddField(
            model_name='cafo',
            name='TrpId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.batrip'),
        ),
        migrations.AddField(
            model_name='cafo',
            name='UserId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
