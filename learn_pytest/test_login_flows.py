import pytest

class TestLoginFlows:

    @pytest.fixture()
    def register_user(self):
        print('Register user successful')
        yield
        print('clean up in register fixture')

    @pytest.fixture()
    def login_with_user_password(self, register_user):
        print('Logging in')
        assert 1 == 1, 'Logging in failed'
        yield
        print('clean up in login fixture')

    def test_v2_logout(self, login_with_user_password):
        print('Logging out')
        assert 1 == 1, 'Logout failed'







