from django.shortcuts import render

from .models import HealthSurvey

def survey_list(request):
    surveys = HealthSurvey.objects.all()
    context = {
        'surveys': surveys
    }
    return render(request, 'survey.html', context)

