from mynakama.models import Anime

def animes_dropdown(request):
    animes = Anime.objects.all()
    return {'animes': animes}