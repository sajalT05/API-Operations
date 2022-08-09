from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Max
# rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, filters
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.views import APIView

# import files
from .serializers import *
from .models import *

# Create your views here -->

# show api overview
@api_view(['GET'])
def api_overview(request):
    '''
    list of all available api endpoints
    '''
    api_urls={
        # GET
        # view all
        'all_authors':'/all-authors/',
        'all_categories':'/all-categories/',
        'all_books':'/all-books/',
        # view details of a specific
        'author_detail':'/author-detail/<str:pk>/',
        'category_detail':'/category-detail/<str:pk>/',
        'book_detail':'/book-detail/<str:pk>/',
        # view list
        # ID
        'authorIdList':'/author-id-list/',
        'categoryIdList':'/category-id-list/',
        'bookIdList':'/book-id-list/',
        # names
        'authorNameList':'/author-name-list/',
        'categoryNameList':'/category-name-list/',
        'bookNameList':'/book-name-list/',
        # filter search by integer field
        'max_sold_book': '/max-sold-book/',
        'max_sold_book_category': '/max-sold-book-category/<str:pk>/',
        'max_sold_book_author/<str:pk>/': '/max-sold-book-author/<str:pk>/',
        # filter search book by char field
        'author_books': '/author-books/<str:pk>/',
        'category_books': '/category-books/<str:pk>/',
        'SearchText': '/find=<str>/',        
        # POST
        'add_author':'/add-author/',
        'add_category':'/add-category/',
        'add_book':'/add-book/',
        # UPDATE
        'update_author': '/update-author/<str:pk>/',
        'update_category': '/update-category/<str:pk>/',
        'update_book': '/update-book/<str:pk>/',
        # DELETE
        'delete_author': '/delete-author/<str:pk>/',
        'delete_category': '/delete-category/<str:pk>/',
        'delete_book': '/delete-book/<str:pk>/',

    }
    return Response(api_urls)

# -->API CRUD

# --> GET
# --> view all
# all_authors --> /all-authors/ --> show all authors
@api_view(['GET'])
def all_authors(request):
    '''
    show all authors
    '''
    authors=Author.objects.all()
    serializer=AuthorSerializer(authors,many=True)
    return Response(serializer.data)
# all_categories --> /all-categories/ --> show all categories
@api_view(['GET'])
def all_categories(request):
    '''
    show all categories
    '''
    categories=Category.objects.all()
    serializer=CategorySerializer(categories,many=True)
    return Response(serializer.data)
# all_books --> /all-books/ --> show all books
@api_view(['GET'])
def all_books(request):
    '''
    show all books
    '''
    books=Book.objects.all()
    serializer=BookSerializer(books,many=True)
    return Response(serializer.data)
# --> view list
# --> ID
# authorIDlist --> /author-id-list/ --> show all author IDs
@api_view(['GET'])
def authorIdList(request):
    '''
    show all author ID's
    '''
    authors=Author.objects.all()
    authorlist={"list of author ID": list(authors.values("authorID"))}
    serializer=AuthorSerializer(authors)
    return Response(authorlist)
# categoryIDlist --> /category-id-list/ --> show all category IDs
@api_view(['GET'])
def categoryIdList(request):
    '''
    show all category ID's
    '''
    categories=Category.objects.all()
    categorylist={"list of category ID": list(categories.values("categoryID"))}
    serializer=CategorySerializer(categories)
    return Response(categorylist)
# bookIDlist --> /book-id-list/ --> show all book IDs
@api_view(['GET'])
def bookIdList(request):
    '''
    show all book ID's
    '''
    books=Book.objects.all()
    booklist={"list of book ID": list(books.values("bookID"))}
    serializer=BookSerializer(books)
    return Response(booklist)
# --> names
# authorNameList --> /author-name-list/ --> show all author names
@api_view(['GET'])
def authorNameList(requst):
    '''
    show all author names
    '''
    authors=Author.objects.all()
    authorlist={"list of author names": list(authors.values("name"))}
    serializers=AuthorSerializer(authors)
    return Response(authorlist)
# categoryNameList --> /category-name-list/ --> show all category names
@api_view(['GET'])
def categoryNameList(request):
    '''
    show all category names
    '''
    categories=Category.objects.all()
    categorylist={"list of category names": list(categories.values("name"))}
    serializer=CategorySerializer(categories)
    return Response(categorylist)
# bookNameList --> /book-name-list/ --> show all book names
def bookNameList(request):
    '''
    show all book names
    '''
    books=Book.objects.all()
    booklist={"list of book names": list(books.values("name"))}
    serializer=BookSerializer(books)
    return Response(booklist)
