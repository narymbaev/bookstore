from django.urls import path

from .views import BookList, BookDetail, SearchResultsListView

urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('<uuid:pk>/', BookDetail.as_view(), name='book_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]