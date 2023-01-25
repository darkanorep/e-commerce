from django import forms

class AddProduct(forms.Form):

    GENDER = (  ('Men\'s', 'Men\'s'),
                ('Women\'s', 'Women\'s'),
                ('Kids', 'Kids'),)

    CATEGORIES = (  ('Tops', 'Tops'),
                    ('Bottoms', 'Bottoms'),
                    ('Footwear', 'Footwear'),
                    ('Accessories', 'Accessories'),
                    ('Hat', 'Hat'),
                    ('Bag', 'Bag'),)

    name = forms.CharField(label="Product Name",max_length=200)
    gender = forms.ChoiceField(choices = GENDER)
    category = forms.ChoiceField(choices = CATEGORIES)
    brand = forms.CharField(label="Brand", max_length=200)
    description = forms.CharField(label="Description", widget=forms.Textarea)
    price = forms.IntegerField(label="Price")
    product_img = forms.ImageField(label="Image", required=False)

class AddReview(forms.Form):
    review = forms.CharField(label="Review", widget=forms.Textarea, required=False)
    review_img = forms.ImageField(label="Image", required=False)
