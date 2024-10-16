from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import logout
from .serializers import AccountSerializer, CvsSerializer
from .models import Account
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
import pandas

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

@api_view(['POST'])
def send_email(request):
    serializer = CvsSerializer(data=request.data)
    if serializer.is_valid():
        cvs_file = request.FILES['file']
        try:
            dataframe = pandas.read_csv(cvs_file, delimiter=',')
            for index, ligne in dataframe.iterrows():
                subject = ligne['objet']
                content = ligne['content']
                emails = ligne['emails']

                send_mail(
                    subject=subject,
                    message=content,
                    from_email='abdoulazizc867@gmail.com',
                    recipient_list=[emails]
                )
                return Response(
                    {
                        'message': 'Email envoyé avec succès'
                    }, status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    'error': f'Une erreur est survenue: {str(e)}'
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    return Response(
        {
            'error': 'Données invalides!'
        }, status=status.HTTP_400_BAD_REQUEST
    )
