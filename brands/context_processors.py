from os import link
from .models import Brand

def menu_links(request):
    link = Brand.objects.all()
    return dict(link=link)