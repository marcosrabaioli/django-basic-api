from django.test import TestCase
import uuid
from .models import Farms
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APITransactionTestCase
from oauth2_provider.models import AccessToken, get_application_model
from django.utils import timezone
import datetime
import secrets
import json

class OAuth2TestCase(APITestCase):
    """OAuth 2.0 authentication"""

    def create_application(self):
        Application = get_application_model()

        self.application = Application(
            name='client_credentials_authotization',
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_CLIENT_CREDENTIALS
        )

        self.application.save()

        token = secrets.token_hex(15)

        self.tok = AccessToken(token=token,
                          application=self.application,
                          expires=timezone.now() + datetime.timedelta(days=1),
                          scope='read write api-web api-monitorings')

        self.tok.save()
        self.assertEqual(Application.objects.all().count(), 1)
        self.assertEqual(AccessToken.objects.all().count(), 1)


class FarmsAPITestCase(APITestCase):


    def setUp(self):

        Application = get_application_model()

        self.application = Application(
            name='client_credentials_authotization',
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_CLIENT_CREDENTIALS
        )

        self.application.save()

        self.token = secrets.token_hex(15)

        self.tok = AccessToken(token=self.token,
                          application=self.application,
                          expires=timezone.now() + datetime.timedelta(days=1),
                          scope='read write api-web')

        self.tok.save()


    def test_post_farm(self):

        self.assertEqual(AccessToken.objects.all().count(), 1)
        farm_id = uuid.uuid4()
        url = reverse('farms-list')
        data_post_farm = {'id': str(farm_id), 'code': 1, 'lat':-29.714817, 'lng':-53.7127424,'active':True}

        response =  self.client.post(url,data_post_farm, format='json', **{"Authorization":"Bearer " + self.token})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Farms.objects.all().count(), 1)
        self.assertEqual(Farms.objects.get().id, farm_id)


    def test_list_farms(self):

        farm_id = uuid.uuid4()
        data_farm = {'id': str(farm_id), 'code': 1, 'lat': -29.714817, 'lng': -53.7127424, 'active': True}

        farm = Farms(**data_farm)
        farm.save()

        url = reverse('farms-list')
        response = self.client.get(url, format='json', **{"Authorization": "Bearer " + self.token})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], data_farm['id'])