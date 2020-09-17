from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
	Nome = forms.CharField(
		widget=forms.TextInput(
			attrs={
			"class":"form-control",
			 "placeholder":"Nome completo"
			}
		)
	)

	email = forms.EmailField(
		widget=forms.EmailInput(
			attrs={
			"class":"form-control",
			 "placeholder":"E-mail"
			}
		)
	)

	Mensagem = forms.CharField(
		widget=forms.Textarea(
			attrs={
			"class":"form-control",
			 "placeholder":"Mensagem"
			}
		)
	)


