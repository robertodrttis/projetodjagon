from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()

    def __str__(self):
        return self.name

class WaterIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    amount = models.FloatField(default=0)

    def __str__(self):
        return f'{self.user.name} - {self.date}'
