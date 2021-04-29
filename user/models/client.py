from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Client(models.Model):

    user = models.ForeignKey(User, verbose_name=_("client user"), on_delete=models.CASCADE)
    first_name = models.CharField(_("first name"), max_length=50, null= True, blank=True)
    last_name = models.CharField(_("last name"), max_length=50, null=True, blank=True)
    email = models.EmailField(_("e-mail"), max_length=254, null=False, blank=False, unique=True)
    phone = models.CharField(_("phone number"), max_length=50, null=True, blank=True)
    active = models.BooleanField(_("active"))
    created_at = models.DateTimeField(_("created at"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True, auto_now_add=False)

    def __str__(self):
        return '{}'.format(self.user)

    class Meta:
        db_table = 'client'
        managed = True
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        permissions = (
            ("can_make_order", "Can Make Order"),
            ("can_active_client", "Can Active Client")
        )
    
    @property
    def full_name(self):
        """
            Return the client full name if exists
            Else None
        """
        if self.first_name & self.last_name:
            return '{f_name}-{l_name}'.format(
                f_name=self.first_name, l_name=self.last_name
            )
        return None