from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status


from .serializers import LoginSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def custom_login(request):
    serialiser = LoginSerializer(data=request.data)
    serialiser.is_valid(raise_exception=True)

    return Response(serialiser.validated_data)
