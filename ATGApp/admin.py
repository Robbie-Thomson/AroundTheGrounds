from django.contrib import admin


# Register your models here.
from ATGApp.models import UserProfile, Stadium, Review


class StadiumAdmin(admin.ModelAdmin):

    list_display = ('name', 'capacity', 'photo', 'homeTeam','TotalScore', 'ReviewCount', 'averageScore' , 'user')

    prepopulated_fields = {'slug': ('name', )}

class ReviewAdmin(admin.ModelAdmin):

    list_display = ('id','user', 'stadium', 'atmosphere', 'food', 'facilities', 'totalScore', 'date')

    prepopulated_fields = {}

admin.site.register(UserProfile)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Stadium, StadiumAdmin)


