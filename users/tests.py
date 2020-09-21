from django.test import TestCase
from django.urls import reverse
from .models import CustomUser
from django.contrib.auth import get_user_model

# Create your tests here.

class CustomUserTests(TestCase):

    def  setup(self):
        self.user = get_user_model().objects.create_user(
            username = "Amjad",
            email = "amjad@gmail.com",
            password = "1234+4321"
        )

    def test_home_page_status_code(self):
        expected = 200
        url = reverse('home')
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEquals(expected,actual)
        
    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        actual = 'home.html'
        self.assertTemplateUsed(response, actual)

    def test_signup_page_template(self):
        url = reverse('signup')
        response = self.client.get(url)
        actual = 'registration/signup.html'
        self.assertTemplateUsed(response, actual)

    def test_Model_str(self):
        user = CustomUser('mohamad')
        actual = user.username
        expected = str(user)
        self.assertEqual(expected, actual)
