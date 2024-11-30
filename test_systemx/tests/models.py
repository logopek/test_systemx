from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.template.defaultfilters import default


# Create your models here.
class Test(models.Model):
    text = models.CharField(max_length=2048, default=" ")
    mark = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)], default=100)



class Question(models.Model):
    class AnswerType(models.TextChoices):
        CHOICE = "choice"
        MULTICHOICE = "multichoice"
        TEXT = "text"



    test = models.ForeignKey(Test, on_delete=models.CASCADE, default=0)
    text = models.CharField(max_length=2048)
    answer_type = models.TextField(choices=AnswerType.choices, null=False, default=AnswerType.CHOICE)
    right_answer_id = models.IntegerField() # TODO: Сделать нормальную систему выбора правильного ответа



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=0, related_name="answers")
    text = models.TextField(max_length=2048)