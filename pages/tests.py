from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView

# Create your tests here.


class HomepageTests(SimpleTestCase):
    print("\n\nInitiating HomepageTests\n")

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        print("\n\tTesting homepage status code ")
        # response = self.client.get('/')  <--this is now handled by setUp()
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        print("\n\tTesting reverse of homepage url name")

        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        print("\n\tTesting template usage")

        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        print("\n\tTesting for correct html")
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        print("\n\tTesting for no incorrect html")
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page')

    def test_homepage_url_resolves_homepageview(self):  # new
        print("\n\tTesting that the homepage url resolves to homepageview")
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTest(SimpleTestCase):

    print("Initializing AboutPage Tests")

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        print("\n\tTesting AboutPage status code")
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        print("\n\tTesting AboutPage template")
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        print("\n\tTesting AboutPage contents")
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_does_not_contain_correct_html(self):
        print("\n\tTesting AboutPage incorrect contents")
        self.assertNotContains(
            self.response, 'random text that should not be there')

    def test_aboutpage_url_resolves_aboutpageview(self):
        print("\n\tTesting AboutPage url ")
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
