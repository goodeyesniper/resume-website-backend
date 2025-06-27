from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactMessageSerializer
from django.core.mail import send_mail
from django.conf import settings

class ContactMessageView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Optional: Send email notification to yourself
            send_mail(
                subject="New Contact Form Message",
                message=(
                    f"Name: {serializer.data['name']}\n"
                    f"Email: {serializer.data['email']}\n\n"
                    f"Message:\n{serializer.data['message']}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_FORM_EMAIL],
                fail_silently=False,
            )

            return Response({"success": "Message sent successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
