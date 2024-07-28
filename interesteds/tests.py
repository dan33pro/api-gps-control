from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Interested


class InterestedTests(APITestCase):

    def setUp(self):
        self.interested_data = {
            "brand": "Brand A",
            "branch": "Branch A",
            "applicant": "Applicant A"
        }
        self.interested = Interested.objects.create(**self.interested_data)
        self.list_create_url = reverse('interested-list-create')
        self.detail_url = reverse(
            'interested-detail', kwargs={'pk': self.interested.pk})

    def test_get_interesteds(self):
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['brand'], self.interested.brand)

    def test_create_interested(self):
        new_interested_data = {
            "brand": "Brand B",
            "branch": "Branch B",
            "applicant": "Applicant B"
        }
        response = self.client.post(self.list_create_url, new_interested_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Interested.objects.count(), 2)
        self.assertEqual(response.data['brand'], new_interested_data['brand'])

    def test_get_interested_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['brand'], self.interested.brand)

    def test_update_interested(self):
        updated_interested_data = {
            "brand": "Updated Brand",
            "branch": "Updated Branch",
            "applicant": "Updated Applicant"
        }
        response = self.client.put(self.detail_url, updated_interested_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.interested.refresh_from_db()
        self.assertEqual(self.interested.brand,
                         updated_interested_data['brand'])

    def test_partial_update_interested(self):
        updated_interested_data = {
            "brand": "Partially Updated Brand"
        }
        response = self.client.patch(self.detail_url, updated_interested_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.interested.refresh_from_db()
        self.assertEqual(self.interested.brand,
                         updated_interested_data['brand'])

    def test_delete_interested(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Interested.objects.count(), 0)

    def test_get_interesteds_ordered_by_id(self):
        interested2 = Interested.objects.create(
            brand="Brand B", branch="Branch B", applicant="Applicant B")
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(
            response.data[0]['id_interested'], self.interested.id_interested)
        self.assertEqual(
            response.data[1]['id_interested'], interested2.id_interested)
