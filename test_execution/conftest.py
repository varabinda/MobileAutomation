import pytest


@pytest.fixture(scope='module')
def fixture_module():
    print('module scope')
    yield
    print('clean up - fixture module')


@pytest.fixture(scope='package')
def fixture_package():
    print('package scope')
    yield
    print('clean up - fixture package')


@pytest.fixture(scope='session')
def fixture_session():
    print('session scope')
    yield
    print('clean up - fixture session')