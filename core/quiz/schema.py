import graphene


from graphene_django import DjangoObjectType, DjangoListField

from .models import Quizzes, Category, Question, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id',
                  'name')


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ('id',
                  'title',
                  'category',
                  'quiz')


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('title',
                  'quiz')


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ('question',
                  'answer_text')


class Query(graphene.ObjectType):

    all_quizzes = DjangoListField(QuizzesType)
    all_questions = DjangoListField(QuestionType)

    def resolve_all_quizzes(root, info):
        return Question.objects.all()


    def resolve_all_quizzes(root, info):
        return Quizzes.objects.filter(id=1)


schema = graphene.Schema(query=Query)
