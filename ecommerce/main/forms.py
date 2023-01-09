from django import forms

class AddProduct(forms.Form):

    CATEGORIES = (  ('Top', 'Top'),
                    ('Bottom', 'Bottom'),
                    ('Shoes', 'Shoes'),
                    ('Watch', 'Watch'),
                    ('Jacket', 'Jacket'),
                    ('Cap', 'Cap'),
                    ('Bag', 'Bag'),
                    ('Accessories', 'Accessories'),
                    ('Mobile Phone', 'Mobile Phone'),)

    name = forms.CharField(label="Product Name",max_length=200)
    category = forms.ChoiceField(choices = CATEGORIES)
    brand = forms.CharField(label="Brand", max_length=200)
    description = forms.CharField(label="Description", widget=forms.Textarea)
    price = forms.IntegerField(label="Price")
    product_img = forms.ImageField(label="Image", required=False)

class AddReview(forms.Form):
    review = forms.CharField(label="Review", widget=forms.Textarea, required=False)
    review_img = forms.ImageField(label="Image", required=False)
