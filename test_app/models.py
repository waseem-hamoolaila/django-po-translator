from django.db import models
from django.utils.translation import gettext_lazy as _

class TestModel(models.Model):
    
    name = models.CharField(_("Hello"), max_length=100)
    last_name = models.CharField(_("Helo"), max_length=150)
    
    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Tests")