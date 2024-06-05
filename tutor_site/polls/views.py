from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F

from .models import Question, Choice

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_questions_list': latest_questions_list,
    }
    return render(request, 'polls/index.html', context=context)


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    context = {'question': question, 'show_question_info': True}
    return render(request, 'polls/detail.html', context)


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request: HttpRequest, question_id: int) -> HttpResponse:

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(
            request,
            'polls/detail.html',
            {
                'question': question,
                'error_message': 'You did not select a choice',
            },
        )
    else:
        # selected_choice.votes += 1  # possible race conditions if 2 user are voting at the same time !!!
        selected_choice.votes = F('votes') + 1  # avoid race condition by incrementing value in DB query
        selected_choice.save()
        selected_choice.refresh_from_db()  # reload obj to remove F(), in case save() called again in this view
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question_id, )))
