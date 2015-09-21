from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.contrib.auth.models import User
from mysite.models import UserProfile, UserUpdate, SelectCountry
from mysite.forms import UserForm, UserProfileForm, UserUpdateForm, SelectCountryForm
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.conf.urls import patterns, include, url

#for redirecting to user profile page after logging in
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

#for sending emails
from django.core.mail import send_mail

def mainpage(request):
    return HttpResponse("This is the main page.  <a href='http://127.0.0.1:8000/profile/'>Your profile</a>. <a href = 'http://127.0.0.1:8000/login/'>Log In </a> <a href = 'http://127.0.0.1:8000/register/'> Register </a>")
    #return HttpResponse("Hello.  This is the main page.")

#Fake User
def bob(request):
    bob = {'name': 'Bob', 'password': '1111', 'age': '43', 'about': 'I am from the USA, and I love candy.'}
    t = Template('Name: {{ bob.name }}  \n Age: {{ bob.age }}  About me: {{bob.about}}')
    c = Context({'bob': bob})
    t.render(c)
    return HttpResponse(t.render(c) + " <a href = 'http://127.0.0.1:8000/main/'>Return to Main Page</a>")


@login_required
def profpage(request):
    profile, created = UserProfile.objects.get_or_create(user = request.user)
    username = request.user.username
    first_name = request.user.first_name
    last_name = request.user.last_name
    street = profile.street_address
    city = profile.city
    state = profile.state
    country = profile.country
    about = profile.about


    
    countries_requested_list =[]
    for i in range(len(profile.countries_requested_list)):
        countries_requested_list.append(str(profile.countries_requested_list[i]))

    t = Template('Username: ' + username + ' ' + first_name + ' ' + last_name + '\n Street Address: ' + street + ' ' + city + ', ' + state + '.  ' + country + '  About me:  ' + about + " Countries requested:  ")
    c = Context({'request.user': request.user})
    t.render(c)

    if len(countries_requested_list) == 0:
        return HttpResponse("Profile page:  " + t.render(c) + " " +
        "<a href = 'http://127.0.0.1:8000/main/'>Return to Main Page</a>  \
        <a href = 'http://127.0.0.1:8000/profile/edit/'>Edit Profile</a> \
        <a href = 'http://127.0.0.1:8000/findmatch/'>Find a match! </a> ")

    elif len(countries_requested_list) == 1:
        country1 = countries_requested_list[0]
        return HttpResponse("Profile page:  " + t.render(c) +  country1 +" " +
            "<a href = 'http://127.0.0.1:8000/main/'>Return to Main Page</a>  \
            <a href = 'http://127.0.0.1:8000/profile/edit/'>Edit Profile</a> \
            <a href = 'http://127.0.0.1:8000/findmatch/'>Find a match! </a> ")

    elif len(countries_requested_list) == 2:
        country1 = countries_requested_list[0]
        country2 = countries_requested_list[1]
        return HttpResponse("Profile page:  " + t.render(c) +  country1 + ", " + country2 +" " +
            "<a href = 'http://127.0.0.1:8000/main/'>Return to Main Page</a>  \
            <a href = 'http://127.0.0.1:8000/profile/edit/'>Edit Profile</a> \
            <a href = 'http://127.0.0.1:8000/findmatch/'>Find a match! </a> ")

    elif len(countries_requested_list) == 3:
        country1 = countries_requested_list[0]
        country2 = countries_requested_list[1]
        country3 = countries_requested_list[2]
        return HttpResponse("Profile page:  " + t.render(c) +  country1 + ", " + country2 + ", " + country3 +" " +
            "<a href = 'http://127.0.0.1:8000/main/'>Return to Main Page</a>  \
            <a href = 'http://127.0.0.1:8000/profile/edit/'>Edit Profile</a> \
            <a href = 'http://127.0.0.1:8000/findmatch/'>Find a match! </a> ")

    elif len(countries_requested_list) == 4:
        country1 = countries_requested_list[0]
        country2 = countries_requested_list[1]
        country3 = countries_requested_list[2]
        country4 = countries_requested_list[3]
        return HttpResponse("Profile page:  " + t.render(c) +  country1 + ", " + country2 + ", " + country3 + ", " + country4 +" " +
            "<a href = 'http://127.0.0.1:8000/main/'>Return to Main Page</a>  \
            <a href = 'http://127.0.0.1:8000/profile/edit/'>Edit Profile</a> \
            <a href = 'http://127.0.0.1:8000/findmatch/'>Find a match! </a> ")

    elif len(countries_requested_list) == 5:
        country1 = countries_requested_list[0]
        country2 = countries_requested_list[1]
        country3 = countries_requested_list[2]
        country4 = countries_requested_list[3]
        country5 = countries_requested_list[4]
        return HttpResponse("Profile page:  " + t.render(c) +  country1 + ", " + country2 + ", " + country3 + ", " + country4 + ", " + country5 + " " +
            "<a href = 'http://127.0.0.1:8000/main/'>Return to Main Page</a>  \
            <a href = 'http://127.0.0.1:8000/profile/edit/'>Edit Profile</a> \
            <a href = 'http://127.0.0.1:8000/findmatch/'>Find a match! </a> ")
    else:
        return HttpResponse("Sorry, you're limited to choosing 5 countries at a time.")




