from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import List

class IndexView(generic.ListView):
    template_name = 'myapp/index.html'

    def get_queryset(self):
        return List.objects.all()

class AddTodo(CreateView):
    model = List
    fields = ['title','description','createddate','completiondate','priority','completed']





