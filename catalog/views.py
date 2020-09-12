from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Era
from django.views import generic

# Create your views here.

def index(request):
    """
    Display function for the site's home page.
    """

    # Generate "quantities" of some of the main objects
    num_books = Book.objects.all().count()
    
    num_instances = BookInstance.objects.all().count()
    
    num_genres = Genre.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()
    
    num_authors = Author.objects.count()

    num_eras = Era.objects.count()
    
    # Rendering an HTML template index.html with data inside
    # of the context variable "context"
    
    return render(
        request,
        'index.html',
        context = {'num_books': num_books, 'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors, 'num_genres': num_genres,
            'num_eras': num_eras,}
    )
    
class BookListView(generic.ListView):
    model = Book
    
    paginate_by = 10
        
class BookDetailView(generic.DetailView):
    model = Book
    
class AuthorListView(generic.ListView):
    model = Author
    
    paginate_by = 10
    
class AuthorDetailView(generic.DetailView):
    model = Author
    
class EraListView(generic.ListView):
    model = Era
    
    paginate_by = 10
    
class EraDetailView(generic.DetailView):
    model = Era