from django.db import models
from django.contrib.auth.models import User

class StudentResult(models.Model):
    TERM_CHOICES = [
        ('First Term', 'First Term'),
        ('Second Term', 'Second Term'),
        ('Third Term', 'Third Term'),
    ]
    
    YEAR_CHOICES = [
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    term = models.CharField(max_length=20, choices=TERM_CHOICES)
    year = models.CharField(max_length=4, choices=YEAR_CHOICES)
    subject = models.CharField(max_length=100)
    class_score = models.IntegerField()
    exam_score = models.IntegerField()
    total_score = models.IntegerField()
    grade = models.CharField(max_length=5)
    remarks = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student.username} - {self.subject} ({self.term} {self.year})"