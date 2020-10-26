from django.db import models

# Create your models here.
class Products(models.Model):
    class Meta:
        verbose_name_plural = 'products'
        #managed = False
#define the choices below
    It = 'Itel'
    Techno = 'Techno'
    Oking = 'Oking'
    Infinix = 'Infinix'
    Samsung = 'Samsung'
    Huawei = 'Huawei'
    Oppo = 'Oppo'
    Realme = 'Realme'
    Nokia = 'Nokia'
    Wiko = 'Wiko'
    Energizer = 'Energizer'
    SQ = 'SQ'
    Kgtel = 'KGTEL'
    Itfly = 'ITFLY'
    Vifone = 'Vifone'
    Iyou = 'IYOU'
    Guava = 'Guava'
    POA = 'Pride'
    Vital = 'Vital'
    Supply = 'Suply'
    Smartopus = 'Smartopus'
    Joytel = 'Joytel'
    Vonex = 'Vonex'
    Companies = [
        ( It , ('Itel')),
        (Techno ,('Techno')),
        (Oking , ('Oking')),
        (Infinix , ('Infinix')),
        (Samsung , ('Samsung')),
        (Huawei , ('Huawei')),
        (Oppo , ('Oppo')),
        (Realme , ('Realme')),
        (Nokia , ('Nokia')),
        (Wiko , ('Wiko')),
        (Energizer , ('Energizer')),
        (SQ , ('SQ')),
        (Kgtel , ('KGTEL')),
        (Itfly , ('ITFLY')),
        (Vifone , ('Vifone')),
        (Iyou , ('IYOU')),
        (Guava , ('Guava')),
        (POA , ('Pride')),
        (Vital , ('Vital')),
        (Supply , ('Suply')),
        (Smartopus , ('Smartopus')),
        (Joytel , ('Joytel')),
        (Vonex , ('Vonex')),
    ]
    #types of products
    ph = 'Phones'
    ch = 'Chargers'
    er = 'Earphones'
    sg = 'Screen Guard'
    Types = [
        (ph, ('Phones')),
        (ch, ('Chargers')),
        (er, ('Earphones')),
        (sg, ('Screen Guard')),
    ]
    name = models.CharField(max_length=10, unique=True)
    product_model = models.CharField(max_length=10,choices=Companies)
    quantity = models.PositiveIntegerField()
    entryprice = models.PositiveIntegerField()
    product_type = models.CharField(max_length=15,choices=Types)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
   
class Detail(models.Model):
    sold = models.BooleanField(default=False)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    Imei = models.BigIntegerField()
    def __str__(self):
        return str(self.product) + str(self.Imei)
        #managed = False

class Sales(models.Model):
    class Meta:
        verbose_name_plural = 'sales'
        #managed = False
    mpesa = 'Mpesa'
    cash = 'Cash'
    cdt = 'Credit'
    pm = [
        (mpesa, ('Mpesa')),
        (cash, ('Cash')),
        (cdt, ('Credit')),
    ]
    no = models.AutoField(primary_key=True)
    Imei = models.ForeignKey(Detail,on_delete=models.CASCADE)
    product_model = models.ForeignKey(Products, on_delete=models.CASCADE)
    date_sold = models.DateTimeField(auto_now_add=True)
    selling_price = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=10,choices=pm, default=cash)
    def __str__(self):
        return str(self.Imei) + str(self.selling_price) + str(self.product_model)
