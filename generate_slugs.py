import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
django.setup()

from mynakama.models import Anime
from django.template.defaultfilters import slugify

def generate_slug(instance):
    instance.slug = slugify(instance.nombre)
    instance.save()

animes = Anime.objects.all()
for anime in animes:
    generate_slug(anime)