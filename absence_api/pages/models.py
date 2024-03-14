from django.db import models

class Absence(models.Model):
    ABSENCE_REASONS = [
        ('AW', 'Accident at Work'),
        ('BH', 'Bank Holiday'),
        ('BV', 'Bereavement'),
        ('CO', 'College'),
        ('DL', 'Dependent Leave'),
        ('DR', 'Doctors/Dentists'),
        ('HP', 'Holiday Paid'),
        ('HO', 'Hospital'),
        ('JU', 'Jury Service'),
        ('MA', 'Maternity Leave'),
        ('NS', 'Non Sickness Absence'),
        ('PA', 'Paternity Leave'),
        ('SA', 'Sickness Absence'),
        ('TR', 'Training'),
        ('UA', 'Unauthorised Absence'),

    ]
    employee_code = models.CharField(max_length=255)
    absence_date = models.DateField()
    absence_reason = models.CharField(max_length=2, choices=ABSENCE_REASONS)

    def __str__(self):
        return f'{self.employee_code}: {self.absence_date}'
