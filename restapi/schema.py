import graphene
from graphene_django.types import DjangoObjectType
from .models import Question


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question


class Query:
    all_questions = graphene.List(QuestionType)

    def resolve_all_questions(self, info, **kwargs):
        return Question.objects.all()