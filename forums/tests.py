from django.test import TestCase 
import unittest
from forums.models import Post

# Create your tests here.

class PostModelTest(TestCase):
    
   
   @classmethod
   def test_correct_length(self):

       self.title=Post.objects.create(title='Covid 19 update')
       length = self.title._meta.get_field('title').max_length
       message = "OK"

       self.assertTrue(length <= 100, message)
        

if __name__ == "__main__":
 
    unittest.main()