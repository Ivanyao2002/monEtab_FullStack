from django.db import models
import datetime

# Create your models here.

SUBJECT_CHOICES = (
    ('math', 'Math'),
    ('physique', 'Physique'),
    ('anglais', 'Anglais'),
    ('svt', 'SVT'),
    ('histoire', 'Histoire'),
    ('français', 'Français'),
)

VACCANT_CHOICE = (
    ('OUI', 'OUI'),
    ('NON', 'NON'),
)

class TeacherModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    is_vacant = models.CharField(max_length=20, choices=VACCANT_CHOICE) 
    city = models.CharField(max_length=30)
    phone = models.PositiveIntegerField(unique=True, blank=True)
    subject_taught = models.CharField(max_length=20, choices=SUBJECT_CHOICES)  
    next_class = models.CharField(max_length=50)
    next_meeting_topic = models.CharField(max_length=100)  

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject_taught}"

    @property
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Professeur'
        verbose_name_plural = 'Professeurs'