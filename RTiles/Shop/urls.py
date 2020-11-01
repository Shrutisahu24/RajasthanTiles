
from django.urls import path, include
from . import views




urlpatterns = [
    path('' , views.Home, name= "home"),
    path('tiles' , views.Tiles, name= "tiles"),
    path('aboutUs' , views.aboutus, name= "aboutus"),
    path('order' , views.YourOrder, name= "order"),
    path('TilesDetails/<int:my_id>/' , views.TilesDetails, name= "TilesDetails"),
    path('myorder' , views.MyOrder, name= "myorder"),
    path('tilestypes' , views.Home, name= "tilestypes"),
    path('tilestypes1/<str:typetile>/' , views.tiles_type, name= "tilestypes1"),
    path('deleteorder/<int:my_id>' , views.userdeleteform, name= "userdeleteform"),

]