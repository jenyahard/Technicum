from scripts.scripts import transform_data

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def obez(request: HttpRequest) -> HttpResponse:
    template = 'obez.html'
    return render(request, template)


def obez_get_data(request: HttpRequest) -> HttpResponse:
    fields_dict = {}
    fields_dict['doc_type'] = 'obez'
    fields_dict['ru_name'] = 'Обоснование безопасности'
    response = transform_data(fields_dict, request)
    return response
