from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View

from Fishgrid_app.models import shopRegistration, Customer_Reg, Compalaint, Cart


class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'

class Shop_Approvel(TemplateView):
    template_name = 'admin/shop_approve.html'

    def get_context_data(self, **kwargs):
        context = super(Shop_Approvel,self).get_context_data(**kwargs)

        shop = shopRegistration.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['shop'] = shop
        return context


class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})

class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})


class Customer_approvel(TemplateView):
    template_name = 'admin/customer_approve.html'

    def get_context_data(self, **kwargs):
        context = super(Customer_approvel,self).get_context_data(**kwargs)

        custr = Customer_Reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['custr'] = custr
        return context



class Shop_View(TemplateView):
    template_name = 'admin/view_shops.html'
    def get_context_data(self, **kwargs):
        context = super(Shop_View,self).get_context_data(**kwargs)

        view_shop = shopRegistration.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['view_shop'] = view_shop
        return context

class Customer_View(TemplateView):
    template_name = 'admin/view_customer.html'
    def get_context_data(self, **kwargs):
        context = super(Customer_View,self).get_context_data(**kwargs)

        view_cust = Customer_Reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['view_cust'] = view_cust
        return context




class Complaint_View(TemplateView):
    template_name = 'admin/view_complaint.html'

    def get_context_data(self, **kwargs):
        context = super(Complaint_View,self).get_context_data(**kwargs)

        compl = Compalaint.objects.filter(status='added')

        context['compl'] = compl
        return context

    def post(self, request, *args, **kwargs):
        # complaint = actions.objects.get(user_id=self.request.id)
        id = request.POST['id']
        action = request.POST['action']
        act = Compalaint.objects.get(id=id)
        # act.complaint=complaint
        act.action = action

        act.status = 'replied'
        act.save()

        return redirect(request.META['HTTP_REFERER'])


class BookingView(TemplateView):
    template_name = 'admin/view_booking.html'
    def get_context_data(self, **kwargs):
        context = super(BookingView,self).get_context_data(**kwargs)
        view_b = Cart.objects.all()

        context['view_b'] = view_b
        return context

