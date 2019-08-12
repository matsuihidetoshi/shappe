import graphene
from graphene_django import DjangoObjectType
from questions.models import Question


class Item(DjangoObjectType):
    class Meta:
        model = Question


class Query(graphene.ObjectType):
    questions = graphene.List(Item)