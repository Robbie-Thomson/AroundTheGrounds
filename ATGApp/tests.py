from django.test import TestCase
from ATGApp.models import Stadium,UserProfile,User
from django.core.urlresolvers import reverse
import populate_ATGApp
from PIL import Image
import pathlib
import datetime
import os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client

#Test
def create_user():
    # Create a user
    user = User.objects.get_or_create(username="testuser", password="test1234",
                                      first_name="Test", last_name="User", email="testuser@testuser.com")[0]
    user.set_password(user.password)
    user.save()

    # Create a user profile
    user_profile = UserProfile.objects.get_or_create(user=user)[0]
    user_profile.save()

    return user_profile

'''def add_stadium(name,capacity,postcode,description,homeTeam):
    stadium = Stadium()
    stadium.name = name
    stadium.capacity = capacity
    stadium.postcode = postcode
    stadium.description = description
    stadium.homeTeam = homeTeam
    stadium.photo = SimpleUploadedFile(name='Allianz_Arena.jpeg', content=open(pathlib.Path("C:\\Users\\jackm\\OneDrive\\Desktop\\Allianz_Arena.jpeg"), 'rb').read(), content_type='image/jpeg')
    stadium.user_id = 1
    stadium.save()
    return stadium
    '''

def setUp(self):
    self.client = Client()

class generalTests(TestCase):
    def test_login(self):
        client = Client()
        create_user()
        login = self.client.login(username="testuser",password="test1234")
        response = self.client.get("http://127.0.0.1:8000/ATGApp/")
        self.assertTrue(login)
        self.assertNotIn(str(response.content),"Log in")
        self.assertNotIn(str(response.content),"Sign Up")

class StadiumTests(TestCase):

    def test_stadium_name_slug(self):
        stadium = Stadium()
        stadium.name = 'Best Stadium In The World'
        stadium.user_id = 1
        stadium.save()
        self.assertEqual(stadium.slug,"best-stadium-in-the-world")

    def test_add_a_stadium(self):

        print("This is the path of the image ")
        
        # done
        image_path = os.path.normpath(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'around_the_grounds', 'static', 'images'))

        image = open(os.path.join(image_path, 'OldTrafford.jpg'), 'rb')
        
        print(image_path)
        
        #image = open(os.path.join(image_path, 'OldTrafford.jpg'), 'rb')
        client = Client()
      
        #Create a user and log in
        create_user()
        
        login = self.client.login(username="testuser",password="test1234")
      
        #Post a stadium to the add stadium page
        response = self.client.post('http://127.0.0.1:8000/ATGApp/add_stadium/',{'name':"Test",'capacity':500,'postcode':"G61 3QG",'homeTeam':"Home FC",'description':"Decent","photo":image,'TotalScore':0,'ReviewCount':0,'averageScore':0,'Review_count':0,'total_Score':0,'average':0,'latitude':0,'longitude':0})

        #Check that the post worked
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')

class ReviewTests(TestCase):
  
    def test_add_a_review(self):
       
        # changed 
        image_path = os.path.normpath(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'around_the_grounds', 'static', 'images'))
    
        print("This is the path")
            
        print(image_path)
        
        image = open(os.path.join(image_path, 'OldTrafford.jpg'), 'rb')
            
            #Create a user and log in
        create_user()

        login = self.client.login(username="testuser",password="test1234")
            
        #Post a stadium to the add stadium page
        response = self.client.post('http://127.0.0.1:8000/ATGApp/add_stadium/',{'name':"Test",'capacity':500,'postcode':"G61 3QG",'homeTeam':"Home FC",'description':"Decent","photo":image,'TotalScore':0,'ReviewCount':0,'averageScore':0,'Review_count':0,'total_Score':0,'average':0,'latitude':0,'longitude':0})

        #Post a review to the test stadium page
        reponse = self.client.post('http://127.0.0.1:8000/ATGApp/writeReview/test/',{'atmosphere':0,'food':0,'facilities':0,'additionalInfo':"TestReview",'date':str(datetime.datetime.now()),'totalScore':0,})
            
        #Set response to test stadium page
        response = self.client.get("http://127.0.0.1:8000/ATGApp/chosenStadium/test/")

        self.assertContains(response,"TestReview")


class MyAccountTests(TestCase):

    def test_account_page(self):
        #Create a user and log in
        create_user()
        
        login = self.client.login(username="testuser",password="test1234")
        
        image_path = os.path.normpath(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'around_the_grounds', 'static', 'images'))
    
        image = open(os.path.join(image_path, 'OldTrafford.jpg'), 'rb')
        #Post a stadium to the add stadium page
        response = self.client.post('http://127.0.0.1:8000/ATGApp/add_stadium/',{'name':"Test",'capacity':500,'postcode':"G61 3QG",'homeTeam':"Home FC",'description':"Decent","photo":image,'TotalScore':0,'ReviewCount':0,'averageScore':0,'Review_count':0,'total_Score':0,'average':0,'latitude':0,'longitude':0})

        #Post a review to the test stadium page
        response = self.client.post('http://127.0.0.1:8000/ATGApp/writeReview/test/',{'atmosphere':0,'food':0,'facilities':0,'additionalInfo':"TestReview",'date':str(datetime.datetime.now()),'totalScore':0})
      
        #Set response to test user page
        response = self.client.get("http://127.0.0.1:8000/ATGApp/account/")

        self.assertContains(response,"TestReview")
        
        
        
