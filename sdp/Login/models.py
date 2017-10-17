from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=250)
    user_id = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    mail_id = models.CharField(max_length=250)
    dob = models.CharField(max_length=250)
    batch = models.CharField(max_length=250)
    profile_pic = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.name + ' - ' + self.batch


