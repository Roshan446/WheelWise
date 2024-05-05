from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from salesapp.models import Bike, BikeBrand, City, State, User,Enquiry, WishListItems, WishList, Feedback
from salesapp.forms import RegistrationForm, SigninForm, BikeSellForm, FeedbackForm

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from salesapp.decorators import signin_required

from django.contrib import messages

# Create your views here.


deccor = [signin_required, never_cache]


class SignupView(View):
    
    def get(self, request, *args, **Kwargs):
        form = RegistrationForm()
        return render(request, "signup.html", {"form":form})
    
    def post(self, request, *args,**kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "you've successfully signed up")
            return redirect("signup")
        else:
            return render(request, "signup.html", {"form":form})
        
class SigninView(View):
    def get(self, request, *args, **kwargs):
        form  =  SigninForm()
        return render(request, "signup.html", {"data":form})
    def post(self, request, *args, **kwargs):
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user_auth = authenticate(username=username, password=password)
            if user_auth:
                login(request, user_auth)
                print(request.user)
                return redirect("home")
            
            else:
                return render(request, "signup.html", {"data":form})

@method_decorator(deccor, name="dispatch")
class BikeHomeView(View):
    def get(self, request, *args, **kwargs):
        brand_object = BikeBrand.objects.all()
        return render(request, "index.html", {"data":brand_object})

@method_decorator(deccor, name="dispatch")
class BikeListView(View):
    def get(self, request, *args, **kwargs):
        brand = BikeBrand.objects.all()
        city_object = City.objects.all()
        state_object = State.objects.all()
        bike_object = Bike.objects.all()
        category = Bike.objects.values_list("category", flat=True).distinct()
        selected_brand = request.GET.get("brand")
        selected_cat = request.GET.get("category")
        selected_location = request.GET.get("location")
        selected_date = request.GET.get("date")
        w_qs =WishList.objects.get(user_object =request.user)

        selected_order = request.GET.get("list")
        if selected_order == "LATEST":
            bike_object =bike_object.order_by('-created_date')
        elif selected_order == 'oldest':
            bike_object=bike_object.order_by('created_date')
        

        print(request.GET)
        if selected_brand:
            bike_object = bike_object.filter(brand_object__name = selected_brand)
            print(request.GET)
        if selected_cat:
            bike_object = bike_object.filter(category = selected_cat)
        if selected_location:
            bike_object = bike_object.filter(city_object__name = selected_location)
        
        return render(request, "bike_list.html", {"brand":brand, "city":city_object, "bike":bike_object, "cat":category})
    
    
    def post(self, request, *args, **kwargs):
        city = request.POST.get("city")
        city_object = City.objects.all()
        brand = BikeBrand.objects.all()
        state_object = State.objects.all()
        bike_object = Bike.objects.all()
        category = Bike.objects.values_list("category", flat=True).distinct()
        selected_brand = request.POST.get("brand")
        selected_cat = request.POST.get("category")
        selected_location = request.POST.get("location")
        selected_date = request.POST.get("date")
        if city:
            bike_object = Bike.objects.filter(city_object__name = city) 
        return render(request, "bike_list.html", {"brand":brand, "city":city_object, "bike":bike_object, "cat":category})


        
@method_decorator(deccor, name="dispatch")
class BikeAddView(View):
    def get(self, request, *args, **kwargs):
        bike_form = BikeSellForm()
        brand = BikeBrand.objects.all()
        city_object = City.objects.all()
        state_object = State.objects.all()
        return render(request, "sell.html", {"form":bike_form, "brand":brand, "city":city_object, "state":state_object})
    
    def post(self, request, *args, **kwargs):
        bike_form = BikeSellForm(request.POST, request.FILES)
        print(request.POST)
        brand = BikeBrand.objects.all()
        city_object = City.objects.all()
        print(bike_form.errors)
        if bike_form.is_valid():
            Bike.objects.create(**bike_form.cleaned_data, user_object =request.user)
            
            return redirect("bike-sell")
        else:
            return render(request, "sell.html", {"form":bike_form, "brand":brand, "city":city_object})



    
@method_decorator(deccor, name="dispatch")
class NewMessageListView(View):
    def get(self, request, *args, **kwargs):
        qs = Enquiry.objects.filter( is_read = False, user_object = request.user, is_replied = True)
        qs = qs.order_by("-created_date")
        return render(request, "message_list.html",{"data":qs})

@method_decorator(deccor, name="dispatch")
class MessageView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        enquiry_object = Enquiry.objects.get(id =id)
        is_read = request.GET.get("is_read")
        print(is_read)
        if is_read == "true":
            enquiry_object.is_read = True
            enquiry_object.save()
        
        qs = Enquiry.objects.filter(user_object = request.user, bike_object = enquiry_object.bike_object)
      

        return render(request, "messages.html", {"enquiry":enquiry_object, "enquiries":qs})
    
    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        enquiry_object  = Enquiry.objects.get(id=id)
        if enquiry_object.user_object == request.user:
            user_object = request.user 
            message = request.POST.get("message")
            Enquiry.objects.create(bike_object =enquiry_object.bike_object, 
                               user_object=user_object,
                               message = message

                               )
        else:
            user_object = enquiry_object.bike_object.user_object
            message = request.POST.get("message")
            Enquiry.objects.create(bike_object =enquiry_object.bike_object, 
                               user_object=user_object,
                               reply = message

                               )
            
        return redirect("message-list")
        
    
