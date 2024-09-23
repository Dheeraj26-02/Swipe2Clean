from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
urlpatterns = [
    # path('',views.login1),
    path('',views.index,name="index"),
    # path('saveEnquiry/',views.saveEnquiry,name="saveEnquiry"),
    path('login1/',views.login1,name="login1"),
    path("register", views.register, name="register"),
    # path('community/',views.community,name="community"),
    path('Business/',views.Business,name="Business"),
    path('BusinessPage/',views.BusinessPage,name="BusinessPage"),
    path('Event/',views.Event,name="Event"),
    path('Profile/',views.Profile,name="Profile"),
    path('leaderboard/',views.leaderboard,name="leaderboard"),
    path('Wallet/',views.Wallet,name="Wallet"),
    path('Complain/',views.Complain,name="Complain"),
    path('dashboard/',views.dashboard,name="dashboard"),
    # path('Signup/',views.Signup,name="Signup"),
    path('Invalid/',views.Invalid,name="Invalid"),
    path('logout/',views.logout,name="logout"),
    path('YourPost/',views.YourPost,name="YourPost"),
    path('CreatePost/',views.CreatePost,name="CreatePost"),
    path('Certificate/',views.Certificate,name="Certificate")
    # path('PopUp/',views.PopUp,name="PopUp"),
    # path('',include((home,urls)))

 ]#+static(settings.MEDIA_URL,documnet_root=settings.MEDIA_ROOT)
    

# if settings.DEBUG:
#     urlpatterns +=static(settings.MEDIA_URL,documnet_root=settings.MEDIA_ROOT)
    