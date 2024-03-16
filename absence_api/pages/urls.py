from django.urls import path
from .views import AbsenceCreateView, AbsenceUpdateView, UploadAbsenceView

urlpatterns = [
    path('api/absences/', AbsenceCreateView.as_view()),
    path('api/absences/<int:pk>/update/', AbsenceUpdateView.as_view()),
    path('upload_file/', UploadAbsenceView.as_view())
]