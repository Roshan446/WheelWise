"""
URL configuration for Bikeworld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from salesapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignupView.as_view(), name="signup"), 
    path("", views.SigninView.as_view(), name="signin"),
    path("home/",views.BikeHomeView.as_view(), name="home"),
    path("bike/sell/", views.BikeAddView.as_view(), name="bike-sell"),
    path("bike/list/", views.BikeListView.as_view(), name = "bike-list"),
    path("bike/messages/list/", views.NewMessageListView.as_view(), name = "message-list"),
    path("bike/<int:pk>/messages/",views.MessageView.as_view(), name="messages"),

    path("bike/<int:pk>/enquiry/", views.EnquiryView.as_view(), name = "enquiry"),
    path("bike/reply/list/", views.ReplyListview.as_view(), name="reply-list"),
    path("bike/<int:pk>/reply/", views.ReplyView.as_view(), name="reply"),
    path("bike/<int:pk>/detail/", views.DetailView.as_view(), name="bike-detail"),
    path("bike/<int:pk>/wishlist/add/", views.BikeWishlistItemsCreateView.as_view(), name = 'wishlist-add'),
    path("bike/wishlist/", views.WishlistListView.as_view(),name='wishlist-list'),
    path("bike/added/", views.AddedBikesView.as_view(), name='added-bike'),
    path("bikes/<int:pk>/update/", views.AddedBikesUpdateView.as_view(), name='bike-update'),
    path("bikes/<int:pk>/remove/", views.AddedBikesDeleteView.as_view(), name='bike-delete'),
    path("signout/", views.SignoutView.as_view(), name='signout'),
    path("feedback/", views.FeedbackView.as_view(), name ='feedback'),
    path("bike/<int:pk>/wishlist/remove/", views.WishListItemremoveView.as_view(), name="wishlist-remove")

    



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

