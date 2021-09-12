from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.urls import reverse
from ...models import Lesson, LessonStatus
from model_bakery import baker
from django.contrib.auth.models import User

client = APIClient()

#-----------------------------------------------------------------------------------------------------------------------
# Test Class for Lesson API
#-----------------------------------------------------------------------------------------------------------------------

class GetAllLessonTestCase(APITestCase):
    """Getting all lesson test case"""
    def setUp(self):
        self.lesson = baker.make(Lesson, _quantity=150)
    
    def test_get_all_lesson(self):
        response = client.get(reverse('lesson_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 150)
    
class GetSingelLessonTestCase(APITestCase):
    """Get singel lesson Test Case"""
    def setUp(self):
        self.lesson = baker.make(Lesson)
    

    def test_get_single_lesson(self):
        response = client.get(reverse('lesson_detail', kwargs={'pk': self.lesson.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.lesson.pk)
    
    def test_get_single_lesson_with_invalid_id(self):
        response = client.get(reverse('lesson_detail', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateLessonTestCase(APITestCase):
    """Create Leson Test Case"""
    def setUp(self):
        self.user = baker.make(User)
        self.status = baker.make(LessonStatus, label='completed')
        self.client.force_authenticate(user=self.user)
        self.valid_data = {
            'title': 'test',
            'slug': 'test',
            'content': 'test',
            'status': self.status.pk,
            'author': self.user.pk
        }
        self.invalid_data = {
            'title': '',
            'slug': '',
            'content': '',
            'status': self.status.pk,
            'author': self.user.pk
        }
        
    def test_create_lesson_with_valid_data(self):
        response = client.post(reverse('lesson_create'), data=self.valid_data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 1)
        self.assertEqual(Lesson.objects.get().title, 'test')
    
    def test_create_lesson_with_invalid_data(self):
        response = client.post(reverse('lesson_create'), data=self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Lesson.objects.count(), 0)
    


class UpdateLessonTestCase(APITestCase):
    """Update Lesson Test Case"""
    def setUp(self):
        self.user = baker.make(User)
        self.status = baker.make(LessonStatus, label='completed')
        self.lesson = baker.make(Lesson, title='test', slug='test', content='test', status=self.status, author=self.user)
        self.client.force_authenticate(user=self.user)
        self.valid_data = {
            'title': 'test',
            'slug': 'test',
            'content': 'test',
            'status': self.status.pk,
            'author': self.user.pk
        }
        self.invalid_data = {
            'title': '',
            'slug': '',
            'content': '',
            'status': self.status.pk,
            'author': self.user.pk
        }
    
    def test_update_lesson_with_valid_data(self):
        response = client.put(reverse('lesson_update', kwargs={'pk': self.lesson.pk}), data=self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.get().title, 'test')
    
    def test_update_lesson_with_invalid_data(self):
        response = client.put(reverse('lesson_update', kwargs={'pk': self.lesson.pk}), data=self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Lesson.objects.get().title, 'test')
    


class DeleteLessonTestCase(APITestCase):
    """Delete Lesson Test Case"""
    def setUp(self):
        self.user = baker.make(User)
        self.status = baker.make(LessonStatus, label='completed')
        self.lesson = baker.make(Lesson, title='test', slug='test', content='test', status=self.status, author=self.user)
        self.client.force_authenticate(user=self.user)
    
    def test_delete_lesson(self):
        response = client.delete(reverse('lesson_delete', kwargs={'pk': self.lesson.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.count(), 0)
    

# Todo the test case for the lesson filter by status
# class FilterLessonTestCase(APITestCase):
#     """Filter Lesson Test Case"""
#     def setUp(self):
#         self.user = baker.make(User)
#         self.status = baker.make(LessonStatus, label='completed')
#         self.lesson = baker.make(Lesson, title='test', slug='test', content='test', status=self.status, author=self.user)
#         self.client.force_authenticate(user=self.user)
    
#     def test_filter_lesson_by_title(self):
#         response = client.get(reverse('lesson_filter_by_title'), data={'title': 'test'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['count'], 1)
    
#     def test_filter_lesson_by_slug(self):
#         response = client.get(reverse('lesson_filter_by_slug'), data={'slug': 'test'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


#--------------------------------------------------------------------------------------------------------------------
# Lesson Status Test Case
#--------------------------------------------------------------------------------------------------------------------


class GetAllLessonStatusTestCase(APITestCase):
    """Get All Lesson Status Test Case"""
    def setUp(self):
        self.status = baker.make(LessonStatus, _quantity=50)
    
    def test_get_all_lesson_status(self):
        response = client.get(reverse('lesson_status_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 50)
    


class GetLessonStatusTestCase(APITestCase):
    """Get Lesson Status Test Case"""
    def setUp(self):
        self.status = baker.make(LessonStatus)
    
    def test_get_lesson_status(self):
        response = client.get(reverse('lesson_status_detail', kwargs={'pk': self.status.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    


class CreateLessonStatusTestCase(APITestCase):
    """Create Lesson Status Test Case"""
    def setUp(self):
        self.valid_data = {
            'label': 'completed'
        }
        self.invalid_data = {
            'label': ''
        }
    
    def test_create_lesson_status_with_valid_data(self):
        response = client.post(reverse('lesson_status_create'), data=self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(LessonStatus.objects.count(), 1)
        self.assertEqual(LessonStatus.objects.get().label, 'completed')
    
    def test_create_lesson_status_with_invalid_data(self):
        response = client.post(reverse('lesson_status_create'), data=self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(LessonStatus.objects.count(), 0)




class UpdateLessonStatusTestCase(APITestCase):
    """Update Lesson Status Test Case"""
    def setUp(self):
        self.user = baker.make(User)
        self.status = baker.make(LessonStatus, label='completed')
        self.valid_data = {
            'label': 'completed'
        }
        self.invalid_data = {
            'label': ''
        }
    
    def test_update_lesson_status_with_valid_data(self):
        response = client.put(reverse('lesson_status_update', kwargs={'pk': self.status.pk}), data=self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(LessonStatus.objects.get().label, 'completed')
    
    def test_update_lesson_status_with_invalid_data(self):
        response = client.put(reverse('lesson_status_update', kwargs={'pk': self.status.pk}), data=self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(LessonStatus.objects.get().label, 'completed')




class DeleteLessonStatusTestCase(APITestCase):
    """Delete Lesson Status Test Case"""
    def setUp(self):
        self.user = baker.make(User)
        self.status = baker.make(LessonStatus, label='completed')
        self.client.force_authenticate(user=self.user)
    
    def test_delete_lesson_status(self):
        response = client.delete(reverse('lesson_status_delete', kwargs={'pk': self.status.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(LessonStatus.objects.count(), 0)
