from rest_framework.response import Response
from rest_framework import viewsets

class TestViewSet(viewsets.ViewSet):
    swagger_schema = None

    def list(self, request):
        return Response({'message': 'Hello!', 'from': 'ClearDrop Project'})
