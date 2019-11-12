from django.db import models

class ProductTypeModel(models.Model):
    pt_no=models.IntegerField(primary_key=True)
    pt_name=models.CharField(max_length=100)


class ProductModel(models.Model):
    p_no=models.IntegerField(primary_key=True)
    p_name=models.CharField(max_length=100)
    p_price=models.FloatField()
    p_type=models.ForeignKey(ProductTypeModel,on_delete=models.CASCADE)
