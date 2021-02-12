from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User


class Profile(AbstractUser):
    leader = models.BooleanField(
        'Team Leader',
        default=False
    )

    work_area = models.CharField(
        max_length=11,
        choices=[
            ('Project', 'Project'),
            ('Development', 'Development'),
            ('Testing', 'Testing'),
            ('Quality', 'Quality')
        ]
    )

    programming_area = models.CharField(
        max_length=9,
        choices=[
            ('Android', 'Android Developer'),
            ('Backend', 'Back-end Developer'),
            ('Dabatabse', 'Database Administrators'),
            ('Desktop', 'Desktop Developer'),
            ('DevOps', 'DevOps'),
            ('Fronend', 'Front-end Developer'),
            ('Fullstack', 'Fullstack Developer'),
            ('Iphone', 'Iphone Developer'),
            ('Software', 'Software Developer'),
            ('Testing', 'Testing')
        ]
    )
    gender = models.CharField(
        max_length=1,
        choices=[
            ('F', 'Female'),
            ('M', 'Male')
        ],
    )
    admission_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.work_area}'


class Task(models.Model):
    sender = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='send_by',
        null=True,
        blank=True
    )
    receiver = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='to'
    )
    subject = models.CharField(max_length=80)
    message = models.TextField()
    send_date = models.DateTimeField(auto_now=True)
    limit_date = models.DateTimeField()
    done = models.BooleanField(default=False)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    query_type = models.PositiveSmallIntegerField(
        choices=[
            (0, 'Consult'),
            (1, 'Claim'),
            (2, 'Suggestions')
        ]
    )
    message = models.TextField()
    send_date = models.DateField(default=datetime.now)
