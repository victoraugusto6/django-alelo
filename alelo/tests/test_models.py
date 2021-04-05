import pytest

from alelo.users.models import User


def test_create_user(db):
    common_user = User.objects.create_user('victor@email.com', 'admin123')
    assert common_user.is_superuser is False
    assert common_user.email == 'victor@email.com'
    assert common_user.check_password('admin123')


def test_create_superuser(db):
    common_user = User.objects.create_superuser('victor@email.com', 'admin123')
    assert common_user.is_superuser is True
    assert common_user.email == 'victor@email.com'
    assert common_user.check_password('admin123')


def test_create_user_without_email(db):
    with pytest.raises(ValueError) as excinfo:
        User.objects.create_user(None, 'admin123')
    assert str(excinfo.value) == 'The given email must be set'


def test_create_superuser_without_email(db):
    with pytest.raises(ValueError) as excinfo:
        User.objects.create_superuser('victor@email.com', 'admin123', is_staff=False)
    assert str(excinfo.value) == 'Superuser must have is_staff=True.'


def test_create_superuser_is_superuser_false(db):
    with pytest.raises(ValueError) as excinfo:
        User.objects.create_superuser('victor@email.com', 'admin123', is_superuser=False)
    assert str(excinfo.value) == 'Superuser must have is_superuser=True.'
