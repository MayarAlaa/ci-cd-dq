import pyodbc
import pytest


@pytest.fixture(scope='module')
def connection():
    conn_str = (
        r"Driver=Sql Server;"
        r"Server=.\SQLEXPRESS;"
        r"Database=TRN;"
        r";uid=TestUser;"
        r"pwd=Test1234;"
    )
    connection = pyodbc.connect(conn_str)
    yield connection
    connection.close()


@pytest.fixture
def cursor(connection):
    cursor = connection.cursor()
    yield cursor
    connection.rollback()
