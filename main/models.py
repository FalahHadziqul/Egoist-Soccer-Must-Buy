import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('socks', 'Socks'),
        ('gloves', 'Gloves'),
        ('kPads', 'Knee Pads'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    product_views = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField(blank=True, null=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
  
    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()
