from django.db import models

# Create your models here.

class Water(models.Model):
    ph=models.DecimalField(max_digits=24, decimal_places=12,null=False)
    Hardness=models.DecimalField(max_digits=24, decimal_places=12,null=False)
    Solids=models.DecimalField(max_digits=24, decimal_places=12,null=False)
    Chloramines=models.DecimalField(max_digits=24, decimal_places=12,null=False)
    Sulfate=models.DecimalField(max_digits=24, decimal_places=12,null=False)
    Conductivity=models.DecimalField(max_digits=24, decimal_places=12,null=False)
    Organic_carbon=models.DecimalField(max_digits=24, decimal_places=12,null=False)
    Trihalomethanes=models.DecimalField(max_digits=24, decimal_places=12,null=False)
    Turbidity=models.DecimalField(max_digits=24, decimal_places=12,null=False)

