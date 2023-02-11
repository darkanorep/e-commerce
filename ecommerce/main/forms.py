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
    stripe_id = forms.CharField(label="StripeID")
    product_img = forms.ImageField(label="Image", required=False)

class AddReview(forms.Form):
    review = forms.CharField(label="Review", widget=forms.Textarea, required=False)
    review_img = forms.ImageField(label="Image", required=False)


class menShoesSize(forms.Form):
    Size = (
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
        ('46', '46'),
        ('47', '47'),
    )

    size = forms.ChoiceField(required = True, choices=Size, widget=forms.RadioSelect(), initial=40)

class womenShoesSize(forms.Form):
    Size = (
        ('35', '35'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
    )

    size = forms.ChoiceField(required = True, choices=Size, widget=forms.RadioSelect(), initial=35)

class kidShoesSize(forms.Form):
    Size = (
        ('24', '24'),
        ('25', '25'),
        ('27', '27'),
        ('28', '28'),
        ('30', '30'),
        ('31', '31'),
        ('32', '32'),
    )

    size = forms.ChoiceField(required = True, choices=Size, widget=forms.RadioSelect(), initial=24)

class clothesSize(forms.Form):
    Size = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    )

    size = forms.ChoiceField(required = True, choices=Size, widget=forms.RadioSelect(), initial='S')