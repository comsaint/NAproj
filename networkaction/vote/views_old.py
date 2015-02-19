from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from vote.models import Question
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
import pdb

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('vote/index.html')
#     context = RequestContext(request, {
#         'latest_question_list': latest_question_list,
#     })
#     return HttpResponse(template.render(context))
    context = {'latest_question_list': latest_question_list} #Shortcut
    return render(request, 'vote/index.html', context)

def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id) #stub example
    
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'vote/detail.html', {'question': question})

    question = get_object_or_404(Question, pk=question_id) #shortcut
    return render(request, 'vote/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'vote/results.html', {'question': question})

def voting(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = request.POST['choice']
        # request.POST returns a dict-like object, with values always being strings
        # request.POST['choice'] look at the 'value' field of a name 'choice'
        # Here we should get either "YES", "NO" or "ABSTAIN"
    
    #pdb.set_trace()
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
        
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('vote:results', args=(p.id,)))
