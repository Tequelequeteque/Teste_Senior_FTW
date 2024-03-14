from .serializers import TaskSerializer
from .models import Tasks
from rest_framework import viewsets

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

