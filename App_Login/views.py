from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.conf import settings
from django.core.mail import send_mail

from App_Login.models import *


from django.contrib import messages
import razorpay
import uuid

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import random


def register_individual(request):

    if request.method == 'POST':
        rotaractor_or_interactor_or_rotarian = request.POST.get('rotaractor_or_interactor_or_rotarian')
        name = request.POST.get('name')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email_id')
        club_name = request.POST.get('club_name')
        club_rotary_id = request.POST.get('club_rotary_id')
        gender = request.POST.get('gender')
        blood_group = request.POST.get('blood_group')
        address = request.POST.get('address')
        emergency_contact_name = request.POST.get('emergency_contact_name')
        emergency_contact_no = request.POST.get('emergency_contact_no')
        jacket_size = request.POST.get('jacket_size')
        participate_in_ryla = request.POST.get('participate_in_ryla')
        theme_interest = request.POST.get('theme_interest')
        username = request.POST.get('username')
        password = request.POST.get('password')
        house_list = ['Alpha', 'Beta', 'Gama', 'Delta']
        house_alloted = random.choice(house_list)
        
        print(rotaractor_or_interactor_or_rotarian)
        print(name)
        print(contact_no)
        print(email)
        print(club_name)
        print(club_rotary_id)
        print(gender)
        print(blood_group)
        print(address)
        print(emergency_contact_name)
        print(emergency_contact_no)
        print(jacket_size)
        print(participate_in_ryla)
        print(theme_interest)
        print(house_alloted)
        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return HttpResponseRedirect(reverse('App_Login:register_individual'))

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return HttpResponseRedirect(reverse('App_Login:register_individual'))


            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            individual_obj = Individual.objects.create(user = user_obj , auth_token = auth_token, rotaractor_or_interactor_or_rotarian=rotaractor_or_interactor_or_rotarian, name = name,contact_no=contact_no, email_id=email, club_name=club_name, club_rotary_id=club_rotary_id, gender=gender, blood_group=blood_group,address=address,emergency_contact_name=emergency_contact_name, emergency_contact_no=emergency_contact_no, jacket_size=jacket_size, participate_in_ryla=participate_in_ryla, theme_interest=theme_interest, house_alloted = house_alloted)
            individual_obj.save()
            messages.success(request, 'Registered Sucessfully')
            # html_template = render_to_string('register_email.html', {'name':name, 'username':username,'password':password})
            # recipient_list = [email]
            # message = EmailMessage('Welcome To SAVTHEARTH', html_template,
            #                        'SAVTHEARTH <info@savthearth.org>', [email])
            # message.content_subtype = 'html'
            # message.send()
            

            return HttpResponseRedirect(reverse('App_Login:login_attempt'))


        except Exception as e:
            print(e)


    return render(request , 'App_Login/register_individual.html')


def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return HttpResponseRedirect(reverse('App_Login:login_attempt'))


        # profile_obj = Profile.objects.filter(user = user_obj ).first()
        #
        # if not profile_obj.is_verified:
        #     messages.success(request, 'Profile is not verified check your mail.')
        #     return HttpResponseRedirect(reverse('App_Login:login_attempt'))

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return HttpResponseRedirect(reverse('App_Login:login_attempt'))

        login(request , user)
        return HttpResponseRedirect(reverse('user_profile'))

    return render(request , 'App_Login/login.html')



@login_required
def logout_user(request):
    logout(request)
    messages.warning(request,"You Are Logged Out!")
    return HttpResponseRedirect(reverse('home'))


def register_club(request):

    if request.method == 'POST' and request.FILES['payment_screenshot']:
        rotaractor_or_interactor_or_rotarian = request.POST.get('rotaractor_or_interactor_or_rotarian')
        name = request.POST.get('name')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email_id')
        rotary_club_name = request.POST.get('rotary_club_name')
        interactor_club_name = request.POST.get('interactor_club_name')
        rotaractor_club_name = request.POST.get('rotaractor_club_name')
        club_rotary_id = request.POST.get('club_rotary_id')
        rotary_id = request.POST.get('rotary_id')
        club_email_id = request.POST.get('club_email_id')
        parent_club_name = request.POST.get('parent_club_name')
        presidents_name = request.POST.get('presidents_name')
        presidents_contact_no = request.POST.get('presidents_contact_no')
        secretary_name = request.POST.get('secretary_name')
        secretary_contact_no = request.POST.get('secretary_contact_no')
        gender = request.POST.get('gender')
        blood_group = request.POST.get('blood_group')
        address = request.POST.get('address')
        emergency_contact_name = request.POST.get('emergency_contact_name')
        emergency_contact_no = request.POST.get('emergency_contact_no')
        jacket_size = request.POST.get('jacket_size')
        no_of_participants = request.POST.get('no_of_participants')
        payment_screenshot = request.FILES.get('payment_screenshot')
        print(rotaractor_or_interactor_or_rotarian)
        print(name)
        print(contact_no)
        print(email)
        print(rotary_club_name)
        print(interactor_club_name)
        print(rotaractor_club_name)
        print(club_rotary_id)
        print(rotary_id)
        print(club_email_id)
        print(parent_club_name)
        print(presidents_name)
        print(presidents_contact_no)
        print(secretary_name)
        print(secretary_contact_no)
        print(gender)
        print(blood_group)
        print(address)
        print(emergency_contact_name)
        print(emergency_contact_no)
        print(jacket_size)
        print(no_of_participants)
        print(payment_screenshot)

        
        
 
        try:

            auth_token = str(uuid.uuid4())
            club_obj = Club.objects.create(auth_token = auth_token, rotaractor_or_interactor_or_rotarian=rotaractor_or_interactor_or_rotarian, name = name,contact_no=contact_no, email_id=email, rotary_club_name=rotary_club_name, interactor_club_name=interactor_club_name,rotaractor_club_name=rotaractor_club_name,club_rotary_id=club_rotary_id, rotary_id=rotary_id,club_email_id=club_email_id,parent_club_name=parent_club_name, presidents_name=presidents_name,presidents_contact_no=presidents_contact_no,secretary_name=secretary_name,secretary_contact_no=secretary_contact_no, gender=gender, blood_group=blood_group,address=address,emergency_contact_name=emergency_contact_name, emergency_contact_no=emergency_contact_no, jacket_size=jacket_size, no_of_participants=no_of_participants, payment_screenshot=payment_screenshot)
            club_obj.save()
            messages.success(request, 'Registered Sucessfully')
            # html_template = render_to_string('register_email.html', {'name':name, 'username':username,'password':password})
            # recipient_list = [email]
            # message = EmailMessage('Welcome To SAVTHEARTH', html_template,
            #                        'SAVTHEARTH <info@savthearth.org>', [email])
            # message.content_subtype = 'html'
            # message.send()
            

            return HttpResponseRedirect(reverse('home'))


        except Exception as e:
            print(e)


    return render(request , 'App_Login/register_club.html')

      





