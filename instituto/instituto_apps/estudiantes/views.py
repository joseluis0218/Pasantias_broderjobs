from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from users.models import User

# Create your views here.


def BuscarCvs(request):

    return render(request, 'estudiante/buscar-cvs.html')
