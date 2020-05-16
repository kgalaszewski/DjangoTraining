from django.contrib import admin
from django.urls import path
from adoptions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('URL/param', 'view name / def name', '???')
    path('adoptions/pets/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('adoptions/pets/create/', views.create_pet_get, name='create_pet_get'),
    path('adoptions/pets/insert/<str:pet_name>/<str:pet_breed>/',
         views.create_pet_post, name='create_pet_post')
]
