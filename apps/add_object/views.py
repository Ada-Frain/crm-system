from django.shortcuts import render
from apps.core.models import Project
from .forms import ProjectCreateForm

def add_object(request):
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            project = form.save()
            return render(request, 'add_object/added.html', {'project': project})
    
    else:
        form = ProjectCreateForm
    return render(request, 'add_object/add.html', {'form': form})
    