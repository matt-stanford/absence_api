from django.shortcuts import render
from django.views.generic.edit import FormView

from rest_framework import generics

from .models import Absence
from .serializers import AbsenceSerializer
from .forms import UploadAbsenceFileForm

import pandas as pd
import io

class AbsenceCreateView(generics.ListCreateAPIView):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
        

class AbsenceUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer

    def delete(self, request, *args, **kwargs):
        absence = Absence.objects.filter(pk=kwargs['pk'])
        if absence.exists():
            return self.destroy(request, *args, **kwargs)

    def perform_update(self, serializer, **kwargs):
        absence = Absence.objects.get(pk=self.kwargs['pk'])
        serializer.save(absence=absence)


class UploadAbsenceView(FormView):
    template_name = 'pages/upload_absence.html'
    form_class = UploadAbsenceFileForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            absence_file = request.FILES['file']

            with io.StringIO(absence_file.read().decode('utf-8')) as file_content:
                absence_data = pd.read_csv(file_content)
                
            for record in absence_data.to_dict(orient='records'):
                try:
                    Absence.objects.create(
                        employee_code = record['employee_code'],
                        absence_date = record['absence_date'],
                        absence_reason = record['absence_reason']
                    )
                except Exception as e:
                    print(e)

            return render(request, self.template_name, {'form': form})