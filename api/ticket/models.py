from django.db import models

# Create your models here.

class ticket(models.Model):
    UserName = models.CharField(max_length=50)
    PhoneNo = models.CharField(max_length=10)
    timing = models.DateTimeField()
    booking_time = models.DateTimeField(auto_now_add=True)
    is_expired = models.BooleanField(default=False)

    def __str__(self):
        return self.UserName

    
    