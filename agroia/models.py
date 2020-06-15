from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Method(models.Model):
    title = models.CharField(max_length=100,unique=True)
    detail = models.CharField(max_length=500)
    upload_by = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    date_upload = models.DateField(default = timezone.now)
    command = models.CharField(max_length=500, default="python")
    file = models.FileField(upload_to="methods", null=True)
    def __str__(self):
        return '{}'.format(self.title)

class Item(models.Model):
    title = models.CharField(max_length=100,unique=True)
    detail = models.CharField(max_length=500)
    method = models.ForeignKey(Method,on_delete=models.CASCADE, default=1)
    upload_by = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    date_upload = models.DateField(default = timezone.now)
    image = models.ImageField(upload_to="crops", null=False)
    image_result = models.CharField(max_length=500, blank=True, null=True)
    txt_result = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return '{}'.format(self.title)