def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        # attempt to grab information from the raw form information
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return redirect('/login/')
        else:
            print user_form.errors

    else:
        user_form = UserForm()

    # render the template depending on the context
    return render_to_response(
            'register.html',
            {'user_form': user_form, 'registered': registered},
            context)

import sys
from django.conf import settings

def reload_urlconf(urlconf=None):
    if urlconf is None:
        urlconf = settings.ROOT_uURLCONF
    if urlconf in sys.modules:
        reload(sys.modules[urlconf])



@login_required
def edit_profile(request):
    user_form = UserUpdateForm()
    profile_form = UserProfileForm()
    context = RequestContext(request)
    new_profile_user = None


    if '_auth_user_id' in request.session:
        userId = request.session['_auth_user_id']
        new_profile_user = UserProfile.objects.get(user_id=userId)
        userDetails = User.objects.get(pk=userId)

        if request.method == 'POST':
            
            if request.POST.get('email', '') != '':
                userDetails.email = request.POST.get('email', '')
            if request.POST.get('first_name', '') != '':
                userDetails.first_name = request.POST.get('first_name', '')
            if request.POST.get('last_name', '') != '':
                userDetails.last_name = request.POST.get('last_name', '')
            userDetails.save()


            if request.POST.get('street_address', '') != '':
                new_profile_user.street_address = request.POST.get('street_address', '')

            if request.POST.get('city', '') != '':
                new_profile_user.city = request.POST.get('city', '')

            if request.POST.get('state', '') != '':
                new_profile_user.state = request.POST.get('state', '')

            if request.POST.get('country', '') != '':
                new_profile_user.country = request.POST.get('country', '')

            if request.POST.get('zipcode', '') != '':
                new_profile_user.zipcode = request.POST.get('zipcode', '')

            if request.POST.get('country_requested', '') != '':
                if len(new_profile_user.countries_requested_list) < 5:
                    new_profile_user.countries_requested_list.append(request.POST.get('country_requested', ''))
                else:
                    return HttpResponse("You're limited to 5 countries at a time.  Remove a country from your list.")

            if request.POST.get('about', '') != '':
                new_profile_user.about = request.POST.get('about', '')
            
            new_profile_user.save()

            if request.POST.get('new_password', '') != '' and request.POST.get('new_password', '') == request.POST.get('confirm_password', ''):
                userDetails.set_password(request.POST.get('new_password', ''))
                userDetails.save()
                return redirect('/login/')
            
            return redirect('/profile/')

        else:
            user_form = UserUpdateForm()
            profile_form = UserProfileForm()
    
    return render_to_response('edit_profile.html', {'user_form': user_form, 'profile_form': profile_form, 'new_profile_user': new_profile_user}, context)


@login_required
def find_match(request):
    country_form = SelectCountryForm()
    context = RequestContext(request)
    tooManyCountries = False
    if '_auth_user_id' in request.session:
        userId = request.session['_auth_user_id']
        new_profile_user = UserProfile.objects.get(user_id=userId)
        

        if request.method == 'POST':
            if request.POST.get('add_country', '') != '':
                if len(new_profile_user.countries_requested_list) < 5:
                    new_profile_user.countries_requested_list.append(request.POST.get('add_country', ''))
                    new_profile_user.save()
                    
                else:
                    tooManyCountries = True
                    #return HttpResponse("You're limited to 5 countries at a time.  Remove a country from your list.")
                    
                return redirect('/profile/')

    return render_to_response('request_match.html', {'tooManyCountries': tooManyCountries, 'country_form': country_form, 'new_profile_user': new_profile_user}, context)






