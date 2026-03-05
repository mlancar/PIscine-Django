from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Article, UserFavouriteArticle

# Create your tests here.

class Test(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="marine",
            password="password123"
        )

    def test_login_required(self):
        response = self.client.get(reverse("articles:add-favourite", args=[1]))
        self.assertEqual(response.status_code, 302)  # redirection login
        
        response = self.client.get(reverse("articles:user-publications"))
        self.assertEqual(response.status_code, 302)
        
        response = self.client.get(reverse("articles:publish-articles"))
        self.assertEqual(response.status_code, 302)
        

    def test_logged_user_can_access(self):
        self.client.login(username="marine", password="password123")
        response = self.client.get(reverse("articles:add-favourite", args=[1]))
        self.assertNotEqual(response.status_code, 302)
    
    def test_user_cannot_access_register(self):
        self.client.login(username="marine", password="password123")
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 302)
    
    def test_user_cannot_access_login(self):
        self.client.login(username="marine", password="password123")
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 302)
    
    def test_add_favourite_twice(self):
        self.client.login(username="marine", password="password123")
        self.article = Article.objects.create(title="Test Article", synopsis="test", content="content", author=self.user)
        
        response = self.client.post(reverse("articles:add-favourite", args=[self.article.id]))
        self.assertEqual(response.status_code, 302)
        
        response = self.client.post(reverse("articles:add-favourite", args=[self.article.id]))
        self.assertEqual(response.status_code, 409)
        