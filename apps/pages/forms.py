from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={
        'class':'form-control',
         'placeholder': 'Full Name'
        }))
    email = forms.EmailField(max_length=100, required=True, widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder': 'E-Mail Address'
        }))
    message = forms.CharField(max_length=400, required=False, widget=forms.TextInput(
        attrs={
        'class':'form-control1',
        'placeholder': 'Your Message'
        }) )