from django.db import models

# Create your models here.


class Transactions(models.Model):
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_location = models.CharField(max_length=255)
    additional_information = models.CharField(max_length=255)
    transaction_date = models.DateField()

    def if_cost(self):
        return self.amount < 0


        from django.db import models
