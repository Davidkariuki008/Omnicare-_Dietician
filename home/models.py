from django.db import models


class Details(models.Model):
    class Meta:
        verbose_name_plural = 'Details'

    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]


    activity_choices = [
        ('Sedentary (little or no exercise)', 'Sedentary (little or no exercise)'),
        ('Lightly active (1-3 days/week)', 'Lightly active (1-3 days/week)'),
        ('Moderately active (3-5 days/week)', 'Moderately active (3-5 days/week)'),
        ('Very active (6-7 days/week)', 'Very active (6-7 days/week)'),
        ('Super active (twice/day)', 'Super active (twice/day)'),
    ]

    name = models.CharField(max_length=100)
    gender = models.CharField(choices=gender_choices, max_length=100)
    weight = models.IntegerField()
    height = models.IntegerField()
    age = models.IntegerField()
    activity = models.CharField(choices=activity_choices, max_length=100)





    def __str__(self):
        return '{}'.format(self.name).capitalize()

