import django_tables2 as tables 
from Physical.models import Products
class PhoneData(tables.Tables):
    name = tables.Column()
    product_model = tables.Column()
    product_type = tables.Column()
    quantity  = tables.Column()

    class Meta:
        attrs = {"class": "producttable"}
        model = Products
        template_name="django_tables2/bootstrap.html"
        fields = ("Type","Name","Model","Quantity")