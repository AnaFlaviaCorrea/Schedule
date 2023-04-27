from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    phone = models.IntegerField()
    height = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()
    date_birth = models.DateField()
    active = models.BooleanField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Contacts'
