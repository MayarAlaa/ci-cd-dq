*** Settings ***
Library  DatabaseLibrary

*** Variables ***
${DBName}  TRN
${DBUser}  TestUser
${DBPassword}  Test1234
${DBHost}  localhost
${DBPort}  61176

*** Keywords ***
Connect DB
    Connect To Database  pymssql  ${DBName}  ${DBUser}  ${DBPassword}  ${DBHost}  ${DBPort}

Disconnect DB
    Disconnect From Database

*** Test Cases ***
Verify uniquness of table [countries] in database [TRN]
    [documentation]  This test case verifies whether countries table has duplicates or not
    Connect DB
    Row Count Is 0    selectStatement=select country_id,region_id,count(*) from hr.countries group by country_id,region_id having count(*) > 1


Check values for columns which are not accepting null values
    [documentation]  This test case verifies that non nullable columns are not null
    Connect DB
    Row Count Is 0   selectStatement=select * from hr.countries where country_id is null or region_id is null


Verify Data Insertion in Table regions
    [documentation]  This test case verifies that user is able to insert data in the table regions successfully
    Connect DB
    ${output}=  Execute SQL Script  C:/Resources/DBScripts/insert.sql
    Should Be Equal As Strings  ${output}  None


Verify maximum length of column region_name is 25
    [documentation]  This test case verifies that maximum length of column region_name is 25
    Connect DB
    Row Count Is 0   selectStatement=select * from hr.regions where len(region_name) > 25


Verify that there are no orphan records in departments table
    [documentation]  This test case verifies that all location_id in departments table already exist in locations table
    Connect DB
    Row Count Is 0   selectStatement=select dep.location_id from hr.departments as dep left join hr.locations as loc on dep.location_id = loc.location_id where loc.location_id is null


Verify Data Update in in departments table
    [documentation]  This test case verifies a user can Update a record in departments table successfully
    ${output}=  Execute SQL String  UPDATE hr.departments SET department_name = 'Happiness' WHERE department_id=1
    Should Be Equal As Strings  ${output}  None