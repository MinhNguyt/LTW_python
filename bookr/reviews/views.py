from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
# #btTH1-C1
# from django.http import HttpResponse
# def index(request):
#     name = request.GET.get("name") or "world"
#     return HttpResponse("Hello, {}!".format(name))
#
# #btTH2-C1
# from django.shortcuts import render
# #bt1
# def index3(request):
#     return render(request, "base3.html")
#
# #bt2
# def index1(request):
#    name = "world"
#    return render(request, "base.html", {"name": name})
#
# #bt-C1
# #bt1
# def index2(request):
#    return render(request, "base1.html")
#
# #bt2
# def search(request):
#    # Đọc cụm từ khóa tìm kiếm từ thông điệp GET
#    search = request.GET.get('search', '')
#
#    # Truyền cụm từ khóa tìm kiếm vào template thông qua hàm render
#    return render(request, 'base2.html', {'search': search})

#-------------------------#
#chương 2:
#th3_1
# from django.http import HttpResponse
# from .models import Book
# def welcome_view(request):
#     message = f"<html><h1>Welcome to Bookr!</h1> <p>{Book.objects.count()} books and counting!</p></html>"
#     return HttpResponse(message)
#th3_2
# from django.shortcuts import render
# def welcome_view (request):
#     return render(request, 'base.html')
#th3_3
from .models import Book
from .utils import average_rating
from .form import SearchForm
from .form import PublisherForm, SearchForm,ReviewForm,BookMediaForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Contributor, Publisher,Review
from django.contrib import messages
from django.utils import timezone
from PIL import Image
from django.core.files.images import ImageFile
from django.contrib.auth.decorators import (login_required,user_passes_test)

def index(request):
 return render(request, "base.html")

#bt1-chương 4
def book_search(request):
    form = SearchForm(request.GET)
    search_text = request.GET.get("search", "")
    search_history = request.session.get('search_history', [])
    books = set()
    if form.is_valid():
        search = form.cleaned_data['search']
        search_in = form.cleaned_data['search_in'] or 'Value One'
        if search_text and search_in == 'Value One':
            books = Book.objects.filter(title__icontains=search)
        elif search_text and search_in == 'Value Two':
            contributors = Contributor.objects.filter(first_names__icontains=search) | \
                           Contributor.objects.filter(last_names__icontains=search)
            books = Book.objects.filter(contributors__in=contributors)
        else:
            books = []
        if request.user.is_authenticated:
            search_history.append([search_in, search])
            request.session['search_history'] = search_history
    elif search_history:
        initial = dict(search=search_text,
                       search_in=search_history[-1][0])
        form = SearchForm(initial=initial)
    else:
        books = []
    context = {
        'form': form,
        'books': books,
        'search_text': search_text,
    }
    return render(request, 'reviews/search_results.html', context)
def book_lists(request):
     books = Book.objects.all()
     book_list = []
     for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
             book_rating = None
        number_of_reviews = 0
        book_list.append({'book': book,
            'book_rating': book_rating,
            'number_of_reviews': number_of_reviews})
     context = {
     'book_list': book_list
     }
     return render(request, 'reviews/book_list.html', context)



#bt2
from django.shortcuts import render
from .models import Review, Book
from .utils import average_rating
def index(request):
    return render(request, "base.html")
# def book_search(request):
#     search_text = request.GET.get("search", "")
#     return render(request,"reviews/book_detail.html,{"search_text": search_text})


def book_list(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
    else:
        book_rating = None

    revs = Review.objects.filter(book__id=book_id)
    review_list = []
    for review in revs:
        review_list.append({'review': review})
    context = {
        'book': book,
        'book_rating': book_rating,
        'reviews': reviews,
        'review_list': review_list
    }
    if request.user.is_authenticated:
        max_viewed_books_length = 10
        viewed_books = request.session.get('viewed_books', [])
        viewed_book = [book.id, book.title]
        if viewed_book in viewed_books:
            viewed_books.pop(viewed_books.index(viewed_book))
            viewed_books.insert(0, viewed_book)
            viewed_books = viewed_books[:max_viewed_books_length]
            request.session['viewed_books'] = viewed_books
    return render(request, 'reviews/book_detail.html', context)
# #TH2-chuong 4
# def publisher_edit(request, pk=None):
#     if pk is not None:
#         publisher = get_object_or_404(Publisher, pk=pk)
#     else:
#         publisher = None
#     if request.method == "POST":
#         form = PublisherForm(request.POST or None, instance=publisher)
#         if form.is_valid():
#             updated_publisher = form.save()
#             if publisher is None:
#                 messages.success(request, "Publisher"" was created.".format(updated_publisher))
#             else:
#                 messages.success(request, "Publisher"" was updated.".format(updated_publisher))
#             return redirect("publisher_edit",updated_publisher.pk)
#     else:
#         form = PublisherForm(instance=publisher)
#     return render(request, "reviews/instance-form.html", {"method":request.method, "form": form})

#bt2-chương 4
def is_staff_user(user):
    return user.is_staff

# @permission_required('edit_publisher')  # 9.03.1
@user_passes_test(is_staff_user)  # 9.03.2
def publisher_edit(request, pk=None):
    if pk is not None:
        instance = get_object_or_404(Publisher, pk=pk)
    else:
        instance = None
    form = PublisherForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('publisher_detail', pk=pk)
    context = {
        'form': form,
        'instance': instance,
        'model_type': 'Publisher',
    }
    return render(request, 'reviews/instance-form.html', context)

#bt3-chương4
@login_required
def review_edit(request, book_pk, review_pk=None):
    book = get_object_or_404(Book, pk=book_pk)
    if review_pk is not None:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user
        if not user.is_staff and review.creator.id != user.id:
            raise PermissionDenied
    else:
        review = None
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            if review_pk is None:
                messages.success(request, "Review for '{}' created.".format(book.title))
            else:
                review.date_edited = timezone.now()
                messages.success(request, "Review for '{}' updated.".format(book.title))
            review.save()
            return redirect('book_list', book_id=book.pk)
    else:
        form = ReviewForm(instance=review)


    return render(request, 'reviews/instance-form.html', {
        'form': form,

        'instance': review,
        'model_type': 'Review',
        'related_model_type': 'Book',
        'related_instance': book.title,
    })

#bt1-th5
from io import BytesIO
@login_required
def book_media(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookMediaForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            book = form.save(False)

            cover = form.cleaned_data.get("cover")

            if cover:
                image = Image.open(cover)
                image.thumbnail((300, 300))
                image_data = BytesIO()
                image.save(fp=image_data, format=cover.image.format)
                image_file = ImageFile(image_data)
                book.cover.save(cover.name, image_file)
            book.save()
            messages.success(request, "Book \"{}\" was successfully updated.".format(book))
            return redirect("book_list", book.pk)
    else:
        form = BookMediaForm(instance=book)

    return render(request, "reviews/instance-form1.html",
                  {"instance": book, "form": form, "model_type": "Book", "is_file_upload": True})



#TH1-chương 5


