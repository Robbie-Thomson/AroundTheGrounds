# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'around_the_grounds.settings')
import django 
django.setup()
from django.contrib.auth.models import User
from ATGApp.models import UserProfile, Stadium, Review

from django.core.files import File

def generate_user():

    print("This is the file path for images below")
    print()

    image_path = os.path.normpath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'around_the_grounds', 'static', 'images'))
   
    print()
    print(str(image_path))
    print()

    old_trafford_image = open(os.path.join(image_path, 'OldTrafford.jpg'), 'rb')
    celtic_park_image = open(os.path.join(image_path, 'celtic-park.jpg'), 'rb')
    anfield_image = open(os.path.join(image_path, 'Anfield.jpg'), 'rb')
    allianz_image = open(os.path.join(image_path, 'Allianz.jpg'), 'rb')
    nou_image = open(os.path.join(image_path, 'NouCamp.jpg'), 'rb')
    bernabeu_image = open(os.path.join(image_path, 'Bernabeu.jpg'), 'rb')
    dortmund_image = open(os.path.join(image_path, 'Dortmund.jpg'), 'rb')
    juve_image = open(os.path.join(image_path, 'Juventus.jpg'), 'rb')

    OTFile = File(old_trafford_image, 'rb')
    CelticFile = File(celtic_park_image, 'rb')
    CampFile = File(nou_image, 'rb')
    AllianzFile = File(allianz_image, 'rb')
    AnfieldFile = File(anfield_image, 'rb')
    BernabeuFile = File(bernabeu_image, 'rb')
    DortmundFile = File(dortmund_image, 'rb')
    JuveFile = File(juve_image, 'rb')

    # Create sample users for the website and thier associated profiles
    # Create the first new user
    new_user = User.objects.get_or_create(username = "Fitba99")[0]
    new_user.first_name="Joe"
    new_user.last_name="Bloggs"
    new_user.save()
    p = UserProfile.objects.create(user=new_user)
    p.save()

    # Create a second new user 
    new_user2 = User.objects.get_or_create(username = "JohnS67")[0]
    new_user2.first_name="John"
    new_user2.last_name="Smith"
    new_user2.save()
    p2 = UserProfile.objects.create(user=new_user2)
    p2.save()

    new_user3 = User.objects.get_or_create(username = "LiverpoolFan")[0]
    new_user3.first_name="Craig"
    new_user3.last_name="Gunn"
    new_user3.save()
    p3 = UserProfile.objects.create(user=new_user3)
    p3.save()

    new_user4 = User.objects.get_or_create(username = "TartanArmy101")[0]
    new_user4.first_name="Davie"
    new_user4.last_name="Shakespeare"
    new_user4.save()
    p4 = UserProfile.objects.create(user=new_user4)
    p4.save()

    new_user5 = User.objects.get_or_create(username = "MarkyBoy23")[0]
    new_user5.first_name="Mark"
    new_user5.last_name="Reynolds"
    new_user5.save()
    p5 = UserProfile.objects.create(user=new_user5)
    p5.save()


    # then a dictionary of stadiums for the users to add 
    Old_Trafford_Reviews = [
        {"atmosphere": 1,
        "food": 5, 
        "facilities": 3,
        "additionalInfo":"What a place",
        },
        {"atmosphere": 3,
        "food": 1, 
        "facilities": 5,
        "additionalInfo":"Brilliant day",
        }]
    
    Camp_Nou_Reviews = [
        {"atmosphere": 4,
        "food": 4, 
        "facilities": 3,
        "additionalInfo":"Incredible",
        },
        {"atmosphere": 2,
        "food": 3, 
        "facilities": 3,
        "additionalInfo":"Football's greatest",
        }]

    
    Stadiums = {"Old Trafford": 
    {"Reviews": Old_Trafford_Reviews,
    "capacity":76000,
    "postcode":"M16ORA",
    "description": "Old Trafford was opened in 1910 and has been home to Premier League side Manchester United FC ever since. The ground had to undergo major renovation after the Second World War air raids left the stadium seriously damaged. This took a rebuilding job of 8 years and during this time Manchester United played their games at Maine Road, Manchester City’s ground at the time. Old Trafford was one of the venues during the 1966 World Cup and hosted 3 group stage matches in Euro 1996.  The stadium has recorded a record attendance of 76,962 in a match between Wolverhampton Wanderers and Grimsby Town.",
    "hometeam": "Manchester United FC",
    "TotalScore": 26,
    "ReviewCount":2,
    "photo":OTFile,
	"latitude": "53.463634",
	"longitude": "-2.291211"},

        "Camp Nou": {"Reviews": Camp_Nou_Reviews,
        "capacity": 99354,
        "postcode":"08028 Barcelona",
        "description": "The Camp Nou was built between 1954 and 1957 and officially opened its doors in 1957 in a game between the club and some players from Warsaw. The stadium was first named Estadi del FC Barcelona but was soon renamed Camp Nou. The stadium originally had some standing areas which were turned into seats in the 1990s. In order to maintain the enormous capacity, the club decided to lower the pitch. The stadium has hosted finals of the European Cup on 2 occasions and has been home to some of the worlds greatest players including Johan Cruyff, Diego Maradona and Lionel Messi.",
        "hometeam": "FC Barcelona",
        "TotalScore":30,
        "ReviewCount":2,
        "photo":CampFile,
		"latitude": "41.381556",
		"longitude": "2.122648"}}

    add_stadium("Anfield", 54074, "L4 OTH", 
    "Anfield is the home of Liverpool Football club since 1892 and is the sixth largest football staium in England. The stadium was originally owned by Merseyside rivals Everton until a dispute between the clubs led to the Toffees moving to their current ground Goodison Park. The record attendance of 61,905 for the ground was set in 1952 in game against Wolverhampton Wanderers.", 
    "Liverpool FC", 0, 0, p3, AnfieldFile, "53.431175","-2.961002")

    add_stadium("Allianz Arena", 75000, 
    "80939 Munchen, Germany", 
    "The Allianz Arena replaced Munich’s old Olympiastadion. The club made plans for a new stadium back in 1997, and even though the city of Munich initially preferred the idea of modernising the Olympiastadion, they eventually went ahead with the clubs’ proposal for an entire new stadium. The Allianz Arena boasts an average attendance of 71,000, bettered only by the Camp Nou, Old Trafford and Singal Iduna Park.", 
    "FC Bayern Munich", 0, 0, p2, AllianzFile, "48.219615", "11.624707")

    add_stadium("Celtic Park", 60832, "G403RE", 
    "Celtic Park, also known as paradise and Parkhead, is home to Celtic Football Club, the champions of the Scottish Permiership and the double treble winners. The stadium was opened in 1892 and in 1898 a new stand was built which was the first 2 tier stand at a football gorund which could fit 50,000 fans. The record attendance for Celtic park is 92,000.", 
    "Celtic FC", 0, 0, p2, CelticFile, "55.850407", "-4.205457")

    add_stadium("Santiago Bernabeu", 81044, "28036 Madrid", 
    "The Santiago Bernabeu has been the home of European Giants Real Madrid since 1947. The arena has hosted many major finals including the European Cup final in 1957, 1969, and 2010. Los blancos have played at the stadium since 1947 and was named after Santiago Bernabeu, the club president at the time. The stadium at one time could fit 125,000 fans but was reduced to its current capacity after many renovations that took place in the 1900s.", 
    "Real Madrid CF", 0, 0, p5, BernabeuFile, "40.454132", "-3.688259")

    add_stadium("Signal Iduna Park", 81365, "Strobelallee 50, 44139 Dortmund", 
    "The Signal Iduna Park, formerly known as the WestfieldStadion, was opened in 1974 and is one of the largest football grounds in Germany. The stadium is well known around the world for its famous “Yellow Wall”, the largest free-standing football stand in Europe. The Signal Iduna Park became the first stadium ever to record an average attendance of over 81,000 in the 2015/16 season and averaged 79,496 last season, the best in Germany. The capacity of the Signal Iduna Park is reduced by almost 16,000 for non-domestic matches to meet UEFA and FIFA guidelines. ",
    "Borussia Dortmund", 0, 0, p3, DortmundFile, "51.4926", "7.4519")

    add_stadium("Allianz Stadium", 41507, "Corso Gaetano Scirea, 50", 
    "The Allianz Stadium is located in Turin, Italy and is home to Italian giants Juventus since 2011.  It earned its new name in 2017 after a sponsorship was formed between the insurance company and the stadium’s owners. The stadium was opened in 2011 and was built to replace the Stadio Delle Alpi, which only became home to the club in 1990 and struggled to gain fan approval due to the distance between the park and the stands which caused a lack of atmosphere.", 
    "Juventus FC", 0, 0, p4, JuveFile, "45.1096", "7.6413")

    for stadium, stadiumData in Stadiums.items():
    
        s = add_stadium(stadium, stadiumData["capacity"], stadiumData["postcode"], stadiumData["description"], stadiumData["hometeam"], stadiumData["TotalScore"], stadiumData["ReviewCount"], p2, stadiumData["photo"], stadiumData["latitude"], stadiumData["longitude"])
        
        print(s)

        for review in stadiumData["Reviews"]:

            add_review(s, p, review["atmosphere"], review["food"], review["facilities"], review["additionalInfo"])

    for s in Stadium.objects.all():

        for r in Review.objects.all():

            print("- {0} - {1} ".format(str(s), str(r)))

    old_trafford = Stadium.objects.get(name="Old Trafford")

    add_review(old_trafford, p4, 5,3,1,"Glory Glory Man United")
    
    allianz_arena = Stadium.objects.get(name="Allianz Arena")
    
    add_review(allianz_arena, p2, 4,4,4,"Best atmosphere in Germany.")

    celtic_park = Stadium.objects.get(name="Celtic Park")

    add_review(celtic_park, p5, 5,3,2, "Best Atmosphere in the world.")

    juventus_stadium = Stadium.objects.get(name ="Allianz Stadium")

    add_review(juventus_stadium, p5, 3,3,2,"Facilities should be better, boring game 0-0.")

    bernabeu = Stadium.objects.get(name ="Santiago Bernabeu")

    add_review(bernabeu, p, 5,3,2,"Not the same since CR7 left")

    anfield = Stadium.objects.get(name ="Anfield")

    add_review(anfield, p3, 4,4,3, "Mon the reds")

    NouCamp = Stadium.objects.get(name ="Camp Nou")

    add_review(NouCamp, p4, 5,4,1, "Messi is not human")

    add_review(NouCamp, p2, 4,4,4, "Total football")

    dortmund = Stadium.objects.get(name="Signal Iduna Park")

    add_review(dortmund, p, 5,2,2, "Yellow wall is different class")

