import pytest
from app.models import User


def test_organization_is_created(test_db):
    user = User(name="John Doe")
    test_db.session.add(user)
    test_db.session.commit()
    assert user.id == 1
