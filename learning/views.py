from .models import Articles
from django.shortcuts import render


def year_archive(request, year):
    a_list = Articles.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'learning/year_archive.html', context)

# from django.http import HttpResponse
# from .models import Reporter
# import json
#
#
# def year_archive(request, pos):
#     # These 3 lines gives data in json
#     _all_data = Reporter.objects.all()
#     json_data = json.dumps([{'name': reporter.full_name} for reporter in _all_data])
#     return HttpResponse(json_data, content_type='application/json')

