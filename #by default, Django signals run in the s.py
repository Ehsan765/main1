#by default, Django signals run in the same database transaction as the caller. This means that if a signal is triggered within a transaction and that transaction is rolled back, the operations performed in the signal will also be rolled back.


from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def mymodel_post_save(sender, instance, created, **kwargs):
    if created and instance.name == 'bad_name':
        raise ValidationError("Invalid name provided!")

def test_signal_transaction():
    try:
        with transaction.atomic():

            obj = MyModel.objects.create(name='good_name')
            print("Object created:", obj)

            obj_bad = MyModel.objects.create(name='bad_name')
            print("This line will not execute due to the error above.")
    except ValidationError as e:
        print("Caught ValidationError:", e)

test_signal_transaction()
