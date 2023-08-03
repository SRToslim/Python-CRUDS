from autoslug import AutoSlugField
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
)

RELIGION = (
    ('islam', 'Islam'),
    ('hinduism', 'Hinduism'),
    ('christian', 'Christian'),
    ('buddhism', 'Buddhism'),
)


class Customer(models.Model):
    name = models.CharField(max_length=155, unique=True, blank=False, null=False)
    slug = AutoSlugField(populate_from='name', null=True, blank=True, unique=True, default=None)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.CharField(max_length=16, blank=True, null=True, unique=True)
    dob = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name='Date of Birth')
    age = models.CharField(max_length=5, blank=False, null=False)
    address = models.TextField(max_length=300, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, default=None, blank=True)
    religion = models.CharField(max_length=10, choices=RELIGION, default=None, blank=True)
    image = models.ImageField(upload_to='user/', blank=True, null=True, default='default_user.png')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return str(f'{self.email}')

    def Image(self):
        return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))
