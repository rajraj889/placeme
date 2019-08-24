from django.conf.urls import url, include
from django.contrib import admin
#from django.contrib.auth import views
from . import views
from django.urls import path,include
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.log, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    url(r'^$', views.home, name='home'),
    #url(r'^$placement/',views.PostList.as_view(),name='placement'),
    path('placement/', views.PostList.as_view(), name='placement'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add_company',views.add_company,name='add_company'),
    path('company_add',views.view_company.as_view(),name='company_add'),
    path('add_exp',views.add_exp,name='add_exp'),
    path('login/',views.login,name='login'),
    path('add_study',views.study_e,name='add_study'),
    path('study',views.stuy.as_view(),name='study'),
    path('<slug:p>/<slug:slug>/', views.studydetail.as_view(), name='study_d'),
    
]
