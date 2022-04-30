from django.db import models
import uuid

# Create your models here.
class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)