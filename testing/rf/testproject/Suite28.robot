*** Variables ***
${val1}           value
@{listVal1}       abc    def    123

*** Test Cases ***
Case281
    log    ${val1}
    log many    @{listVal1}
    log    %{JAVA_HOME}
    ${shuzhi}    Set Variable    ${2.6}    2.6

Case282
    ${val2}    Set Variable    abcd
    ${valif2}    Set Variable If    '${val2}'=='abcd'    efgh    ace
    ${getVal1}    Get Length    ${val2}
    ${getVal2}    GET Time
    log    ${val1}
    Run Keyword If    '${val2}'=='abcd'    log    efgh
    log    12340${val2}efgh
    log    ${val2[2]}
    log    ${val2[0:3]}
    ${cal1}    Set Variable    123
    ${cal2}    Evaluate    ${cal1}+1
    ${cal1}    Set Variable    '123'
    ${cal2}    Evaluate    int(${cal1})+1
