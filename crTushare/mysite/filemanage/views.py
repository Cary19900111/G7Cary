# from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from django.http import FileResponse
import os

# Create your views here.


def index(request):
    file_list = []
    prjpath = os.getcwd()
    filepath = prjpath+"/filemanage/download"
    for dirpath, dirnames, filenames in os.walk(filepath):
        # print("dirpath:")
        # print(dirpath)
        # print("dirnames:")j
        # print(dirnames)
        # print("filenames:")
        # print(filenames)
        for file in filenames:
                fullpath = os.path.join(dirpath, file)
                file_list.append(fullpath.split("/")[-1])
    context = {
        'list': file_list
    }
    return render(request, "filemanage/index.html", context)


def downfile(request, filename):
    filepath = os.getcwd() + "/filemanage/download/" + filename
    print(filepath)
    file = open(filepath, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename={}'.format(filename)
    return response
