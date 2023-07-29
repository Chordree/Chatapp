from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import openai
from django.contrib import auth 
from django.contrib.auth.models import User

api_key = 'sk-add your api key here'

openai.api_key = api_key
# Create your views here.

def base(request):
    # remove this view later on .. and import openAI
    return render(request, 'chattemps/base.html' )


# add alrdy have an accout log and regsiter anchor link
def query_ai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens = 100,
        n=1,
        stop=None,
        temperature=0.7  
    )
    # see to change val see what happens  
    reply = response.choices[0].text.strip()
    # see if this would also work as choices[0]['text']
    # see if the. method also works in dictionary
    
    return reply

def chat(request):
    if request.method == 'POST':
        messg = request.POST.get('message')
        resp =   'hey how are you doing'   #query_ai(messg)     # use the fuction and comment the test string
        return JsonResponse({'message':messg, 'response':resp})
    return render(request, 'chattemps/chatbot.html' )

def login(request):
    error_message = ''
    if request.method == 'POST':
        usernamee = request.POST['username']
        passwordd = request.POST['password']
        user = auth.authenticate(request, username=usernamee, password=passwordd)
        if user is not None:
            auth.login(request, user)
            return redirect('chatpage')
        error_message = 'invalid login details'
         
    return render(request, 'chattemps/login.html', {'error_message':error_message} )

def register(request):
    error_message = ''
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username, email, password1)
            user.save()
            auth.login(request, user)
            # add an except block here or a conditional incase user is not succesfully created 
            return redirect('chatpage')
            
        error_message = "passwords don't match"
    return render(request, 'chattemps/register.html', {'error_message': error_message})


# add logout view function
def logout(request):
    auth.logout(request)
    return redirect('chatpage')



#this was just to test the views 
def home(request):
    context = {'a' : 'yeah yeah yeah'}
    return render(request, 'chattemps/home.html', context)

    # return HttpResponse('welcome to the home page')  
    # # just used the above to test the view is working fine with httpresponse




# see to rename the subfolder of the Templates to name of app .. in case of class based views
# i.e chatapp instead of [chattemps or any other name]
