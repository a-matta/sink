*** Variables ***
${REASON}    JIRA-1234
${BASE_URL}    https://dev.your-app.com

*** Test Cases ***
Simple Case
    Log To Console    Running tests for ${REASON} on ${BASE_URL}
