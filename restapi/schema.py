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
        option1 = graphene.String()
        option2 = graphene.String()
        option3 = graphene.String()
        option4 = graphene.String()
        option5 = graphene.String()

    question = graphene.Field(lambda: QuestionType)

    def mutate(
        self, info, title, content,
        option1, option2, option3, option4, option5
        ):
        question = Question.objects.create(
            title=title, content=content,
            option_1=option1,
            option_2=option2,
            option_3=option3,
            option_4=option4,
            option_5=option5,
            )
        return CreateQuestion(question=question)

class UpdateQuestion(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        content = graphene.String()
        option1 = graphene.String()
        result1 = graphene.Int()
        option2 = graphene.String()
        result2 = graphene.Int()
        option3 = graphene.String()
        result3 = graphene.Int()
        option4 = graphene.String()
        result4 = graphene.Int()
        option5 = graphene.String()
        result5 = graphene.Int()
    
    question = graphene.Field(lambda: QuestionType)

    def mutate(
        self, info, id, title, content,
        option1, result1,
        option2, result2,
        option3, result3,
        option4, result4,
        option5, result5,
        ):
        question = Question.objects.filter(id=id).first()
        question.title = title
        question.content = content
        question.option_1 = option1
        question.result_1 = result1
        question.option_2 = option2
        question.result_2 = result2
        question.option_3 = option3
        question.result_3 = result3
        question.option_4 = option4
        question.result_4 = result4
        question.option_5 = option5
        question.result_5 = result5

        question.calculate_ratio(
            result1, result2, result3,
            result4, result5
            )
        return UpdateQuestion(question=question)

class PostQuestion(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        option = graphene.Int()

    question = graphene.Field(lambda: QuestionType)

    def mutate(self, info, id, option):
        question = Question.objects.filter(id=id).first()
        if option == 1:
            question.result_1 += 1
        elif option == 2:
            question.result_2 += 1
        elif option == 3:
            question.result_3 += 1
        elif option == 4:
            question.result_4 += 1
        elif option == 5:
            question.result_5 += 1
        
        question.calculate_ratio(
            question.result_1,
            question.result_2,
            question.result_3,
            question.result_4,
            question.result_5
            )
        return PostQuestion(question=question)




class Mutation(graphene.ObjectType):
    create_question = CreateQuestion.Field()
    update_question = UpdateQuestion.Field()
    post_question = PostQuestion.Field()