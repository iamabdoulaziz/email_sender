from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import logout
from .serializers import AccountSerializer
from .models import Account
from django.contrib.auth.hashers import make_password, check_password

@api_view(['POST'])
def create_account(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        hash_password = make_password(password)
        Account.objects.create(email=email, password=hash_password)
        return Response(
            {
                'message': 'Compte créé avec successs !'
            }, status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        account = Account.objects.get(email=email)
    except Account.DoesNotExist:
        return Response(
            {'errors': 'Email non trouvé !'}, status=status.HTTP_404_NOT_FOUND
        )

    if check_password(password, account.password):
        return Response(
            {
                'message': 'Connexion établie!'
            }, status=status.HTTP_200_OK
        )
    else:
        return Response(
            {
                'error': 'Mot de passe incorrect!'
            }, status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['POST'])
def logout(request):
    logout(request)
    return Response(
        {
            'message': 'Au revoir!'
        }
    )
