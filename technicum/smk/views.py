import os

from scripts.scripts import smk_transform_data

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.conf import settings


def smk(request: HttpRequest) -> HttpResponse:
    template = 'smk.html'
    return render(request, template)


def smk_get_data(request: HttpRequest) -> HttpResponse:
    folder_path = os.path.join(settings.MEDIA_ROOT, 'smk')
    smk_base_files_list = os.listdir(folder_path)
    fields_dict = {}
    fields_dict['doc_type'] = 'smk'
    fields_dict['smk_base_files_list'] = smk_base_files_list
    return smk_transform_data(fields_dict, request)
