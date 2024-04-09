# from django.urls import path
# from . import views
# urlpatterns = [
#     path('books/', views.book_list, name='book_list'),
# ]
# #bt2_c2
from django.urls import path
from .views import index, book_search
from . import views, api_views
from rest_framework.routers import DefaultRouter
from . import views, api_views
from django.urls import include
router = DefaultRouter()
router.register(r'books', api_views.BookViewSet)
router.register(r'reviews', api_views.ReviewViewSet)
urlpatterns = [
    path('books/', views.book_lists, name='book_lists'),
    path('books/<int:book_id>/', views.book_list, name='book_list'),
    path("book-search/", views.book_search, name='book_search'),
    path('books/<int:book_pk>/reviews/new/', views.review_edit, name='review_create'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/', views.review_edit, name='review_edit'),
    path('books/<int:pk>/media/', views.book_media, name='book_media'),
    path('api/', include((router.urls, 'api'))),
    path('api/login', api_views.Login.as_view(),name='login')

]


