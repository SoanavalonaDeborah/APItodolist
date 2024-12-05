from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import TasksModel
from .serializers import TasksSerializer


class TaskListView(generics.ListCreateAPIView):
    queryset = TasksModel.objects.all()
    serializer_class = TasksSerializer
    
    def get(self, request):
    # Récupère les tâches appartenant à l'utilisateur connecté.
        tasks = TasksModel.objects.filter(owner=request.user)
         # Sérialise les tâches pour les retourner sous forme de JSON.
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)  # Retourne les données des tâches en réponse.

    def post(self, request):
         # Sérialise les données envoyées pour créer une nouvelle tâche.
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():  # Vérifie si les données sont valides.
            serializer.save(owner=request.user)  # Associe la tâche à l'utilisateur connecté.
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Retourne la tâche créée.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retourne les erreurs en cas de problème.


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TasksModel.objects.all()
    serializer_class = TasksSerializer