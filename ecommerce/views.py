from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .forms import ContactForm

def home_page(request):
	return render(request, "home_page.html")

def about_page(request):
	return render(request, "about_page.html")

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	form = ContactForm()
	context = {
		"title":"Contacto",
		"form": form
	}
	if contact_form.is_valid():
		print(form.cleaned_data)
		if request.is_ajax():
			return JsonResponse({"message": "Obrigado pelo seu contacto"})

	if contact_form.errors:
		errors = contact_form.errors.as_json()
		if request.is_ajax():
			return HttpResponse(errors, status=400, content_type='application/json')
	
	return render(request, "contact/view.html", context)