# --> view details of a specific object
# author_detail --> /author-detail/<str:pk>/ --> show details of a specific author
@api_view(['GET'])
def author_detail(request,pk):
    '''
    show details of a specific author
    '''
    author=Author.objects.get(pk=pk)
    serializer=AuthorSerializer(author)
    return Response(serializer.data)
# category_detail --> /category-detail/<str:pk>/ --> show details of a specific category
@api_view(['GET'])
def category_detail(request,pk):
    '''
    show details of a specific category
    '''
    category=Category.objects.get(pk=pk)
    serializer=CategorySerializer(category)
    return Response(serializer.data)
# book_detail --> /book-detail/<str:pk>/ --> show details of a specific book
@api_view(['GET'])
def book_detail(request,pk):
    '''
    show details of a specific book
    '''
    book=Book.objects.get(pk=pk)
    serializer=BookSerializer(book)
    return Response(serializer.data)
# --> filter search
# --> char field value
# --> show book details of a specific author
# author_books --> /author-books/<str:pk>/ --> show book details of a specific author
@api_view(['GET'])
def author_books(request,pk):
    '''
    show book details of a specific author
    '''
    books=Book.objects.filter(authorID=pk)
    serializer=BookSerializer(books,many=True)
    return Response(serializer.data)
# --> show book details of a specific category
# category_books --> /category-books/<str:pk>/ --> show book details of a specific category
@api_view(['GET'])
def category_books(request,pk):
    '''
    show book details of a specific category
    '''
    books=Book.objects.filter(categoryID=pk)
    serializer=BookSerializer(books,many=True)
    return Response(serializer.data)
# --> integer field value
# max_sold_book --> /max-sold-book/ --> show max sold book
@api_view(['GET'])
def max_sold_book(request):
    '''
    show max sold book
    '''
    book=Book.objects.all().order_by('soldCount').reverse()[0]
    serializer=BookSerializer(book)
    return Response(serializer.data)
# max_sold_book_author --> /max-sold-book-author/ --> show max sold book by author
@api_view(['GET'])
def max_sold_book_author(request,pk):
    '''
    show max sold book author
    '''
    books=Book.objects.filter(authorID=pk).order_by('soldCount').reverse()[0]
    serializer=BookSerializer(books)
    return Response(serializer.data)
# max_sold_book_category --> /max-sold-book-category/ --> show max sold book by category
@api_view(['GET'])
def max_sold_book_category(request,pk):
    '''
    show max sold book category
    '''

    books=Book.objects.filter(categoryID=pk).order_by('soldCount').reverse()[0]
    serializer=BookSerializer(books)
    return Response(serializer.data)
# search_book --> /search-book/ --> show search book
class SearchText(ListAPIView):
    '''
    search books with text in book title, author name
    ''' 
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title','authorID__name']

# --> POST
# --> add new
# add_author --> /add-author/ --> add new author
@api_view(['POST'])
def add_author(request):
    '''
    add new author
    '''
    serializer=AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# add_category --> /add-category/ --> add new category
@api_view(['POST'])
def add_category(request):
    '''
    add new category
    '''
    serializer=CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# add_book --> /add-book/ --> add new book
@api_view(['POST'])
def add_book(request):
    '''
    add new book
    '''
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# UPDATE
# --> update existing
# update_author --> /update-author/<str:pk>/ --> update author
@api_view(['PUT'])
def update_author(request,pk):
    '''
    update author
    '''
    author=Author.objects.get(pk=pk)
    serializer=AuthorSerializer(instance=author,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# update_category --> /update-category/<str:pk>/ --> update category
@api_view(['PUT'])
def update_category(request,pk):
    '''
    update category
    '''
    category=Category.objects.get(pk=pk)
    serializer=CategorySerializer(instance=category,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# update_book --> /update-book/<str:pk>/ --> update book
@api_view(['PUT'])
def update_book(request,pk):
    '''
    update book
    '''
    book=Book.objects.get(pk=pk)
    serializer=BookSerializer(instance=book,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# DELETE
# --> delete existing
# delete_author --> /delete-author/<str:pk>/ --> delete author
@api_view(['DELETE'])
def delete_author(request,pk):
    '''
    delete author
    '''
    author=Author.objects.get(pk=pk)
    author.delete()
    return Response('Author deleted successfully')
# delete_category --> /delete-category/<str:pk>/ --> delete category
@api_view(['DELETE'])
def delete_category(request,pk):
    '''
    delete category
    '''
    category=Category.objects.get(pk=pk)
    category.delete()
    return Response('Category deleted successfully')
# delete_book --> /delete-book/<str:pk>/ --> delete book
@api_view(['DELETE'])
def delete_book(request,pk):
    '''
    delete book
    '''
    book=Book.objects.get(pk=pk)
    book.delete()
    return Response('Book deleted successfully')

