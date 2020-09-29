from django.test import TestCase
from apps.organization.models import Organization


class ModelsTestCase(TestCase):
    def setUp(self):
        Organization.objects.create(name="lion", )
        Organization.objects.create(name="cat",)

    def test_home_page_status_code(self):
       response = self.client.get('/')
       self.assertEquals(response.status_code, 200)

    def test_animals_can_speak(self):
        lion = Organization.objects.get(name="lion")
        cat = Organization.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
