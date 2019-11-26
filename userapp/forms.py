
import django.forms  as forms

class ContactForm (forms.Form):
    name= forms.CharField(max_length=100, label="Name")
    email = forms.EmailField(max_length=100, label="Email")
    phone = forms.CharField (max_length=10, label="Phone")
    mobile = forms.CharField(max_length=10, label="Mobile")


