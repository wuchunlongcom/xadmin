from django.urls import path,include,re_path
from .views import SchoolItemsView

from . import views

app_name = 'app'

urlpatterns = [
    # 学校信息
    #path('school/items/', SchoolItemsView.as_view(),name='school_items'),
    path("school/items/", views.SchoolItemsView,name='school_items'),
]
