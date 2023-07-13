from django import forms
from .models import Building

class BuildingForm(forms.ModelForm):
    owner_name = forms.CharField(label="Owner's Name")
    L_G_A = forms.CharField(label="L.G.A")
    number_flats = forms.CharField(label="Number Of Flats")
    email = forms.EmailField(label="E-mail")
    phone_number = forms.CharField(label="Phone Number")
    agent_id = forms.CharField(label="Agent Id")

    class Meta:
        model = Building
        fields = ('owner_name', 'address', 'building_type', 'number_flats', 'amount_value',  'ansidd_no', 'L_G_A', 'email', 'phone_number', 'agent_id', 'image')
