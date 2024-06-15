from typing import TYPE_CHECKING

from django.test import TestCase

if TYPE_CHECKING:
    from loan_payment_schedule.payments.models import Client


class ClientModelTestCase(TestCase):

    def test_create_client(self):
        client_name = 'Test Client'
        client = Client.objects.create(name=client_name)

        # Verify if the client was created successfully
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(client.name, client_name)

    def test_create_client_blank_name(self):
        # Attempt to create a client without a name
        with self.assertRaises(ValueError):
            Client.objects.create(name='')

    def test_create_client_null_name(self):
        # Attempt to create a client with a null name
        with self.assertRaises(ValueError):
            Client.objects.create(name=None)

    def test_get_client_by_name(self):
        client_name = 'Test Client'
        Client.objects.create(name=client_name)

        # Retrieve the client and verify its name
        client = Client.objects.get(name=client_name)
        self.assertEqual(client.name, client_name)

    def test_update_client_name(self):
        client_name = 'Test Client'
        new_client_name = 'Updated Client'
        client = Client.objects.create(name=client_name)

        # Update the client's name and save it
        client.name = new_client_name
        client.save()

        # Retrieve the updated client and verify its new name
        updated_client = Client.objects.get(id=client.id)
        self.assertEqual(updated_client.name, new_client_name)

    def test_delete_client(self):
        client_name = 'Test Client'
        client = Client.objects.create(name=client_name)

        # Delete the client and verify it no longer exists
        client.delete()
        self.assertEqual(Client.objects.count(), 0)
