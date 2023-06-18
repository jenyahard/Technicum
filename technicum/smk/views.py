from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def smk(request: HttpRequest) -> HttpResponse:
    template = 'smk.html'
    return render(request, template)


def smk_get_data(request: HttpRequest) -> HttpResponse:
    # folder_path = os.path.join(settings.MEDIA_ROOT, 'smk')
    # smk_base_files_list = os.listdir(folder_path)
    # fields_dict = {}
    # doc_type = 'smk'
    template = 'smk.html'
    return render(request, template)
