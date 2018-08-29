import re



ALARMS =  ['Vendor BTS certificate' , 'Synchronization lost',  'Diagnostic Files collected' , "BTS booted at .*? due to trs management reset",  'BTS booted at .*? due to trs power-on reset' ,    '.*? ToP master service .*? unusable',    'Failure in connection between BTS and iOMS or 3rd party tool']
out_alarm_list =  [ 'BTS booted at 12 due to trs power-on reset','Vendor BTS certificate',  'Vendor BTS certificate',  'Vendor BTS certificate' , 'Vendor BTS certificate', 'dupa']


lista = out_alarm_list.copy()

for x in lista:
    for alarm in ALARMS:
        regex = re.compile(alarm)
        match = re.findall(regex, x)
        if len(match):
            out_alarm_list.remove(x)
if len(out_alarm_list) != 0:
    print("Unknown errors found: {}".format(out_alarm_list))
else:
    print("Cool")

