from django.contrib.auth import get_user_model
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import TestCase

from notes.models import Task, Note

class TestTask(TestCase):

    @classmethod 
    def setUpTestData(cls):
        user = get_user_model().objects.create_user(username="test", password="pass")
        user.save()
        newTask = Task.objects.create(
            user = user,
            title = "Workout",
            message = "Legs Day",
            date = "2021-12-23",
            time = "23:27:00",
        )
        newTask.save()
        newNote = Note.objects.create(
            user = user,
            title = "New Note",
            message = "Study",
            date = "2021-12-15T19:58:24.789181Z",

        )



    def test_task_str(self):
        task = Task.objects.get(id = 1)
        self.assertEqual(str(task.title), "Workout")

    def test_task_content(self):
        task = Task.objects.get(id=1)
        self.assertEqual(task.title,'Workout')
        self.assertEqual(task.message,'Legs Day')
        

    def test_note_content(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.title,'New Note')
        self.assertEqual(note.message,'Study')
        

class APITest(APITestCase):


############ Task features tests ###############

    def test_task_list(self):

        response = self.client.get(reverse("task_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_task_detail(self):

        test_user = get_user_model().objects.create_user(
            username="test", password="pass"
        )
        test_user.save()

        test_task = Task.objects.create(
            id = 1,
            title = "Workout",
            message = "Legs Day",
            date = "2021-12-23",
            time = "23:27:00",
        )
        test_task.save()

        response = self.client.get(reverse("task_detail", args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": 1,
                "title": test_task.title,
                "message": test_task.message,
                "date": test_task.date,
                "time": test_task.time,
                "user": test_task.user,

            },
        )

    def test_task_update(self):

        test_user = get_user_model().objects.create_user(
            username="test", password="pass"
        )
        test_user.save()

        test_task = Task.objects.create(
            title = "Workout",
            message = "Legs Day",
            date = "2021-12-23",
            time = "23:27:00",
        )

        test_task.save()

        url = reverse("task_detail", args=[test_task.id])
        data = {
                "id": 1,
                "title": "Shopping",
                "message": "Groceries",
                "date": "2021-12-25",
                "time": "23:27:30",
        }

        self.client.login(username="test", password="pass")
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, url)
        self.assertEqual(Task.objects.count(), test_task.id)
        self.assertEqual(Task.objects.get().id, data["id"])

    def test_task_delete(self):

        test_user = get_user_model().objects.create_user(
            username="test", password="pass"
        )
        test_user.save()

        test_task = Task.objects.create(
            title = "Workout",
            message = "Legs Day",
            date = "2021-12-23",
            time = "23:27:00",
        )

        test_task.save()

        task = Task.objects.get()
        url = reverse("task_detail", kwargs={"pk": task.id})
        self.client.login(username="tester", password="pass")
        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)

######### Notes feature tests ########

    def test_notes_list(self):

        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_notes_detail(self):

        test_user = get_user_model().objects.create_user(
            username="test", password="pass"
        )
        test_user.save()

        test_note = Note.objects.create(
            id = 1,
            title = "New Note",
            message = "Study",
            date = "2021-12-15T19:58:24.789181Z",
        )
        test_note.save()

        response = self.client.get(reverse("note_detail", args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": 1,
                "title": test_note.title,
                "message": test_note.message,
                "date": test_note.date,
                "user": test_note.user,

            },
        )

    



