from django.shortcuts import render
from rest_framework.views import View, APIView
from rest_framework.response import Response

from .serializers import *
from django.core import mail
from django.core.mail import send_mail

# Create your views here.
from django.conf import settings
from .email import validate_email

EMAIL_HOST_USER = settings.EMAIL_HOST_USER
recipient_list = [EMAIL_HOST_USER, ]

recipient_email = settings.EMAIL_HOST_USER


class homeView(View):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        serializer = ContactSerializer(data=request.POST)
        if serializer.is_valid():
            full_name = serializer.validated_data.get('full_name')
            subject = serializer.validated_data.get("subject")
            email = serializer.validated_data.get("email", "")
            message = serializer.validated_data.get("message")
            if full_name and subject and message and email:
                try:
                    is_valid = validate_email(email)
                    if is_valid:
                        send_mail(subject, message, email, [recipient_email])
                        return render(request, 'index.html', {'message': 'Mail successfully sent'})
                    else:
                        error_message = f'Invalid recipient email address: {str(e)}'
                        return render(request, 'index.html', {'message': error_message})
                except Exception as e:
                    error_message = f'Failed to send email with error: {str(e)}'
                    return render(request, 'index.html', {'message': error_message})

                
            else:
                error_message = f'Incomplete form data: {str(serializer.errors)}'
                return render(request, 'index.html', {'message': error_message})
        else:
            print(serializer.errors)
            return render(request, 'index.html', {'message': 'Invalid form data'})

    

        

