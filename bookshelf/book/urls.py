from django.urls import path
from . import views, download, upload


app_name = "book"

urlpatterns = [
    path('upload/', upload.upload, name='upload'),
    path('download/<str:file_type>/', download.download, name='download'),
    path('book/', views.book_list, name='book_list'),  
]