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
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    price = int(request.GET.get("price", 0))
    guest = int(request.GET.get("guest", 0))
    bed = int(request.GET.get("bed", 0))
    bedroom = int(request.GET.get("bedroom", 0))
    bath = int(request.GET.get("bath", 0))
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")
    instant = bool(request.GET.get("instant", False))
    super_host = bool(request.GET.get("super_host", False))

    room_type = int(request.GET.get("room_type", 0))
    room_types = models.RoomType.objects.all()

    amenities = models.Amenity.objects.all()

    facilities = models.Facility.objects.all()

    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guest": guest,
        "bed": bed,
        "bedroom": bedroom,
        "bath": bath,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "super_host": super_host,
    }

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args["country__startswith"] = country

    if room_type != 0:
        filter_args["room_type__pk"] = room_type

    if price != 0:
        filter_args["price__lte"] = price

    if guest != 0:
        filter_args["guests__gte"] = guest

    if bed != 0:
        filter_args["beds__gte"] = bed

    if bedroom != 0:
        filter_args["bedrooms__gte"] = bedroom

    if bath != 0:
        filter_args["baths__gte"] = bath

    if instant is True:
        filter_args["instant_book"] = True

    if super_host is True:
        filter_args["host__superhost"] = True

    if len(s_amenities) > 0:
        for s_amenity in s_amenities:
            filter_args["amenity__pk"] = int(s_amenity)

    if len(s_facilities) > 0:
        for s_facility in s_facilities:
            filter_args["facility__pk"] = int(s_facility)

    rooms = models.Room.objects.filter(**filter_args)

    return render(
        request,
        "rooms/search.html",
        {**form, **choices, "rooms": rooms},
    )
