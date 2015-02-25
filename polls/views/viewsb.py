from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from polls.models import Question, Choice
from django.core.urlresolvers import reverse
from django.views import generic
# *****  All Django wants is that HttpResponse. Or an exception.   ****
from django.utils import timezone



class DetailView(generic.DetailView) : 
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self) :
        return Question.objects.filter(pub_date__lte=timezone.now())

"""
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
"""

class ResultsView(generic.DetailView) :
    model = Question
    template_name = 'polls/results.html'

"""
def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/results.html', {'question' : question })
"""


def vote(request, question_id):
    #simple case return HttpResponse("You're voting on question %s." % question_id)
    p = get_object_or_404(Question, pk=question_id)
    try :
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist) : 
        return render(request , 'polls/detail.html', {
            "question" : p,  
            "error_message" : "You didn't select a choice." , 
        })
    else :
        selected_choice.votes +=1
        selected_choice.save()
        ## Always return an HttpResponseRedirect after successfully dealing with POST data!!!
        ## prevents data from being doubly-posted if the user hits the back button!!!!
        
        return HttpResponseRedirect(reverse('polls:results', args = (p.id,) ) )
         
        # pass top HttpResponseRedirect, 
        #   the name of the view that we want to pass control to 
        #   and the variable portion of the URL pattern that points to that view
