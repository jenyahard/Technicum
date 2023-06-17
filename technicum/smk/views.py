from scripts.scripts import transform_data

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def smk(request: HttpRequest) -> HttpResponse:
    template = 'smk.html'
    return render(request, template)


def smk_get_data(request: HttpRequest) -> HttpResponse:
    fields_dict = {}
    doc_type = fields_dict['doc_type'] = 'smk'
    response = transform_data(fields_dict, doc_type, request)
    return response
