from django.contrib import admin
from cinema.models import Categorie, Films, Ticket, Place, Salle

# Register your models here.

admin.site.register([
    Categorie,
    Films,
    Ticket,
    Place,
    Salle

])
