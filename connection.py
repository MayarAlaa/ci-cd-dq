import pymssql
import pytest


@pytest.fixture(scope='module')
def connection():
    connection = pymssql.connect(server='EPPLKRAW04C0\\SQLEXPRESS', user='TestUser', password='Test1234', database='TRN')
    yield connection
    connection.close()


@pytest.fixture
def cursor(connection):
    cursor = connection.cursor()
    yield cursor
    connection.rollback()
