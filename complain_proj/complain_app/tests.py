from django.test import TestCase
from .models import *
from django.urls import reverse

class ComplainTest(TestCase):
    
    def setUp(self):
        self.data = {'first_name': 'pidor', 'last_name': 'gnida', 'username': 'klapon_kota', 'home_adress':'parashany', 'password': 'podvodnik228'}
        self.jopa = User.objects.create_user(**self.data)
        self.category = Category.objects.create(name = 'Polenno')
        self.complain = Complain.objects.create(written_by = self.jopa, category = self.category, content = 'dsgsgdh', image = 'dgdhd')
        
    def test_create(self):
        data = {'first_name': 'pidor', 'last_name': 'gnidaxxx', 'username': 'klapon_kotaxxx', 'home_adress':'parashanxxxxy', 'password': 'podvodnik2xxx28'}
        response = self.client.post('/auth/users/', data)
        self.assertEqual(response.status_code, 201)
        
    def test_auth(self):
        data = {'username': self.data['username'], 'password':self.data['password']}
        response = self.client.post('/auth/token/login/', data)
        self.assertTrue('auth_token' in response.content.decode())
        
    def test_get_complains(self):
        data = {'id': self.jopa.pk}
        response = self.client.post(reverse('user-get-complains'), data)
        self.assertTrue(self.complain.content in response.content.decode())
        
    
# Create your tests here.
