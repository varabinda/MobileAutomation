import pytest


@pytest.fixture(scope='function')
def fixture_function():
    print('function scope')
    yield
    print('clean up - fixture function')


@pytest.fixture(scope='class')
def fixture_class():
    print('class scope')
    yield
    print('clean up - fixture class')


def test_three(fixture_module, fixture_session, fixture_function, fixture_package):
    print('test three')


class TestFixtureScope:

    def test_one(self, fixture_module, fixture_session, fixture_function, fixture_class, fixture_package):
        print('test one')

    def test_tow(self, fixture_module, fixture_session, fixture_function, fixture_class, fixture_package):
        print('test tow')
