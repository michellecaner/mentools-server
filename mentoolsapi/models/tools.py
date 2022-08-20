from django.db import models

class Tools(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    tool_type = models.CharField(max_length=55)
    