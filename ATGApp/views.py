from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from ATGApp.models import Review, Stadium, UserProfile, User
from ATGApp.forms import UserForm, UserProfileForm, addStadiumForm, ReviewForm


def index(request):
    #Returns information on highest rated stadium
    #Returns picture of highest rated stadium

    HRS = Stadium.objects.order_by('-averageScore')[:1]
    
    print(HRS)
    
    context_dict = {'h' : HRS}

    response = render(request,'ATGApp/index.html', context = context_dict)

    return response

def stadiums(request):
    #Returns top stadiums
    stadiums = Stadium.objects.order_by('-name')
    
    context_dict = {'stadiums':stadiums}
    return render(request, 'ATGApp/stadiums.html', context = context_dict)

def add_stadium(request):

    form = addStadiumForm()

    if request.method == "POST":
        
        form = addStadiumForm(request.POST,request.FILES)
    
        if form.is_valid():

            if request.user.is_authenticated():

                user = request.user
                
                stadium = form.save(commit=False)

                user_profile =  UserProfile.objects.get(user=user)
                
                stadium.user = user_profile

                stadium.save()

                return index(request)
        
        else:
            print(form.errors)

    return render(request, "ATGApp/add_stadium.html", {"form": form})

def chosenStadium(request, stadium_name_slug):
    
    # if request.method == 'POST':
    # context_dict={chosen_stadium}
    context_dict = {}

    try:
        stadium = Stadium.objects.get(slug = stadium_name_slug)
        reviews = Review.objects.order_by('-date').filter(stadium = stadium)

        context_dict["reviews"] = reviews
        context_dict["stadium"] = stadium

    except Stadium.DoesNotExist:
        context_dict["stadium"] = None
        context_dict["reviews"] = None

    return render(request, 'ATGApp/chosenStadium.html', context=context_dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print('Invalid login details: {0}, {1}'.format(username, password))
            return render(request, 'ATGApp/invalid_login.html')
    else:
        return render(request, 'ATGApp/login.html', {})

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'ATGApp/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

def account(request):

    if request.user.is_authenticated():
        
        user = request.user
        user_profile = UserProfile.objects.get(user=user)
        reviews = Review.objects.order_by('-date').filter(user=user_profile)
        for review in reviews:
            print(review.stadium)
        # context_dict = {'reviews':reviews}
        
        stadiums = Stadium.objects.order_by('name').filter(user=user_profile)
        for stadium in stadiums:
            print(stadium.name)

        context_dict = {'stadiums':stadiums, 'reviews':reviews, 'user_profile':user_profile}

    else:
        context_dict = {}
    return render(request,'ATGApp/myAccount.html', context = context_dict)

def like_category(request):
    stad_id = None
    if  request.method == 'GET':
        stad_id = request.GET['stadium_id']
        likes = 0 
        if stad_id:
            stad = Stadium.objects.get(id=int(stad_id))
            if stad:
                likes = stad.likes + 1
                stad.likes = likes
                stad.save()
    return HttpResponse(likes)
	
	
@login_required
def del_acc(request):
	try:
		
		user = request.user
		logout(request)
		UserProfile.objects.get(user=user).delete()
		user.delete()
		print("Successfully deleted account.")
	except UserProfile.DoesNotExist:
		print("User does not exist.")
	return render(request, "ATGApp/index.html");

	

@login_required
def writeReview(request, stadium_name_slug):

    try:

        stadium = Stadium.objects.get(slug=stadium_name_slug)
    
    except Stadium.DoesNotExist:

        stadium = None

    form = ReviewForm()

    if request.method == "POST":

        form = ReviewForm(request.POST)

        if form.is_valid():

            if stadium:

                user = request.user

                review = form.save(commit=False)

                review.stadium = stadium

                user_profile = UserProfile.objects.get(user=user)

                review.user = user_profile

                print("stadium saved")

                review.save()

                return stadiums(request)
    else:

        print(form.errors)
    
    context_dict = {'form':form, 'stadium':stadium}

    return render(request, 'ATGApp/writeReview.html', context_dict)
    
    '''
    

    try:
        stadium = Stadium.objects.get(slug = stadium_name_slug)
        reviews = Review.objects.order_by('-date').filter(stadium = stadium)

        context_dict["reviews"] = reviews
        context_dict["stadium"] = stadium

    except Stadium.DoesNotExist:
        context_dict["stadium"] = None
        context_dict["reviews"] = None

 

    return render(request, 'ATGApp/chosenStadium.html', context=context_dict)

    '''
