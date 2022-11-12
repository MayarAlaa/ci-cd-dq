# ci-cd-dq
Basic testing of data from TRN database using PyTest framework.

The chosen merging strategy is GitHub Flow. The repository holds 2 types of branches: main and features. As per the project requirements, the release frequency is periodic and service preferences is open source. The number of the team is not large so having every approved PR deployed to production first won't be a huge blocker.


# Screenshots:
## Dockerfile
<img width="684" alt="Screenshot_10" src="https://user-images.githubusercontent.com/18288755/201496947-7a1e2bd8-26d9-4ea3-bc3b-0eb99a68fbcc.png">


## Jenkins Pipeline configuration:
<img width="909" alt="Jenkins Config1" src="https://user-images.githubusercontent.com/18288755/201496873-de00b6ae-93b8-4b6c-a6a6-34acb05e5cec.png">
<img width="956" alt="Jenkins Config 2" src="https://user-images.githubusercontent.com/18288755/201496875-dd98ffec-4d2c-472a-a286-e24c05f52ca2.png">


## Example of creating a new file 'commit-example' on branch 'feature-test-merge'

<img width="681" alt="commit example" src="https://user-images.githubusercontent.com/18288755/201496832-16b8bc45-3e06-4969-afc3-6dd710f8509b.png">

## Pipeline Run Results:
<img width="673" alt="pipeline-stages-success" src="https://user-images.githubusercontent.com/18288755/201496912-2508ff98-7896-423e-9eb0-6ea3011edbf2.png">

## After successful merge:
<img width="675" alt="merge to main" src="https://user-images.githubusercontent.com/18288755/201496865-444acc9e-70f2-44bc-92bd-b934b914b604.png">
