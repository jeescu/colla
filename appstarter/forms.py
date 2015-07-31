from django import forms


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


class UserForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class ProfileForm(forms.Form):
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    middle_name=forms.CharField(required=True)
    position=forms.CharField(required=True)
    mail=forms.CharField(required=True)