def add_stadium(name, capacity, postcode, description, hometeam, totalScore, reviewCount, user, photo, latitude, longitude):

    print("This is inside the add stadium function\n",name, capacity, postcode, description, hometeam, totalScore, reviewCount, user)

    stadium = Stadium.objects.create(name=name, user=user)

    print(stadium.name)
    stadium.description = description
    stadium.capacity = capacity
    stadium.postcode = postcode
    stadium.homeTeam = hometeam
    stadium.TotalScore = totalScore
    stadium.ReviewCount = reviewCount
    stadium.photo = photo
    stadium.latitude = latitude
    stadium.longitude = longitude
	
    stadium.save()

    print(stadium,"-",stadium.user,"-",stadium.slug)

    return stadium

def add_review(stadium, user, atmosphere, food, facilities, Info):

    review = Review.objects.create(stadium=stadium, user=user)
    review.atmosphere = atmosphere
    review.food = food
    review.facilities = facilities
    review.additionalInfo = Info

    review.save()

    print(review)
    
    return review


    # then need a dictionary of reviews made by users on the stadiums



    # need to remember to hard code the field entry for the reviews
    # counter and the totalScore in the stadium records as they can't be 
    # dynamically calculated yet. 


if __name__== '__main__':
    print("Created the new user profile ")
    generate_user()


