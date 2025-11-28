*** Settings ***
Variables    ../resource/variables.py

*** Variables ***
${REASON}    JIRA-1234

*** Test Cases ***
Simple Case
    Log To Console    Running tests for ${REASON} on ${BASE_URL}
