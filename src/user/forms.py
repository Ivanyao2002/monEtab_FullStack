from django import forms
from .models import UserModel

# class UserForm(forms.Form):
#     pseudo = forms.CharField(label="Pseudo", max_length=15, strip=True, required=True)
#     password = forms.CharField(label="Mot de passe",min_length=8, widget= forms.PasswordInput(), required=True)
#     password_confirm = forms.CharField(label="Confirmation du mot de passe",min_length=8, widget= forms.PasswordInput(), required=True)

#     def clean_password(self):
#         password = self.cleaned_data.get('password') 
#         password_confirm = self.cleaned_data.get('password_confirm') 

#         forbidden_characters = ['$', '&', '#', '{', '[', '£']
#         if any(char in password for char in forbidden_characters): 
#             raise forms.ValidationError("Le mot de pass ne doit pas contenir les valeurs suivant: '&', '#', '{', '[','£','$' ") 

#         if password and password_confirm and password != password_confirm:
#             raise forms.ValidationError("Les mots de passe ne correspondent pas.")
#         return password
 
class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ["pseudo", "password"]

        widgets = {
            'pseudo': forms.TextInput(attrs={'placeholder': 'Prénom'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }