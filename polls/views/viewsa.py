from django.shortcuts import render, get_object_or_404
from django.http import Http404
from polls.models import Question
from django.http import HttpResponse
from polls.models import Question

from django.template import RequestContext, loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })

    #output = ', '.join([p.question_text for p in latest_question_list])
    return HttpResponse(template.render(context))
