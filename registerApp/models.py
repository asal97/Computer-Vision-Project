from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

ALPHA_CHOICES = (
    ("1", "الف"),
    ("2", "ب"),
    ("3", "پ"),
    ("4", "ت"),
    ("5", "ث"),
    ("6", "ج"),
    ("7", "چ"),
    ("8", "ح"),
    ("9", "خ"),
    ("10", "د"),
    ("11", "ذ"),
    ("12", "ر"),
    ("13", "ز"),
    ("14", "ژ"),
    ("15", "س"),
    ("16", "ش"),
    ("17", "ص"),
    ("18", "ض"),
    ("19", "ط"),
    ("20", "ظ"),
    ("21", "ع"),
    ("22", "غ"),
    ("23", "ف"),
    ("24", "ق"),
    ("25", "ک",),
    ("26", "گ"),
    ("27", "ل"),
    ("28", "م"),
    ("29", "ن"),
    ("30", "و",),
    ("31", "ه"),
    ("32", "ی"),
    ("33", "D"),
    ("34", "S"),
)

PLATE_CHOICES = (
    ("1", "سواری ملی"),
    ("2", "سواری منظقه ازاد انزلی"),
    ("3", "موتور سیکلت"),)


class Plate(models.Model):
    plate_type = models.CharField(
        max_length=3,
        choices=PLATE_CHOICES,
        blank=True,
        default=1
    )

    firstNum = models.IntegerField()
    secondNum = models.IntegerField()
    cityNum = models.IntegerField(validators=[MaxValueValidator(99), MinValueValidator(10)], blank=True)
    alpha = models.CharField(
        max_length=3,
        choices=ALPHA_CHOICES,
        blank=True,
        default=1
    )

    class Meta:
        unique_together = ('firstNum', 'secondNum', 'alpha', 'cityNum')

    def __str__(self):
        return '%s %s %s %s' % (self.firstNum, self.secondNum, self.cityNum, self.alpha)


class Owner(models.Model):
    first_name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='profilePic', blank=True)
    family_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11, blank=True)
    nationalCode = models.CharField(max_length=10, unique=True)
    description = models.TextField(max_length=300)

    def __str__(self):
        return '%s %s %s %s %s' % (self.first_name, self.family_name, self.phone, self.nationalCode, self.description)


class Vehicle(models.Model):
    plate = models.OneToOneField(Plate, on_delete=models.CASCADE, blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='carPic', blank=True)
    color = models.CharField(max_length=10, blank=True)
    type = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return '%s %s %s' % (self.plate, self.color, self.type)
