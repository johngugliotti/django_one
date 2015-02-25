from django.shortcuts import render, get_object_or_404
from django.http import Http404
from polls.models import Question
from django.http import HttpResponse
from polls.models import Question
from django.views import generic
from django.utils import timezone

from django.template import RequestContext, loader

class IndexView(generic.ListView) : 
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self) :
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })

    #output = ', '.join([p.question_text for p in latest_question_list])
    return HttpResponse(template.render(context))
"""
