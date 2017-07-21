from django.db import models
from django.utils.six import python_2_unicode_compatible
from channels import Group

# Create your models here.
class Room(models.Model):
    """
    Room for chat.
    """

    title = models.CharField(max_length=255)

    # Only authorized users
    staff_only = models.BooleanField(default=False)

    @property
    def websocket_group(self):
        """
        Returns the Channels Group that sockets should subscribe to to get sent
        messages as they are generated.
        """

        return Group("room-%s" % self.id)

    def str(self):
        return self.title
