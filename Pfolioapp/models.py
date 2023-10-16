from django.db import models

# Create your models here.

class ContactUS(models.Model):
    full_name = models.CharField(max_length=63)
    email = models.EmailField(max_length = 150)
    subject = models.CharField(max_length=225)
    message = models.TextField()

    def __str__(self):
        return f'{self.full_name} sent mail with subject: {self.subject}'
