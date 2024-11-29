from django.http import HttpResponse
from django.shortcuts import render
from .models import Test, Question, Answer


# Create your views here.


def test(response, test_id):
    test_obj = Test.objects.filter(id=test_id).first()

    question_list = [i for i in Question.objects.filter(test__id=test_id)]
    answer_list = {}
    for i in question_list:
        answer_list.update({i.id: [answer for answer in Answer.objects.filter(question__id=i.id)] })
    return render(response, "test.html", context={"question_list": question_list, "test_obj": test_obj, "answer_list": answer_list})