from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from vote.models import Question

import datetime
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'vote/index.html'
    context_object_name = 'latest_question_list'
    #use 'context_object_name' to ask django to use a variable named 'latest_question_list' as context object
    #instead of 'question_list'(default)
    #the function "get_queryset" below will return an object called 'latest_question_list'(as we named above),
    #which is used in 'vote/index.html'
    #we may also leave 'context_object_name' default here and change 'latest_question_list' to 'question_list'
    #in vote/index.html instead, but it is a lot easier to specify the name here 
    #since we had already written the html file
    
    def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'vote/detail.html' #use this html, otherwise default to <app name>/<model name>_detail.html
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'vote/results.html' 
    #if we do not specify this, django will use the same "DetailView" template to parse model "Question", 
    #resulting in a same view for different pages


def voting(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = request.POST['choice']
    except (KeyError, p.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'vote/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        if selected_choice == 'YES':
            p.vote_count_YES += 1
            p.save()
        elif selected_choice == 'NO':
            p.vote_count_NO += 1
            p.save()
        elif selected_choice == 'ABSTAIN':
            p.vote_count_ABSTAIN += 1
            p.save()
        else:
            return(request,'vote/detail.html',{
            'question':p,
            'error_message':"Cannot recognise this choice!"
            })
        return HttpResponseRedirect(reverse('vote:results', args=(p.id,)))
