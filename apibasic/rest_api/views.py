from .models import Farms
from .serializers import FarmsSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_condition import Or, And
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
# Create your views here.


class ExampleList(generics.ListAPIView):

    queryset = []
    serializer_class = FarmsSerializer
    permission_classes = [AllowAny]

class FarmsList(generics.ListCreateAPIView):

    queryset = Farms.objects.all()
    serializer_class = FarmsSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [And(TokenHasReadWriteScope, TokenHasScope)]
    required_scopes = ['api-web']


