from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils.helpers import create_short_uuid


class BaseModel(models.Model):
    """
        Base Model for add uid, updated, created fields to all project models

    """

    class Meta:
        abstract = True

    uid = models.CharField(
        _("UID"),
        max_length=50,
        default=create_short_uuid,
        unique=True,
        editable=False,
        db_index=True
    )

    updated = models.DateTimeField(
        verbose_name=_("Updated At"),
        null=True, auto_now=True
    )

    created = models.DateTimeField(
        verbose_name=_("Created At"),
        null=True, auto_now_add=True
    )
