from rest_framework import fields, serializers
from ..models import Lesson, LessonStatus

#------------------------------
# Lesson Serializer -----------
#------------------------------

# Lesson Serializer
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('__all__')

# Display Lesonn serializer
class LessonDisplaySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    status = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Lesson
        fields = ('__all__')


#------------------------------
# Lesson Status Serializer -----
#------------------------------


# Lesson Status Serializer
class LessonStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonStatus
        fields = ('__all__')


