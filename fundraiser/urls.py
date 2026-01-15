"""
fundraiser URL Configuration
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from userapp import views as user_views
from adminapp import views as admin_views


urlpatterns = [

    # =========================
    # CUSTOM ADMIN PAGES (FIRST)
    # =========================
    path('view-adminlogin', admin_views.adminlogin, name='admin_login'),
    path('admindashboard', admin_views.adminhome, name='admin_home'),
    path('view-fundraisers', admin_views.raiser, name='view_fundraisers'),
    path('view-funds', admin_views.funds, name='view_funds'),
    path('view_fundraiser_profile/<int:id>/', admin_views.fundraiserprofile, name='view_fundraiser_profile'),
    path('fundraiserprofile_accept/<int:id>/', admin_views.fundraiserprofileaccept, name='fundraiserprofile_accept'),
    path('fundraiserprofile_reject/<int:id>/', admin_views.fundraiserprofilereject, name='fundraiserprofile_reject'),
    path('view-feedbacks', admin_views.feedbacks, name='view_feedbacks'),

    # =========================
    # USER PAGES
    # =========================
    path('', user_views.home2, name='home2'),
    path('about', user_views.about, name='about'),
    path('login', user_views.login, name='login'),
    path('signup', user_views.signup, name='signup'),
    path('contact', user_views.contact, name='contact'),
    path('livehood', user_views.livehood, name='livehood'),
    path('userprofile', user_views.userprofile, name='userprofile'),
    path('userdashboard', user_views.userdashboard, name='userdashboard'),
    path('userfeedback', user_views.userfeedback, name='userfeedback'),
    path('userfund', user_views.userfund, name='userfund'),
    path('health', user_views.health, name='health'),
    path('education', user_views.education, name='education'),
    path('donate', user_views.donate, name='donate'),
    path('donateaction2', user_views.donateaction, name='donateaction2'),
    path('donateaction/<int:id>', user_views.donateaction, name='donateaction'),
    path('fundrasing', user_views.fundrasing, name='fundrasing'),
    path('blockchain-verify/<int:id>', user_views.verify_blockchain, name='blockchain_verify'),

    # =========================
    # DJANGO DEFAULT ADMIN (LAST)
    # =========================
    path('admin/', admin.site.urls),
]

# =========================
# MEDIA FILES
# =========================
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
