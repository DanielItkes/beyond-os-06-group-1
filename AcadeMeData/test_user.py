import pytest
from AcadeMeData.models import User


@pytest.fixture
def user_example():
    user_data = {'username': "username", 'password': "password", 'email': "user@example.com",
                 'university': "RU", 'degree': "CS"}
    user = User.create_user(*user_data)
    return user


@pytest.mark.django_db
class TestUserModel:
    def test_create_user(self, user_example):
        user = User.get_user('username')
        assert user.get_username() == user_example.user.username
        assert user.email == user_example.user.email
        assert user.password == user_example.user.password

    def test_del_user(self, user_example):
        assert User.del_user(user_example)
        user = User.get_user('username')
        assert user is None

    def test_get_user(self, user_example):
        assert User.get_user('username') == user_example.user
