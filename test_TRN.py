import string

from exceptiongroup import catch

from connection import *


# get percentage of passed records per test case
def get_result_by_percentage(corrupted_records_amount: int, overall_records_amount: int, description: str) -> bool:
    print(description + " = %" + str(
        round(((overall_records_amount - corrupted_records_amount) / overall_records_amount) * 100,2)))
    if corrupted_records_amount / overall_records_amount > 0:
        return False
    return True
    pass


# function to find records with null or empty values
def verify_completeness(records: list) -> bool:
    records_amount_with_empty_values = 0
    for record in records:
        if record[0] == '0':
            records_amount_with_empty_values = records_amount_with_empty_values + 1

    return get_result_by_percentage(records_amount_with_empty_values, len(records), "Percentage of completed records")


# function to find records with value length more than expected
def verify_max_length(records: list, max_length: int):
    records_amount_with_values_more_than_max_length = 0

    for record in records:
        if len(record[0]) > max_length:
            records_amount_with_values_more_than_max_length = records_amount_with_values_more_than_max_length + 1

    return get_result_by_percentage(records_amount_with_values_more_than_max_length, len(records),
                                    f"Percentage of records with length less than or equal {max_length}")



# function to find records with value more than expected
def verify_max_value(records: list, max_value: int):
    records_amount_with_values_more_than_max_value = 0

    for record in records:
        if record[0] > max_value:
            records_amount_with_values_more_than_max_value = records_amount_with_values_more_than_max_value + 1

    return get_result_by_percentage(records_amount_with_values_more_than_max_value, len(records),
                                    f"Percentage of records with length less than or equal {max_value}")


# function to find records with dependents counts more than expected
def verify_allowed_dependents_count(records: list, max_value: int):
    records_amount_with_values_more_than_max_dep_cnt = 0

    for record in records:
        if record[1] > max_value:
            records_amount_with_values_more_than_max_dep_cnt = records_amount_with_values_more_than_max_dep_cnt + 1

    return get_result_by_percentage(records_amount_with_values_more_than_max_dep_cnt, len(records),
                                    f"Percentage of records with length less than or equal {max_value}")


# implement function to find records with non allowed values
def verify_allowed_values(records: list, allowed_values: list):
    records_amount_with_not_allowed_values = 0
    for record in records:
        if record[0] not in allowed_values:
            records_amount_with_not_allowed_values = records_amount_with_not_allowed_values + 1
    return get_result_by_percentage(records_amount_with_not_allowed_values, len(records),
                                    f"Percentage of records with allowed values ({allowed_values})")


# function to verify datatype
def verify_datatype(records: list, data_types: list):
    columns_with_incorrect_datatype= 0
    for i in range(len(data_types)):
        if records[i][0] != data_types[i]:
            columns_with_incorrect_datatype = columns_with_incorrect_datatype + 1


    return get_result_by_percentage(columns_with_incorrect_datatype, len(records),
                                    f"Percentage of columns with correct datatype: ")

# Table: hr.jobs: Verify max length for column[job_title] <= 35
def test_verify_max_length(cursor):
   
     cursor.execute('select job_title from hr.jobss')
     rs = cursor.fetchall()

     assert verify_max_length(rs, 35)

    


# Table: hr.jobs: Verify max value for column[max_salary] = 40000
def test_verify_max_value(cursor):
    try:
     cursor.execute('select max_salary from hr.jobs')
     rs = cursor.fetchall()

     assert verify_max_value(rs, 40000)

    except :
     print("Test Failed")


#Table: hr.dependents: Verify that employee_id is in required range of values
def test_verify_allowed_values(cursor):
    try:
     cursor.execute('select employee_id from hr.dependents')
     rs = cursor.fetchall()
     cursor.execute('select distinct employee_id from hr.employees')
     allowed_values = cursor.fetchall()
     assert verify_allowed_values(rs, allowed_values)

    except :
     print("Test Failed")

#Table: hr.dependents: Verify that each employee is allowed max 1 Child
def test_verify_allowed_dependents_count(cursor):
    try:
     cursor.execute(' select employee_id , count(*) as Child_Count from hr.dependents group by employee_id')
     rs = cursor.fetchall()
     assert verify_allowed_dependents_count(rs,1)

    except :
     print("Test Failed")

#Table: hr.locations: Verify completeness for column postal_code.
def test_verify_completeness(cursor):
    try:
     cursor.execute('select coalesce(postal_code,\'0\') from hr.locations ')
     rs = cursor.fetchall()
     print(rs)
     assert verify_completeness(rs)

    except :
     print("Test Failed")


# Table: hr.locations: Verify that datatypes of all columns
def test_verify_datatype(cursor):
    try:
     cursor.execute('SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where table_NAME = \'locations\'')
     rs = cursor.fetchall()
     allowed_datatypes = ["int", "varchar", "varchar", "varchar", "varchar", "char"]
     assert verify_datatype(rs, allowed_datatypes)

    except :
     print("Test Failed")
