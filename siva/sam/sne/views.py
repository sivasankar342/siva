from django.shortcuts import render
from django.contrib.auth.models import User, auth



# Create your views here.
def register(request):  
        if request.method== 'POST':
            firstname = request.POST['firstname']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirmpassword = request.POST['confirmpassword']

            User = User.object.create_user(username=username, email=email, password=password, firstname=firstname)
            User.save()
            print('user created')
        else:
            return render(request, 'signup.html')