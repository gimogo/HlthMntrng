from django.test import TestCase 
import unittest
from service.models import Location
from service.models import Hospital

# Create your tests here.

class LocationModelTest(TestCase):
    
   @classmethod
   def setUpTestData(cls):
       Location.objects.create(city='Dhaka') 

   @classmethod
   def test_location_max_length(self):
       location = Location.objects.get(id=1)
       max_length = location._meta.get_field('city').max_length 
       message = "OK"

       self.assertTrue(max_length <= 50, message)
        

class HospitalModelTest(TestCase):
    
   
   def test_correct_hospital_created(self):

       self.hospital=Hospital.objects.create(name='test name edited')
       self.assertEquals(str(self.hospital),'test name edited')

if __name__ == "__main__":
 
    unittest.main()
