from django.http import HttpResponse
from django.contrib.auth import login
from django.middleware.csrf import get_token
from rest_framework import status as http_status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.serializers import UserRegistrationSerializer, UserPublicSerializer


def api_root(request):
    return HttpResponse(
        """
        <html>
            <head>
                <title>Parking Manager API</title>
            </head>
            <body>
                <h1>Parking Manager API</h1>
                <p>And... Hello world, sure.</p>
            </body>
        </html>
        """
    )


class UserRegistrationView(APIView):
    """Create a new user (register). Accepts username, password, optional email. Logs the user in on success."""

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request, user)
        return Response(
            UserPublicSerializer(user).data,
            status=http_status.HTTP_201_CREATED,
        )


class CsrfTokenView(APIView):
    """Return the CSRF token so the frontend can send it on subsequent POST/PATCH/DELETE. Call with credentials."""

    def get(self, request):
        token = get_token(request)
        return Response({"csrfToken": token})