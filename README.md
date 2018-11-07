# Zabbix SMS Plugin

Python script for sending SMS notifications in zabbix platfrom using direct7 sms gateway.

## Getting Started
These instructions will get you a copy of the script and configuration guidelines for setting it up in zabbix

## Prerequisites


#### D7SMS Subscription
please contact support@d7networks.com or http://sms.d7networks.com for subscription. 


### Zabbix Setup


Visit https://github.com/d7networks/zabbix for latest version of D7SMS for Zabbix.

Get "AlertScriptsPath" of zabbix setup from zabbix_server.conf
Download the script to same directory and make it executable

Update USER and PASS inside the script with the credentials recieved from  http://sms.d7networks.com

Open Zabbix panel and go to Administration > Media Types and click on Create media type and input following details



```
Name:D7SMS
    Type:Script
    Script name:d7sms.py
    Script parameters
        {ALERT.SENDTO}
        {ALERT.MESSAGE}
```

Once created media type, Goto Administration > Users click on the desired User > Media and click on Add


Enter Mobile number with international prefix at "Send to" option
    Select type of alerts (severity) required and enable it. 
    
    
You can get the latest version of this script from GUTHUB : https://github.com/d7networks/zabbix
For all queries and help on installation please contact support@d7networks.com