from rest_framework import generics
from ..models import Lesson, LessonStatus
from ..serializers.lesson import LessonDisplaySerializer, LessonStatusSerializer, LessonSerializer

#------------------------
# Lesson View's ---------
#------------------------

# List of lessons 
class LessonList(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDisplaySerializer


# Detail of a lesson
class LessonDetail(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDisplaySerializer
    

# Create a lesson 
class LessonCreate(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


# Update a lesson
class LessonUpdate(generics.RetrieveUpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


# Delete a lesson
class LessonDelete(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


# Filter lesson by status
class LessonFilterByStatus(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDisplaySerializer

    def get_queryset(self):
        status = self.kwargs['status']
        return Lesson.objects.filter(status=status)


# Filter lesson by slug 
class LessonFilterBySlug(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDisplaySerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Lesson.objects.filter(slug=slug)


#------------------------
# Lesson Status View's --
#------------------------


# List of lesson status
class LessonStatusList(generics.ListAPIView):
    queryset = LessonStatus.objects.all()
    serializer_class = LessonStatusSerializer


# Detail of a lesson status
class LessonStatusDetail(generics.RetrieveAPIView):
    queryset = LessonStatus.objects.all()
    serializer_class = LessonStatusSerializer


# Create a lesson status
class LessonStatusCreate(generics.CreateAPIView):
    queryset = LessonStatus.objects.all()
    serializer_class = LessonStatusSerializer


# Update a lesson status
class LessonStatusUpdate(generics.RetrieveUpdateAPIView):
    queryset = LessonStatus.objects.all()
    serializer_class = LessonStatusSerializer


# Delete a lesson status
class LessonStatusDelete(generics.DestroyAPIView):
    queryset = LessonStatus.objects.all()
    serializer_class = LessonStatusSerializer

