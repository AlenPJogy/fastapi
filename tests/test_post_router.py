from datetime import datetime, timezone

from app import models
from app.routers.post import postout


def test_postout_handles_single_row():
    owner = models.User(
        id=1,
        email="user@example.com",
        password="secret",
        created_at=datetime.now(timezone.utc),
    )
    post = models.Post(
        id=1,
        title="Test title",
        content="Test content",
        published=True,
        created_at=datetime.now(timezone.utc),
        owner_id=1,
        owner=owner,
    )

    result = postout((post, 2))

    assert result.Post.id == 1
    assert result.vote == 2
