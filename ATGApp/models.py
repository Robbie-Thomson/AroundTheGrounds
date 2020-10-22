from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from django.db.models.signals import post_delete
from datetime import date

# In order to get the highest rated stadium, use an sql query count total score
# then group by stadium which will show the stadium object and the total score across all reviews
# then order by count(totalScore) DESC

# This would be the SQL Query for sorting the stadium objects
# in descending order in terms of totalScore


# SELECT stadium, SUM(totalScore) FROM Reviews
# GROUP BY stadium
# ORDER BY totalScore DESC


# Create your models here.
# Create a Stadium table which will hold the data about each of the stadiums
# added that can be reviewed
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Stadium(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True, primary_key=True)
    photo = models.ImageField(upload_to='stadium_images', blank=True)
    capacity = models.IntegerField(default=0)
    postcode = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    homeTeam = models.CharField(max_length=55)
    slug = models.SlugField(unique=True)
    ReviewCount = models.IntegerField(default=0)
    TotalScore = models.IntegerField(default=0)
    averageScore = models.IntegerField(default=0)
    latitude = models.CharField(max_length=100, default="1")
    longitude = models.CharField(max_length=100, default="1")
	
    def save(self, *args, **kwargs):

        # create a counter storing the number of review objects associated with this stadium being saved
        # assign the number of reviews for this stadium to counter and store this as the
        # review count field value for this stadium.
        counter = 0
        counter = Review.objects.all().filter(stadium=self).count()
        self.ReviewCount = counter

        # keep a count of the total score
        score = 0
        # if there are reviews on the stadium
        if counter > 0:
            # get the reviews on this stadium
            reviews = Review.objects.all().filter(stadium=self)
            # fir each review
            for r in reviews:
                # add the total score for the review to the counter
                score += r.totalScore
            # when the loop has completed assign the scores across all reviews to the total
            # score of the stadium
        self.TotalScore = score

        if self.ReviewCount !=0:

            self.averageScore = self.TotalScore//self.ReviewCount
       
        else:
            
            self.averageScore = 0


        self.slug = slugify(self.name)
        super(Stadium, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'stadiums'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    atmosphere = models.IntegerField(default=0)
    food = models.IntegerField(default=0)
    facilities = models.IntegerField(default=0)
    additionalInfo = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    totalScore = models.IntegerField(blank=True)
        
    def save(self, *args, **kwargs):

        self.date = date.today()

        self.totalScore = self.atmosphere + self.food + self.facilities
        super(Review, self).save(*args, **kwargs)
        Stadium.save(self.stadium)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)

    @receiver(post_delete)
    def save_stadium_again(sender, instance, **kwargs):
        if sender == Review:
            instance.stadium.save()


# in order to update the data in the tables when a user deletes their account or
# reviews or stadi
