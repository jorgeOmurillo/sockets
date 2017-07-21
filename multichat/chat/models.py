from django.db import models
from django.utils.six import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Room(models.Model):
    """
    Room for chat.
    """

    title = models.CharField(max_length=255)

    # Only authorized users
    staff_only = models.BooleanField(default=False)

    def str(self):
        return self.title
