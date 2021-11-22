from re import template
from django.conf.urls import url
from django.urls import path, include
from blog.views import iletisim, anasayfa, KategoriListView, yazilarim, DetayView, YaziEkleCreateView, yazi_guncelle, YaziSilDeleteView, yorum_sil
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('iletisim', iletisim, name='iletisim'),
    path('kategori/<slug:kategoriSlug>',
         KategoriListView.as_view(), name='kategori'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', DetayView.as_view(), name='detay'),
    path('yazi-ekle', YaziEkleCreateView.as_view(), name='yazi-ekle'),
    path('yazi-guncelle/<slug:slug>', yazi_guncelle, name='yazi-guncelle'),
    path("yazi-sil/<slug:slug>", YaziSilDeleteView.as_view(), name="yazi-sil"),
    path('yorum-sil/<int:id>', yorum_sil, name="yorum-sil"),
    path('hakkimda', TemplateView.as_view(
        template_name='pages/hakkimda.html'), name='hakkimda'),
    path('yonlendir', RedirectView.as_view(
        url='www.google.com'
    ), name='yonlendir'),

]
