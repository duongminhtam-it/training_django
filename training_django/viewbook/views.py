# from django.http import request
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, FormView, DeleteView, CreateView
from viewbook.models import Book
from django.core.paginator import Paginator
from viewbook.forms import BookForm


class ViewListBook(ListView):
    model = Book
    paginate_by = 2

    def get_queryset(self):  # Get data from database and setting, this is stronger get_context_data
        key_word = self.request.GET.get('q')
        if key_word:
            return Book.objects.filter(name__icontains=key_word)
        else:
            return Book.objects.all()

    def deletet(self, *args, **kwargs):
        import json
        a = json.load(self.request["body"])
        id = self.request.GET.get('id')
        # delete = Book.delete(id=)


class FormViewBook(FormView):
    template_name = 'viewbook/formview.html'
    form_class = BookForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.dosomething()
        return HttpResponse("thanh cong")
        # return super(FormViewBook, self).form_valid(form)

class CreatedViewBook(CreateView):
    model = Book
