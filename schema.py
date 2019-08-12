import graphene
import questions.schema


class Query(questions.schema.Query,
            graphene.ObjectType):
    pass


schema = graphene.Schema(
    query=Query,
)