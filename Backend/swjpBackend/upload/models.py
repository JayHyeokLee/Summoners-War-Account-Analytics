from django.db import models

class UploadedJSONFile(models.Model):
    file = models.FileField(upload_to='json_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class UserAVG(models.Model):
    userID = models.IntegerField(primary_key=True)
    userName = models.CharField()
    globalAVG = models.DecimalField(max_digits=5, decimal_places=2)
    vioAVG = models.DecimalField(max_digits=5, decimal_places=2)
    willAVG = models.DecimalField(max_digits=5, decimal_places=2)
    swiftAVG = models.DecimalField(max_digits=5, decimal_places=2)
    desAVG = models.DecimalField(max_digits=5, decimal_places=2)
    sealAVG = models.DecimalField(max_digits=5, decimal_places=2)