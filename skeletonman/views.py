# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.views.generic.base import TemplateView


# Create your views here.

# Create your views here.
from django.http import HttpResponse


class HomePageView(TemplateView):

    template_name = "skeletonIndex.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context


def index(request):
    template = loader.get_template("app/skeletonIndex.html")
    return HttpResponse(template.render())


@csrf_exempt
def servo_number(request, pk):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        return JsonResponse("some shit from skeletonman servo rest api " + pk, safe=False)


@csrf_exempt
def servo_all(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        return JsonResponse("some shit from skeletonman servo rest api", safe=False)