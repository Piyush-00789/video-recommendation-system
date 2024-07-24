from django.views import generic
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate,login
from .forms import UserForm
from  django.views.generic import View
from .models import Usersdetails,Usertaste
from django.contrib.sessions import base_session
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .apps import VideoConfig

class Indexview(generic.ListView):
    template_name = "video/index.html"
    context_object_name = "all_records"

    def get_queryset(self):
        return 0

class UserDetailsCreate(CreateView):
    template_name = "video/usersdetails_form.html"
    model = Usersdetails
    fields = ['firstname','lastname','email','password']


class CreateUserTaste(CreateView):
    model = Usertaste
    template_name = "video/userchoices_form.html"
    fields = ['emailid','taste']





class UserFormView(View):
    form_class = UserForm
    template_name = "video/usersdetails_form.html"
    #display blank form

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #process form data

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():


            usersdetails = form.save(commit=False)


            #clean normalized(data)

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            #request.session['email'] = email

            print("fghgfhgfh")
            #usersdetails.set_password(password)
            usersdetails.save()
            print("fghgfhgf")
            #returns user objects if credentials are correct

            usersdetails = authenticate(email=email,password=password)
            return redirect('video:user-taste')

            if usersdetails is not None:
                print("first")

                if usersdetails.is_active:
                    print("sec")

                    login(request,usersdetails)
                    print("third")
                    return redirect('video:index')


        print("fourth")


        return render(request,self.template_name,{'form':form})






class useravailable(generic.DetailView):
    model = Usersdetails






def signin(request):
    if request.method =="GET":
        print("GET")
    elif request.method =="POST":
        print("POST")
    return render(request,"video/signin_form.html")

def logincheck(request):
    context_object_name = "hoyeeee"
    if request.method =="GET":
        print("GET")
    elif request.method =="POST":
        print("POST")
        call_model = Usersdetails.objects.all()
        email = request.POST.get('email')
        if call_model == email:
            print("Confirmed")
        else:
            print("NOT")
        print(email)

def signup(request):
    return render(request, "video/usersdetails_form.html")

class call_model(APIView):

    def get(self, request):
        if request.method == 'GET':

            # sentence is the query we want to get the prediction for
            params = request.GET.get('sentence')
            #confirmed case 1
            # predict method used to get the prediction
            print("paaaaaaa")
            response = VideoConfig.make_recommendations(params)
            ###
            print("saaaaaa")
            print(response)
            print(type(response))
            # returning JSON response
            return JsonResponse(response,safe=False)









