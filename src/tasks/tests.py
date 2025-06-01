import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from tasks.models import Task


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username="testuser", email="test@example.com", password="testpass"
    )


@pytest.fixture
def client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def task(user):
    return Task.objects.create(
        user=user, title="Test Task", description="Test description"
    )


def test_create_task(client):
    url = reverse("task-list")
    data = {
        "title": "New Task",
        "description": "Do something important",
        "completed": False,
    }
    response = client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Task.objects.filter(title="New Task").exists()


def test_list_tasks(client, task):
    url = reverse("task-list")
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) >= 1  # с учётом пагинации


def test_update_task(client, task):
    url = reverse("task-detail", kwargs={"pk": task.pk})
    data = {"title": "Updated Title"}
    response = client.patch(url, data, format="json")

    assert response.status_code == status.HTTP_200_OK
    task.refresh_from_db()
    assert task.title == "Updated Title"


def test_delete_task(client, task):
    url = reverse("task-detail", kwargs={"pk": task.pk})
    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Task.objects.filter(pk=task.pk).exists()
