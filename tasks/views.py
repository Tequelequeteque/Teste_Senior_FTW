from .serializers import TaskSerializer
from .models import Tasks
from rest_framework import viewsets, filters

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['status','priority','created_at']
    search_fields = ['status','priority','created_at']

