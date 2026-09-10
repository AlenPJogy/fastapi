from app import models, schemas
import pytest


def test_create_comment(authorized_client, test_posts, session, test_user):
    res = authorized_client.post(
        "/comments/", json={"comment": "This is a test comment", "post_id": test_posts[0].id, "email": test_user['email']})
    print(res.json())
    assert res.status_code == 201


def test_create_comment_non_exist_post(authorized_client, test_posts, session, test_user):
    res = authorized_client.post(
        "/comments/", json={"comment": "This is a test comment", "post_id": 1234567, "email": test_user['email']})
    assert res.status_code == 404


def test_unauthorized_user_create_comment(client, test_posts, session, test_user):
    res = client.post(
        "/comments/", json={"comment": "This is a test comment", "post_id": test_posts[0].id, "email": test_user['email']})
    assert res.status_code == 401


def test_delete_comment(authorized_client, test_posts, session, test_user):
    comment = authorized_client.post(
        "/comments/", json={"comment": "This is a test comment", "post_id": test_posts[0].id, "email": test_user['email']})
    comment_id = comment.json()["id"]
    res = authorized_client.delete(
        f"/comments/{comment_id}")
    assert res.status_code == 204
