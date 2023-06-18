from scripts.scripts import transform_data

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def tu(request: HttpRequest) -> HttpResponse:
    template = 'tu.html'
    return render(request, template)


def tu_get_data(request: HttpRequest) -> HttpResponse:
    fields_dict = {}
    fields_dict['doc_type'] = 'tu'
    return transform_data(fields_dict, request)
