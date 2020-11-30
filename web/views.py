import datetime
import mimetypes
import os

import qrcode
from django.conf import settings
from django.template.context_processors import media
from django.template.defaulttags import url
from django.templatetags.static import static
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from django.views.generic.edit import FormMixin

from web.forms import UploadFileForm


class WebView(FormView, FormMixin):
    template_name = 'web/index.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('main')

    def get(self, request, *args, **kwargs):
        uploaded_file_url = self.request.session.pop('uploaded_file_url', '')
        if uploaded_file_url:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )

            qr.add_data(uploaded_file_url)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            from django.http import HttpResponse
            response = HttpResponse(content_type="image/jpeg")
            img.save(response, "JPEG", quality=80)
            return response
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        if form.cleaned_data.get('file'):
            file_system_path = f"{settings.MEDIA_ROOT}/{form.cleaned_data.get('file').name}"
            # file_system_path = f"static/{form.cleaned_data.get('file').name}"
            file_media_url = f"{settings.MEDIA_URL}{form.cleaned_data.get('file').name}"
            if not os.path.isdir(settings.MEDIA_ROOT):
            # if not os.path.isdir(settings.STATIC_ROOT):
                try:
                    # Python ≥ 3.5
                    # https://stackoverflow.com/a/273227/3377046
                    from pathlib import Path
                    # Path(settings.STATIC_ROOT).mkdir(parents=True, exist_ok=True)
                    Path(settings.STATIC_ROOT).mkdir(parents=True, exist_ok=True)
                except ImportError:
                    # os.makedirs(settings.STATIC_ROOT)
                    os.makedirs(settings.MEDIA_ROOT)

            with open(file_system_path, 'wb+') as destination:
                for chunk in form.cleaned_data.get('file').chunks():
                    destination.write(chunk)

            # reversed_url = static(file_media_url)
            # reversed_url = static(form.cleaned_data.get('file').name)
            # url('media', form.cleaned_data.get('file').name)
            self.request.session['uploaded_file_url'] = f"{self.request.build_absolute_uri()[:-1]}{file_media_url}"
        return super().form_valid(form)
        # return foo
