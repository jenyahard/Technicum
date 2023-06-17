from scripts.scripts import transform_data

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def dul(request: HttpRequest) -> HttpResponse:
    template = 'dul.html'
    return render(request, template)


def dul_get_data(request: HttpRequest) -> HttpResponse:
    fields_dict = {}
    doc_type = fields_dict['doc_type'] = 'dul'
    response = transform_data(fields_dict, doc_type, request)
    return response
