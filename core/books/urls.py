from django.urls import path
from graphene_django.views import GraphQLView
from core.books.schema import schema

urlpatterns = [
    path("book", GraphQLView.as_view(graphiql=True,
         schema=schema))
]
