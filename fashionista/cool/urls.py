from django.conf.urls import url
from  . import views


app_name = 'cool'
urlpatterns = [
    # / cool app root directory
    url(r'^$', views.index, name= 'index'),

    # / cool app root directory
    url(r'^yo/$', views.yo, name= 'yo'),

    # /cool/register/
    url(r'register/$', views.AccountsCreate.as_view(), name= 'register'),

    # /cool/login/
    url(r'login/$', views.UserFormView.as_view(), name= 'login'),

    # /cool/logout/
    url(r'logout/$', views.logout_user, name='logout'),

    # /cool/mypage/2
    url(r'mypage/(?P<user_id>[0-9]+)/$', views.mypage, name= 'mypage'),



    #    /cool/mypage/2
    url(r'voting/$', views.voting, name= 'voting'),

    # /cool/mypage/2
    url(r'profile/$', views.profile, name= 'profile'),



]
