# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    test = models.CharField(max_length=255, null=True, blank=True)
    rest = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Xer(models.Model):

    #__Xer_FIELDS__
    zer = models.CharField(max_length=255, null=True, blank=True)
    ter = models.IntegerField(null=True, blank=True)

    #__Xer_FIELDS__END

    class Meta:
        verbose_name        = _("Xer")
        verbose_name_plural = _("Xer")



#__MODELS__END
