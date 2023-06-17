from scripts.scripts import transform_data

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def rexpl(request: HttpRequest) -> HttpResponse:
    template = 'rexpl.html'
    return render(request, template)


def rexpl_get_data(request: HttpRequest) -> HttpResponse:
    fields_dict = {}
    doc_type = fields_dict['doc_type'] = 'rexpl'
    response = transform_data(fields_dict, doc_type, request)
    return response
