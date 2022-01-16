import pytest
from django.contrib.auth import get_user_model

class TestUserModel:

    # https://pytest-django.readthedocs.io/en/latest/database.html
    @pytest.mark.django_db
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        # given
        username = 'testuser'
        email = 'test@email.com'
        password = 'test123'
        # when
        # We are able to familiarise with an API by looking at the test
        # seeing what we need to provide to the arguments and check that the API call has
        # the expected behaviour
        user = get_user_model().objects.create_user(
            username,
            email,
            password
        )

        assert user.username == username
        assert user.email == email
        assert user.check_password(password)
