from django.db import models
import datetime

# Create your models here.

CLASSROOM_CHOICES = (
    ('Tle', 'Terminale'),
    ('1ere', 'Première'),
    ('2nde', 'Deuxième'),
    ('3eme', 'Troisième'),
    ('4eme', 'Quatrième'),
    ('5eme', 'Cinquième'),
    ('6eme', 'Sixième'),
)

GENDER_CHOICES = (
    ('H', 'Homme'),
    ('F', 'Femme'),
)

class StudentModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=30, unique=True)
    birth_date = models.DateField()
    classroom = models.CharField(max_length=20, choices=CLASSROOM_CHOICES)
    phone = models.CharField(max_length=10, unique=True, blank=True)
    city = models.CharField(max_length=30) 
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='Homme')

    def __str__(self) -> str:
        return f"{self.registration_number} - {self.first_name} {self.last_name}"
    
    @property
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Élève'
        verbose_name_plural = 'Élèves'
