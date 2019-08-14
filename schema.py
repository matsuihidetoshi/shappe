import graphene
import restapi.schema


class Query(restapi.schema.Query,
            graphene.ObjectType):
    pass

class Mutation(restapi.schema.Mutation,
               graphene.ObjectType):
    pass

schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)