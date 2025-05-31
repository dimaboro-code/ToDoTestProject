from rest_framework import viewsets, permissions, filters
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        completed = self.request.content_params.get('completed')
        search = self.request.content_params.get('search')
        if completed is not None:
            queryset = queryset.filter(completed=completed == 'true')
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
