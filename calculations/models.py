from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Country(models.Model):
    code = models.CharField(max_length=100, unique=True, null=True, blank=True) #(primary_key=True)
    name = models.CharField(max_length=100)
    continent_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name

class User(models.Model):
    full_name = models.CharField(max_length=255)
    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        to_field='code',
        db_column='country_code'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class Apartment(models.Model):
    apartment_no = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    number_of_members = models.IntegerField(
        validators=[MinValueValidator(1)],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Apartment {self.apartment_no} - {self.name or 'Unnamed'}"

class ApartmentMember(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    member_fullname = models.CharField(max_length=255)
    apartment = models.ForeignKey(
        Apartment,
        on_delete=models.CASCADE,
        to_field='apartment_no',
        db_column='apartment_no'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.member_fullname} - Apartment {self.apartment.apartment_no}"

class BillShare(models.Model):
    member = models.ForeignKey(
        ApartmentMember,
        on_delete=models.CASCADE,
        related_name='bill_shares'
    )
    apartment = models.ForeignKey(
        Apartment,
        on_delete=models.CASCADE,
        related_name='bill_shares'
    )
    share_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        help_text="Percentage of bill to be paid by member"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.member.member_fullname} - {self.share_percentage}% of {self.apartment}"