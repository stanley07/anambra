from django import forms
from .models import Building

class BuildingForm(forms.ModelForm):
    owner_name = forms.CharField(label="Owner's Name")
    geographical_zone = forms.CharField(label="Geographical Zone")
    number_flats = forms.CharField(label="Number Of Flats")
    email = forms.EmailField(label="E-mail")
    phone_number = forms.CharField(label="Phone Number")

    class Meta:
        model = Building
        fields = ('owner_name', 'address', 'building_type', 'number_flats', 'amount_value', 'contact', 'ansidd_no', 'geographical_zone', 'email', 'phone_number', 'image')
