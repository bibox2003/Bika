from django.test import TestCase
from django.urls import reverse
from .models import Post  # Example model

# Example TestCase for a model
class PostModelTest(TestCase):

    def test_post_str(self):
        # Create a sample post
        post = Post.objects.create(title="Test Post", content="This is a test post")
        
        # Check that the string representation of the post is correct
        self.assertEqual(str(post), "Test Post")

# Example TestCase for a view
class HomePageViewTest(TestCase):

    def test_home_page_status_code(self):
        # Use reverse() to get the URL of the home page
        url = reverse('home')  # Make sure 'home' is the name of the URL in your urls.py
        response = self.client.get(url)  # Use the test client to perform a GET request
        
        # Check that the status code of the response is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_correct_html(self):
        url = reverse('home')
        response = self.client.get(url)
        
        # Check that the response contains specific text
        self.assertContains(response, "Welcome to My Django Website")

    def test_home_page_does_not_contain_wrong_html(self):
        url = reverse('home')
        response = self.client.get(url)
        
        # Check that the response does not contain incorrect text
        self.assertNotContains(response, "Some wrong text")
