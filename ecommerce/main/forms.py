from django import forms

class AddProduct(forms.Form):
    name = forms.CharField(label="Product Name",max_length=200)
    category = forms.CharField(label="Category", max_length=200)
    brand = forms.CharField(label="Brand", max_length=200)
    description = forms.CharField(label="Description", max_length=200)
    price = forms.IntegerField(label="Price")
