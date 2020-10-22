from django import forms
from ATGApp.models import Review, Stadium, UserProfile
from django.contrib.auth.models import User

class addStadiumForm(forms.ModelForm):
        
    name = forms.CharField(Stadium._meta.get_field("name").max_length, help_text="Please enter the Stadium name.")
    capacity = forms.IntegerField(Stadium._meta.get_field("capacity").max_length, help_text="Please the Stadiums Capacity.")
    postcode = forms.CharField(Stadium._meta.get_field("postcode").max_length, help_text="Please enter the Postcode of the Stadium.")
    homeTeam = forms.CharField(Stadium._meta.get_field("homeTeam").max_length, help_text="What is the home team that plays at the Stadium.")
    description = forms.CharField(Stadium._meta.get_field("description").max_length, help_text="Please give a small description of the Stadium. (MAX 500 characters)", widget = forms.TextInput(attrs={'class':'largeInput'}))
    latitude = forms.CharField(widget=forms.TextInput(attrs={'id':'latitude', 'type':'hidden'}), max_length=Stadium._meta.get_field("latitude").max_length)
    longitude = forms.CharField(widget=forms.TextInput(attrs={'id':'longitude', 'type':'hidden'}), max_length=Stadium._meta.get_field("longitude").max_length)
    #image input
    photo = forms.ImageField(help_text = "Upload a picture of the stadium ")
    
    ##HIDDEN##
    #user_id = forms.CharField(widget=forms.HiddenInput())
    Review_count = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    total_Score = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    average = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Stadium
        fields = ('name', 'homeTeam', 'capacity', 'description', 'postcode', 'latitude', 'longitude', 'photo')


class ReviewForm(forms.ModelForm):

    Number_Choices=[('1','Unacceptable'), ('2','Poor'), ('3','Satisfactory'), ('4','Good'), ('5','Exellent')]

    # dont need to add the stadium name as we access the stadium page then click
    # the add review link which takes the slug of the stadium as a perameter in the url for 
    # its add review page. We then use this slug after the form submitted to get 
    # the asscociated stadium object the review is for and assign this to the stadium field 
    # for the review. We then get the current logged in userProfile, We then save the stadium which updates the total score the date and then updates 
    # the total score and the number of reviews for the stadium that has just been reviewed. 
   
    atmosphere = forms.IntegerField(help_text='Atmosphere:', widget=forms.RadioSelect(choices=Number_Choices))
    food = forms.IntegerField(help_text='Food:', widget=forms.RadioSelect(choices=Number_Choices))
    facilities = forms.IntegerField(help_text = "Facilities:", widget=forms.RadioSelect(choices=Number_Choices))
    additionalInfo = forms.CharField(max_length=200, help_text="Please include any additonal information about your visit", required = False, widget = forms.TextInput(attrs={'class':'largeInput1'}))
    
    # The following fields are the hidden fields 
    totalScore = forms.IntegerField(widget = forms.HiddenInput(), initial=0)
    
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Review
        fields = ('atmosphere', 'food', 'facilities', 'additionalInfo')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


