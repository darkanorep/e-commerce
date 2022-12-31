from django import forms

class AddProduct(forms.Form):
    name = forms.CharField(label="Product Name",max_length=200)
    category = forms.CharField(label="Category", max_length=200)
    brand = forms.CharField(label="Brand", max_length=200)
    description = forms.CharField(label="Description", widget=forms.Textarea)
    price = forms.IntegerField(label="Price")
    product_img = forms.ImageField(label="Image", required=False)

class AddReview(forms.Form):
    review = forms.CharField(label="Review", widget=forms.Textarea, required=False)
    review_img = forms.ImageField(label="Image", required=False)
