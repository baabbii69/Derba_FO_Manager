# signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Driver)
@receiver(post_delete, sender=Driver)
@receiver(post_save, sender=DrvEmergecyContact)
@receiver(post_delete, sender=DrvEmergecyContact)
@receiver(post_save, sender=DrvLicence)
@receiver(post_delete, sender=DrvLicence)
@receiver(post_save, sender=DrvLeave)
@receiver(post_delete, sender=DrvLeave)
@receiver(post_save, sender=Condition)
@receiver(post_delete, sender=Condition)
@receiver(post_save, sender=Trailer)
@receiver(post_delete, sender=Trailer)
@receiver(post_save, sender=DrvPassport)
@receiver(post_delete, sender=DrvPassport)
@receiver(post_save, sender=CustomerContact)
@receiver(post_delete, sender=CustomerContact)
@receiver(post_save, sender=Customer)
@receiver(post_delete, sender=Customer)
@receiver(post_save, sender=FbStsCat)
@receiver(post_delete, sender=FbStsCat)
@receiver(post_save, sender=BbMtrl)
@receiver(post_delete, sender=BbMtrl)
@receiver(post_save, sender=BaTrip)
@receiver(post_delete, sender=BaTrip)
def log_user_action(sender, instance, **kwargs):
    user = instance.fkUserId if hasattr(instance, 'fkUserId') else instance.driverID.user

    if kwargs['created']:
        action = f"Created {instance.__class__.__name__}: {instance}"
    else:
        if sender.objects.filter(pk=instance.pk).exists():
            action = f"Updated {instance.__class__.__name__}: {instance}"
        else:
            action = f"Deleted {instance.__class__.__name__}: {instance}"
    UserActionLog.objects.create(user=user, action=action)
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from django.contrib.auth import get_user_model
# from django.apps import apps
# from .models import *
#
# User = get_user_model()
#
# @receiver(post_save)
# @receiver(post_delete)
# def record_user_activity(sender, instance, created, **kwargs):
#     user = instance.fkUserId if hasattr(instance, 'fkUserId') else None
#     action = 'created' if created else 'updated'
#     model_name = sender.__name__  # Get the model name dynamically
#     UserActivity.objects.create(user=user, action=action, model_name=model_name)
#
#
# for model in [Driver, DrvEmergecyContact, DrvLicence, DrvLeave, DrvPassport, CustomerContact, Customer, FbStsCat, BbMtrl, BaTrip,
#               DjboutiPass, AaFleetNo, AbTruck, DbFuelStn, CaFO, DaFuel, FaSts, FltBolo, TRLBolo, FltComesa, TRLComesa,
#               FltInsurance, TRLInsurance, FltThirdParty, TRLThirdParty, TyerNew, TyerReturn, EaPerdiuem, EbAdvance,
#               EcSettlement]:
#     post_save.connect(record_user_activity, sender=model)
#     post_delete.connect(record_user_activity, sender=model)
#
