# -*- coding: utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from polls.models import Question, Choice

# logging 추가
import logging
logger = logging.getLogger(__name__)

#-- Class-based GenericView
class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        '''Return the last five published questions.'''
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'


#-- Function-based View
def vote(request, question_id):
    logger.debug('vote().question_id: %s' % question_id) # 추가
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # 설문 투표 폼을 다시 보여준다.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터를 정상적으로 처리하였으면,
        # 항상 HttpResponseRedirect를 반환하여 리다이렉션 처리함
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))