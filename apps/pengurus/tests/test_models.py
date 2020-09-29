from django.test import TestCase
from apps.pengurus.models import User


class ModelsTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="lion", )
        User.objects.create(name="cat",)

    def test_home_page_status_code(self):
       response = self.client.get('/')
       self.assertEquals(response.status_code, 200)

    def test_animals_can_speak(self):
        lion = User.objects.get(name="lion")
        cat = User.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
