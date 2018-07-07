from django.db import models


class Person(models.Model):
    username = models.CharField(max_length = 40)
    currency= models.CharField(max_length = 40, null=True, editable = True)


    def __str__(self):
        return "UserName : %s , currency : %s " %(self.username, self.currency)