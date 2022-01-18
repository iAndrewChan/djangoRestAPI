import pytest
from django.contrib.auth import get_user_model


class TestUserModel:

    # https://pytest-django.readthedocs.io/en/latest/database.html
    @pytest.mark.django_db
    @pytest.mark.parametrize("password", ["test123", "test"])
    def test_create_user_successful(self, password):
        """Test creating a new user with an email is successful"""
        # when
        # We are able to familiarise with an API by looking at the test
        # seeing what we need to provide to the arguments and check that the API call has
        # the expected behaviour
        # models.py::UserManager::create_user is what defines this API
        user = get_user_model().objects.create_user(password)

        assert user.employee_id
        assert user.check_password(password)

    @pytest.mark.django_db
    @pytest.mark.parametrize(
        "password, expected_exception_message",
        [
            (None, "User must have a password set"),
            ("tes", "User password must have at least 4 characters"),
        ],
    )
    def test_create_user_with_password_exceptions(
        self, password, expected_exception_message
    ):
        """Test creating a new user with None password"""

        with pytest.raises(ValueError) as e:
            get_user_model().objects.create_user(password)

        assert str(e.value) == expected_exception_message

    @pytest.mark.django_db
    def test_create_superuser_success(self):
        """Test creating a new super user"""
        email = "email"
        password = "password"

        superuser = get_user_model().objects.create_superuser(email, password)
        assert superuser.email == email
        assert superuser.check_password(password)
        assert superuser.is_superuser

    @pytest.mark.django_db
    @pytest.mark.parametrize(
        "email, password, expected_exception_message",
        [
            (None, None, "Superuser must have an email"),
            ("email", None, "Superuser must have a password set"),
            ("email", "tes", "Superuser password must have at least 4 characters"),
        ],
    )
    def test_create_superuser_unsuccessful(
        self, email, password, expected_exception_message
    ):
        """Test creating a new super user unsuccessfully"""

        with pytest.raises(ValueError) as e:
            get_user_model().objects.create_superuser(email, password)

        assert str(e.value) == expected_exception_message
