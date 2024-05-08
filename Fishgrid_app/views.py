from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.views.generic import TemplateView

from Fishgrid_app.models import Customer_Reg, UserType, shopRegistration


class IndexView(TemplateView):
    template_name = 'index.html'



class Customer_reg(TemplateView):
    template_name = 'cus_register.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['con_password']

        address=request.POST['address']
        if password == con_password:

            if User.objects.filter(email=email):
                print('pass')
                return render(request, 'cus_register.html', {'message': "already added the email"})

            else:
                user = User.objects._create_user(username=email, password=password, email=email, first_name=name,
                                                 is_staff='0', last_name='0')
                user.save()
                customer = Customer_Reg()
                customer.user = user
                customer.address=address
                customer.con_password=con_password
                customer.save()
                usertype = UserType()

                usertype.user = user
                usertype.type = "customer"
                usertype.save()
                return render(request, 'cus_register.html', {'message': "successfully added"})
        else:
            return render(request, 'cus_register.html', {'message': "password didn't match"})


class Login(TemplateView):
    template_name = 'login.html'
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)


        if user is not None:
            login(request, user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "customer":
                    return redirect('/customer')
                elif UserType.objects.get(user_id=user.id).type == "shop":
                    return redirect('/shop')
            # elif UserType.objects.get(user_id=user.id).type == "pharmacy":
            #     return redirect('/pharmacy')

            else:
                return render(request,'login.html',{'message':" User Account Not Authenticated"})


        else:
            return render(request, 'login.html', {'message': "Invalid Username or Password"})

class shopReg(TemplateView):
    template_name = 'shop_register.html'
    def post(self, request,*args,**kwargs):
        shopname = request.POST['shopname']
        address = request.POST['address']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        image = request.FILES['image']
        fi = FileSystemStorage()
        files = fi.save(image.name, image)
        password = request.POST['password']
        con_password = request.POST['con_password']


        if password == con_password:

            if User.objects.filter(email=email):
                print ('pass')
                return render(request,'shop_register.html',{'message':"already added the username or email"})

            else:
                user = User.objects._create_user(username=email,password=password,email=email,first_name=shopname,is_staff='0',last_name='0')
                user.save()
                shop = shopRegistration()
                shop.user = user
                shop.phonenumber = phonenumber
                shop.address=address
                shop.con_password=con_password
                shop.image = files


                shop.save()
                usertype = UserType()
                usertype.user = user
                usertype.type = "shop"
                usertype.save()


                return render(request, 'shop_register.html', {'message': "successfully added"})
        else:
            return render(request, 'shop_register.html', {'message': "password didn't match"})


class Forgot_Password(TemplateView):
    template_name = 'forgotpassword.html'

    def get_context_data(self, **kwargs):
        context = super(Forgot_Password, self).get_context_data(**kwargs)
        customer = Customer_Reg.objects.filter(user__last_name='1').count()
        shop = shopRegistration.objects.filter(user__last_name='1').count()
        admin = User.objects.get(is_superuser='1')
        context['customer'] = customer
        context['shop'] = shop
        context['admin'] = admin
        return context

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        print(email)
        user_id = self.request.user.id
        if User.objects.filter(last_name='1',email=email):
            user = User.objects.get(last_name='1',email=email)
            Type = UserType.objects.get(user_id=user.id)
            if Type.type == 'customer':
                customer = Customer_Reg.objects.get(user_id=user.id)
                Password = customer.con_password
                email = EmailMessage(
                    Password,
                    'Your password',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                )
                email.fail_silently = False
                email.send()
                return render(request, 'index.html', {'message': "Send mail successfully"})
            elif Type.type == 'shop':

                shop = shopRegistration.objects.get(user_id=user.id)
                print(shop)
                email = EmailMessage(
                    shop.con_password,
                    'Your password',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                )
                email.fail_silently = False
                email.send()
                return render(request, 'index.html', {'message': "Send mail successfully"})

        else:
            return render(request, 'index.html', {'message': "Tis User Is Not Exist"})




