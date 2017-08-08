*** Settings ***
Resource          NewResource.robot

*** Keywords ***
random char
    [Arguments]    ${arg1}    ${arg2}=123    @{arg3}
    log    ${arg1}
    log    ${arg2}
    log    =@{arg3}=
