from django import forms
from .models import StudentModel

class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentModel
        fields = "__all__"
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro Matricule'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'classroom': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError("Le téléphone doit contenir uniquement des chiffres.")
        return phone 

# class StudentForm(forms.Form):
#     registration_number = forms.CharField(label="Matricule", max_length=20, strip=True, required=True)
#     first_name = forms.CharField(label="Nom", max_length=20, strip=True, required=True)
#     last_name = forms.CharField(label="Prénoms", max_length=50, strip=True, required=True)
#     birth_date = forms.DateField(label="Date de naissance", required=True, widget=forms.SelectDateWidget())
#     city = forms.CharField(label="Ville", max_length=30, strip=True, required=True)
#     phone = forms.CharField(label="Téléphone", max_length=10, strip=True, required=True)
#     classroom = forms.CharField(label="Classe", max_length=20, strip=True, required=True)

#     def clean_phone(self):
#         phone = self.cleaned_data.get('phone')
#         if not phone.isdigit():
#             raise forms.ValidationError("Le téléphone doit contenir uniquement des chiffres.")
#         return phone
