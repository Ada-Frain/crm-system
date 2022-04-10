from re import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from apps.core.models import Project

def home_page(request):
    projects = Project.objects.all()

    return render(
            request,
            'core/db.html',
            {'projects': projects}
        )

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)

    return render(
            request,
            'core/detail.html',
            {'project': project}
        )


    

