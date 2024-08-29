from django import forms

from .models import TeacherModel

class TeacherForm(forms.ModelForm):

    class Meta:
        model = TeacherModel
        fields  = "__all__" 
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'next_class': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prochain cours'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'subject_taught': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'}),
            'is_vacant': forms.Select(attrs={'class': 'form-control', 'type':'radio'}),
            'next_meeting_topic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sujet prochaine réunion'}),
        }

    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
    #     if not phone.isdigit():
    #         raise forms.ValidationError("Le téléphone doit contenir uniquement des chiffres.")
    #     return phone 

# class TeacherForm(forms.Form):
#     first_name = forms.CharField(label="Nom", max_length=20, strip=True, required=True)
#     last_name = forms.CharField(label="Prénoms", max_length=50, strip=True, required=True)
#     birth_date = forms.DateField(label="Date de naissance", required=True, widget=forms.SelectDateWidget())
#     city = forms.CharField(label="Ville", max_length=30, strip=True, required=True)
#     phone = forms.CharField(label="Téléphone", max_length=10, strip=True, required=True)
#     subject_taught = forms.CharField(label="Matière enseignée", max_length=30, strip=True, required=True)
#     next_class = forms.CharField(label="Prochain cours", max_length=30, strip=True, required=True)
#     next_meeting_topic = forms.CharField(label="Sujet de la prochaine réunion", max_length=30, strip=True, required=True)
#     is_vacant = forms.BooleanField(label="Est vacant ?", required=False, initial=True)

#     def clean_phone(self):
#         phone = self.cleaned_data.get('phone')
#         if not phone.isdigit():
#             raise forms.ValidationError("Le téléphone doit contenir uniquement des chiffres.")
#         return phone


