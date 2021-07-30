from django.db import models
from datetime import datetime

# Create your models here.


class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

    def archive(self):
        return super().get_queryset()


class BaseModel(models.Model):

    deleted = models.BooleanField(default=False)

    objects = BaseManager()

    class Meta:
        abstract = True


class TimestampMixin(models.Model):
    class Meta:
        abstract = True

    create_timestamp = models.DateTimeField(auto_now_add=True)
    modify_timestamp = models.DateTimeField(auto_now=True)
    delete_timestamp = models.DateTimeField(default=None, null=True, blank=True)

    def logical_delete(self):
        self.delete_timestamp = datetime.now()
        self.save()


class TestModel(BaseModel):
    pass







