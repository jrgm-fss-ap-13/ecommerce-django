from django import forms
from .models import Producto, Manga, Figura

class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
   
class MangaForm(ProductForm):
    class Meta(ProductForm.Meta):
        model = Manga
        exclude = ['anime_id_anime']

class FiguraForm(ProductForm):
    class Meta(ProductForm.Meta):
        model = Figura
        exclude = ['anime_id_anime']   