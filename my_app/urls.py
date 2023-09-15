from my_app.views import index, about, general, special_subjects, optional_subjects
from django.urls import path

urlpatterns = [
    path('',index, name='index'),
    path('about/', about , name='about'),
    path('general/', general , name='general'),
    path('special_subjects/', special_subjects , name='special_subjects'),
    path('optional_subjects/', optional_subjects , name='optional_subjects')
]