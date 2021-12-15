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








