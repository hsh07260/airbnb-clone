from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models

# from . import models as room_models

"""
def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    try:
        rooms = paginator.get_page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        rooms = paginator.page(1)
        return redirect("/")
"""

"""
def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
    except models.Room.DoesNotExist:
        raise Http404()

    return render(request, "rooms/detail.html", {"room": room})
"""


class HomeView(ListView):
    """Home View Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    page_kwarg = "page"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room


def search(request):

    return render(
        request,
        "rooms/search.html",
        {},
    )
