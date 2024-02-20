from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
class Products(models.Model):
    """Model representing a product."""
    title = models.CharField(max_length=100)
    description =  models.TextField()
    price = models.DecimalField( max_digits=10, decimal_places=2)
    created_at = models.DateTimeField( auto_now_add=True)
# Create your models here.
    def __str__(self):
        return self.title

@receiver(pre_save, sender=Products)
def update_field(sender, instance):
    """Signal receiver function to update the 'created_at' field."""
    instance.created_at = timezone.now()
    print(timezone.now())
