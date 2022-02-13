from django.test import TestCase
from django.urls import reverse 


# Create your tests here.
class ConfCreatingTests(TestCase):
    def test_no_confessions(self):
        """
            If no confession is shown, it checks to see if object list is empty.
        """
        response = self.client.get(reverse('first_app:confList'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response , "NO CONFESSIONS")
        self.assertQuerysetEqual(response.context['object_list'],[])
        
