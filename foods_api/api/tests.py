from django.test import TestCase
from django.urls import reverse


class FoodCategoriesAPIViewTest(TestCase):
    """Testing API views."""
    fixtures = ['cats_and_foods.json']

    def test_get_categories_with_published_food(self):
        response = self.client.get(reverse('food_categories'))
        self.assertEqual(response.status_code, 200)

        with open('api/fixtures/expected.json', 'r') as file:
            # Format expected JSON to oneline string
            expected = ''.join(list(map(lambda line: line.strip(), file.readlines()))).replace(': ', ':')
        self.assertContains(response, expected)
