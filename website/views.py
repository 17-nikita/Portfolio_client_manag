

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Project, Client
import json

def landing_page(request):
    projects = Project.objects.all()
    clients = Client.objects.all()

    context = {
        'projects': projects,
        'clients': clients
    }
    return render(request, 'website/landing_page.html', context)


@require_POST
def contact_submit_view(request):
    try:
        data = json.loads(request.body)
        full_name = data.get('fullName')
        email = data.get('email')
        mobile = data.get('mobile')
        city = data.get('city')

        
        print(f"Contact Submission: {full_name}, {email}, {mobile}, {city}")
        return JsonResponse({'status': 'success', 'message': 'Contact form submitted successfully!'})

    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({'status': 'error', 'message': 'An error occurred.'}, status=500)


@require_POST
def subscribe_view(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')

        
        print(f"Newsletter Subscription: {email}")
        return JsonResponse({'status': 'success', 'message': 'Subscribed successfully!'})

    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({'status': 'error', 'message': 'An error occurred.'}, status=500)

def project_detail_view(request, project_id):
    from .models import Project
    project = get_object_or_404(Project, id=project_id)

    context = {
        'project': project
    }
    return render(request, 'website/project_detail.html', context)
