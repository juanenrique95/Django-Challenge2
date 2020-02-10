from rest_framework import mixins, viewsets

from . import models
from . import serializers
from rest_framework import status, response
from rest_framework.decorators import api_view


class AccountViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    """
        API endpoint that allows accounts to be viewed.

        list:
        Return all the accounts available.

        create:
        Create an account.

        retrieve:
        Return a given account.

        update:
        Update a given account.
    """
    # model = models.Account
    # serializer_class = serializers.AccountSerializer
    queryset = models.Account.objects.all()


    def get_serializer_class(self):
        serializer_class = serializers.AccountSerializer
        if self.action == 'update':
            serializer_class = serializers.AccountSerializer_Update
        return serializer_class



    def update(self, request, pk=None):
        super().update(request, pk)
        account = self.get_object()
        serialized_account = serializers.AccountSerializer(account)
        return response.Response(data=serialized_account.data, status=status.HTTP_200_OK)


def f(x):
    response = ""
    for i in range(1, x+1):
        if i % 15 == 0:
            response += "FizzBuzz"
        elif i % 3 == 0:
            response += "Fizz"
        elif i % 5 == 0:
            response += "Buzz"
        else:
            response += str(i)
    return response
    # return if x % 3 == 0: 'Fizz' elif x % 5 == 0: 'Buzz' else x

@api_view(["GET"])
def fizz_buzz(request):
    x = request.query_params.get('x', 100)
    response_data = {
        'x': x,
        "fizzbuzz": f(int(x))
    }
    return response.Response(data=response_data, status=status.HTTP_200_OK)

    # def list(self, request):
    #     print("listar")
    #     return super().list(request)

    # def retrieve(self, request, pk=None):
    #     print("retrievear")
    #     return super().retrieve(request, pk)
