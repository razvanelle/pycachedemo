from django.db import models
from django.db.models.signals import post_save, post_delete, post_init
from django.dispatch import receiver
from cachedemo.api import prjcache


class Project(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)

# callback methods for update/delete signals
@receiver([post_save], sender=Project, dispatch_uid="update_project")
def signal_update(sender, instance, **kwargs):
  print("POST_UPDATE: ", instance.id, '-', instance.name)
  prjcache.put(instance.id, prjcache.getTimeStr())

@receiver([post_delete], sender=Project, dispatch_uid="delete_project")
def signal_delete(sender, instance, **kwargs):
  print("POST_DELETE: ", instance.id, '-', instance.name)
  prjcache.put(instance.id, prjcache.getTimeStr())

