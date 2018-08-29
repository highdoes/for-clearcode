*** Settings ***
Documentation    Suite description
Library   Collections


*** Variables ***
@{ALARMS}=  'Vendor BTS certificate'  'Synchronization lost'  'Diagnostic Files collected'  BTS booted at .*? due to trs management reset   'BTS booted at .*? due to trs power-on reset'     '.*? ToP master service .*? unusable'    'Failure in connection between BTS and iOMS or 3rd party tool'
@{out_alarm_list}=  'Vendor BTS certificate'  'Vendor BTS certificate'  'Vendor BTS certificate'  'Vendor BTS certificate'  'BTS booted at 12 due to trs power-on reset'
*** Test Cases ***
Test title
   Ims2 Alarms Get All And Check If Allowed


*** Keywords ***
Ims2 Alarms Get All And Check If Allowed
    ${lenght}=     get length    ${out_alarm_list}
    Run Keyword If       ${lenght}== 0    pass execution   No alarms found
    :FOR    ${element}     IN    @{out_alarm_list}
    \     List Should Contain Value    ${ALARMS}    ${element}