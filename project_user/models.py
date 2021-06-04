from django.db import models

from django.contrib.auth.models import AbstractUser


class ProjectUser(AbstractUser):

    formaloo_customer_slug = models.CharField(
        verbose_name='Formaloo customer slug',
        blank=True, null=True, max_length=20
    )

    class Meta:
        verbose_name = "Project User"
        verbose_name_plural = "Project Users"

    def __str__(self):
        """returns a Unicode “representation” of ProjectUser object."""
        return self.username
