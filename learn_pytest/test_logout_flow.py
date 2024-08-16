import pytest


class TestLoginFlow:
    @pytest.fixture
    def register_user(self):
        print('Register user successful')
        yield
        print('Deregister user successful')

    @pytest.fixture
    def login_user(self, register_user):
        print('User login successful')
        yield
        print('Clean up in login user')

    def test_user_logout(self, login_user):
        print('User logout successful')
        assert 1 == 2
