from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Contact
from .form import ContactForm
from django.urls import reverse_lazy
from django.core.mail import send_mail


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')


class SendContact(View):
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save()
            subject = f'Сообщение с формы от {form.first_name} {form.last_name} Почта отправителя: {form.email}'
            #send_mail(subject, form.message, form.email, ['tyoaa51@gmail.com'])
        # success_url = reverse_lazy('success_page')
        return redirect('/contact/success/')


class Success(View):
    def get(self, request):
        return render(request, 'success.html')

