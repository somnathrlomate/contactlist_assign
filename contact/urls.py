from django.urls import path
from contact import views

urlpatterns = [
    path('contact/',
    	views.contact_list,
    	name = 'contact-list'),
    path('contact/<int:pk>/',
    	views.contact_list_detail,
    	name='contact-detail'),
    path('task/',
		views.user_list,
		name = 'user-list'),
	path('task/<int:pk>/',
		views.user_detail,
		name='user-detail'),
            ]