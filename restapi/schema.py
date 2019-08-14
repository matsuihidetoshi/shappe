import graphene
from graphene_django.types import DjangoObjectType
from .models import Question


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question


class Query:
    all_questions = graphene.List(QuestionType)
    question = graphene.Field(QuestionType,
                              id=graphene.Int(),
                              title=graphene.String())

    def resolve_all_questions(self, info, **kwargs):
        return Question.objects.all()

    def resolve_question(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return Question.objects.get(pk=id)

        if title is not None:
            return Question.objects.get(title=title)

        return None

class CreateQuestion(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        content = graphene.String()

    question = graphene.Field(lambda: QuestionType)

    def mutate(self, info, title, content):
        question = Question.objects.create(title=title, content=content)
        return CreateQuestion(question=question)

class UpdateQuestion(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        content = graphene.String()
    
    question = graphene.Field(lambda: QuestionType)

    def mutate(self, info, id, title, content):
        question = Question.objects.filter(id=id).first()
        question.content = content
        question.save()
        return UpdateQuestion(question=question)

class Mutation(graphene.ObjectType):
    create_question = CreateQuestion.Field()
    update_question = UpdateQuestion.Field()