@method_decorator(deccor, name="dispatch")
class EnquiryView(View):
    def get(self, request, *args, **kwargs):
        id =kwargs.get("pk")
        qs =Bike.objects.get(id=id)
        e_qs = Enquiry.objects.filter(bike_object = qs, user_object = request.user)
        return render(request, 'enquiry.html',{"bike":qs, "enquiries":e_qs})
    
    def post(self, request, *args,**kwargs):
        id = kwargs.get("pk")
        bike_object  = Bike.objects.get(id=id)
        user_object = request.user
        message = request.POST.get("message")
        Enquiry.objects.create(bike_object =bike_object, 
                               user_object=user_object,
                               message = message

                               )
            
        
        return redirect("bike-list")
    
@method_decorator(deccor, name="dispatch")
class ReplyListview(View):
    def get(self, request, *args, **kwargs):
        r_qs = Enquiry.objects.filter(bike_object__user_object = request.user, is_replied = False).order_by("-created_date") #this is to order from the newest created date
        return render(request, "reply_list.html", {"data":r_qs})

@method_decorator(deccor, name="dispatch")  
class ReplyView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        enquiry_object = Enquiry.objects.get(id=id)

    
        qs = Enquiry.objects.filter(user_object = enquiry_object.user_object, bike_object = enquiry_object.bike_object)
        
        return render(request, "reply.html", {"enquiry":qs, "data":enquiry_object })
    
    def post(self, request, *args, **kwargs):
        reply = request.POST.get("reply")
        id = kwargs.get("pk")
        
        enquiry_object = Enquiry.objects.get(id=id)
        qs = Enquiry.objects.filter(user_object = enquiry_object.user_object, bike_object = enquiry_object.bike_object)
        if reply:
            enquiry_object.reply = reply
            enquiry_object.save()
        if enquiry_object.reply:
            for r in qs:
                r.is_replied = True
                r.save()
            
        return redirect("reply-list")
    
@method_decorator(deccor, name="dispatch")
class DetailView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        bike_obj = Bike.objects.get(id=id)
        return render(request, 'bike_detail.html', {"bike":bike_obj})

@method_decorator(deccor, name="dispatch")    
class BikeWishlistItemsCreateView(View):
    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        bike_object = Bike.objects.get(id=id)
        wishlist_object = WishList.objects.get(user_object = request.user)
        qs = request.user.saved.saveditem.filter(bike_object=bike_object)
        if qs:    
            return redirect("bike-list")
        else:
            print(wishlist_object)
            WishListItems.objects.create(bike_object =bike_object, wishlist_object =wishlist_object)
            return redirect('wishlist-list')
            
@method_decorator(deccor, name="dispatch")
class WishlistListView(View):
    def get(self, request, *args, **kwargs):
        wishlist_object = WishList.objects.get(user_object = request.user)
        print(wishlist_object.wish_items_count)

        qs = WishListItems.objects.filter(wishlist_object = wishlist_object)
        return render(request, 'wishlist_list.html', {"items":qs})

@method_decorator(deccor, name="dispatch")
class WishListItemremoveView(View):
    def get(self, request, *args, **kwargs):
        id =kwargs.get("pk")
        
        WishListItems.objects.get(id=id).delete()
        return redirect("wishlist-list")

        
@method_decorator(deccor, name="dispatch")
class AddedBikesView(View):
    def get(self, request, *args, **kwargs):
        qs =Bike.objects.filter(user_object = request.user)
        selected_sort = request.GET.get("sortby")
        if selected_sort=="newest":
            qs=qs.order_by("-created_date")
        else:
            qs =qs.order_by("created_date")
        return render(request, 'added_bikes.html',{"bike":qs})

@method_decorator(deccor, name="dispatch")    
class AddedBikesUpdateView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        bike_object = Bike.objects.get(id = id)
        form = BikeSellForm(instance=bike_object)
        brand = BikeBrand.objects.all()
        city_object = City.objects.all()
        state_object = State.objects.all()
        return render(request, 'update_bike.html', {"bike":bike_object,"form": form, "brand":brand, "city":city_object, "state":state_object})
    
    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        bike_object = Bike.objects.get(id = id)
        form = BikeSellForm(request.POST,request.FILES,instance=bike_object)
        if form.is_valid():
            form.save()
            return redirect("added-bike")
        else:
            return render(request, 'sell.html', {"form":form})

@method_decorator(deccor, name="dispatch")
class AddedBikesDeleteView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs =Bike.objects.get(id=id)
        qs = qs.delete()
        return redirect("added-bike")


class SignoutView(View):
    def get(self, request, *args, **kwargs):
        
        logout(request)
        messages.success(request,"you've successfully logged out")
        return redirect('signin')

class FeedbackView(View):
    # def get(self, request, *args, **kwargs):
    #     form = FeedbackForm()
    #     return render(request, "index.html", {"form":form})
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(user_object = request.user)
            messages.success(request, "Thank you for your feedback")
        return redirect("home")




        
