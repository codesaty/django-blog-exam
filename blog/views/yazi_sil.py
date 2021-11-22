from django.contrib.auth.decorators import login_required
from blog.models import Yazilar
from django.shortcuts import redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy


class YaziSilDeleteView(DeleteView):

    template_name = 'pages/yazi_sil_onay.html'
    success_url = reverse_lazy('yazilarim')

    def get_queryset(self):
        yazi = Yazilar.objects.filter(
            slug=self.kwargs['slug'], yazar=self.request.user)
        return yazi
