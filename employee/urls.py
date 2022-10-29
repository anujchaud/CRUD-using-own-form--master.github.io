import imp
from django.urls import path

from .views import *

urlpatterns = [
    
    path('',show_view),
    path('add/',add_view),
    path('update/<int:eid>/',update_view),
    path('delete/<int:eid>/',delete_view),
    path('view/<int:eid>/',view_employee)
]
