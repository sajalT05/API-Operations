from django.contrib import admin
from django.urls import path

# django rest framework
# api documentation
from rest_framework.documentation import include_docs_urls

# import files
from . import views

# add url paths here -->
urlpatterns = [
#	path('pathName', views.viewsFunctionName, name="pageName" ),
    # homepage
    path('', views.api_overview, name='api_overview'),

    # # api documentation --> swagger
    # path(r'docs/', include_docs_urls(title='API Docs')),

    # API
    # GET
    # view all 
    # authors
    path('all-authors/', views.all_authors, name='all_authors'),
    # categories
    path('all-categories/', views.all_categories, name='all_categories'),
    # books
    path('all-books/', views.all_books, name='all_books'),
    # view details of a specific
    # author
    path('author-detail/<str:pk>/', views.author_detail, name='author_detail'),
    # category
    path('category-detail/<str:pk>/', views.category_detail, name='category_detail'),
    # book
    path('book-detail/<str:pk>/', views.book_detail, name='book_detail'),
    # view list
    # ID
    # authors
    path('author-id-list/', views.authorIdList, name='authorIdList'),
    # categories
    path('category-id-list/', views.categoryIdList, name='categoryIdList'),
    # books
    path('book-id-list/', views.bookIdList, name='bookIdList'),
    # names
    # authors
    path('author-name-list/', views.authorNameList, name='authorNameList'),
    # categories
    path('category-name-list/', views.categoryNameList, name='categoryNameList'),
    # books
    path('book-name-list/', views.bookNameList, name='bookNameList'),
    # filter search
    # charcater field
    # show book details of a specific author
    path('author-books/<str:pk>/', views.author_books, name='author-books'),
    # show book details of a specific category
    path('category-books/<str:pk>/', views.category_books, name='category-books'),
    # search book by partial text
    path('find/', views.SearchText.as_view(), name='search'),
    # integer field
    # max sold book
    path("max-sold-book/", views.max_sold_book, name="max_sold_book"),
    # max sold book author
    path('max-sold-book-author/<str:pk>/', views.max_sold_book_author, name='max_sold_book_author'),
    # max sold book category
    path('max-sold-book-category/<str:pk>/', views.max_sold_book_category, name='max_sold_book_category'),

    # POST
    # add author
    path('add-author/', views.add_author, name='add_author'),
    # add category
    path('add-category/', views.add_category, name='add_category'),
    # add book
    path('add-book/', views.add_book, name='add_book'),

    # UPDATE
    # update author
    path('update-author/<str:pk>/', views.update_author, name='update_author'),
    # update category
    path('update-category/<str:pk>/', views.update_category, name='update_category'),
    # update book
    path('update-book/<str:pk>/', views.update_book, name='update_book'),

    # DELETE
    # delete author
    path('delete-author/<str:pk>/', views.delete_author, name='delete_author'),
    # delete category
    path('delete-category/<str:pk>/', views.delete_category, name='delete_category'),
    # delete book
    path('delete-book/<str:pk>/', views.delete_book, name='delete_book'),


]