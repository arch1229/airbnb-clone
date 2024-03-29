from django.views.generic import ListView
from . import models

# Create your views here.
class RoomList(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = 'created'