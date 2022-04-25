from django.shortcuts import render
from django.http import HttpResponse


projectlist = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website.'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'This was a project where I built out my portfolio.'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Awesome open-source project I am still working on.'
    },
]


def projects(request):
    page = "projects"
    number = 11
    context = {
        'page': page,
        'number': number,
        'projects': projectlist
    }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project_obj = None
    for i in projectlist:
        if i['id'] == pk:
            project_obj = i
    return render(request, 'projects/single-project.html', {'project': project_obj})
