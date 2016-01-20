from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Store, User, Review, Comment
from .forms import StoreForm

# Create your views here.
def index(request):
    return render(request, 'legolas/index.html')


def storelist(request , pk=1):
    per_page = 10
    start_pos = (int(pk) - 1) * per_page
    end_pos = start_pos + per_page
    storelist = Store.objects.all().order_by('-store_rating')[start_pos:end_pos]
    return render(request, 'legolas/storelist.html', {'storelist': storelist})

def a_store(request, pk):
    store = Store.objects.get(pk=pk)
    return render(request, 'legolas/store_page.html', {'store': store})

def store_new(request):
    if (request.method == "post"):
        form = StoreForm(request.post)
        if form.is_valid():
            store = form.save(commit=False)
            store_rating = 0
            store.save()
            return redirect('legolas.views.a_store', pk=store.pk)
    else:
        form = StoreForm()
    return render(request, 'legolas/store_edit.html', {'form': form})



def a_user(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'legolas/user_page.html', {'user': user})