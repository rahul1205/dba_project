import os
from django.shortcuts import render
from main.models import StudentData
from main.serializers import StudentDataSerializer, StudentDataPublicSerializer
from rest_framework import generics, permissions, views, response, status
from main.services import load_data

# URLs of these APIs can be found under db/urls.py

module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'course_marks.csv') # replace course_marks.csv with actual excel/csv file

class LoadData(generics.GenericAPIView):
    """
    API to load CSV to MySQL database
    URI localhost:8000/load-data/
    """
    def get(self, request):
        file = open(file_path)
        for line in file.readlines()[2:20]:
            values = line.split(',')
            load_data(values)
        return response.Response(
                    status=status.HTTP_200_OK)

class GetGraduands(generics.ListAPIView):
    """
    API to determine sexton distinction or distinction
    URI localhost:8000/get-graduands/
    """
    model = StudentData
    serializer_class = StudentDataSerializer
    def get_queryset(self):
        return self.model.objects.filter(applied_to_graduate='GS')

class CreateAssessmentReport(generics.ListAPIView):
    """
    General API to fetch all data
    URI localhost:8000/create-assessment-report
    """
    model = StudentData
    serializer_class = StudentDataPublicSerializer
    def get_queryset(self):
        return self.model.objects.all()