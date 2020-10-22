from django import template
from ATGApp.models import Stadium, Review

register = template.Library()

@register.inclusion_tag('atg/stadiums.html')
def get_stadium_list():
    return {'stadiums': Stadium.objects.all()}