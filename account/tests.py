from django.test import TestCase
from .import views

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response=self.client.get('/')
        self.assertEquals(response.status_code,200)
    
    def test_home_page_contains_correct_html(self):
        response=self.client.get('/')
        self.assertContains(response,'<h1>homepage</h1>')
    
    def test_home_page_does_not_contain_incorrect_html(self):
        response=self.client.get('/')
        self.assertNoContains(response,'Hii there!I should be on this page')
    
    def test_view_uses_correct_templates(self):
        response=self.client.get('/')
        self.assertTemplateUsed(response,'testpages.html')


# Create your tests here.
