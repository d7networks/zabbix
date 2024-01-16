# Zabbix SMS Plugin

Zabbix SMS notification via D7SMS allows to send worldwide SMS notifications for each hosts and services. 

For FREE sms credits signup at https://d7networks.com. 

We used Python script for sending SMS notifications in zabbix platfrom using D7SMS gateway.

## Getting Started
These instructions will get you a copy of the script and configuration guidelines for setting it up in Zabbix

### Prerequisites
- D7SMS Subscription

     Signup at https://d7networks.com for subscription and FREE sms credits. 

### Zabbix Setup


- Get "AlertScriptsPath" of zabbix setup from zabbix_server.conf and navigate to same. 

      Default AlertScriptsPath is /usr/lib/zabbix/alertscripts
- Download D7SMS script from [here](https://raw.githubusercontent.com/d7networks/zabbix/master/d7sms.py) and make it executable
```
cd /usr/lib/zabbix/alertscripts
wget https://raw.githubusercontent.com/d7networks/zabbix/master/d7sms.py
chmod +x /usr/lib/zabbix/alertscripts/d7sms.py
```
- Replace the "D7TOKEN" in the script with the token you obtained from https://app.d7networks.com/api-tokens.
```
vim /usr/lib/zabbix/alertscripts/d7sms.py +7

Update line number 7 
    D7TOKEN = "eyJhbGciOiJIUzI1NiIsInR......."
```

- Open Zabbix panel and navigate to Alerts > Media Types and click on `Create media` type and input following details

```
Name:D7SMS
    Type:Script
    Script name:d7sms.py
    Script parameters
        {ALERT.SENDTO}
        {ALERT.MESSAGE}
```
- Click on Message templates tab on the same window and click add 
    Select Message type as `Problem`, and you will get a predefined script. Click on add 
    Now add one more template for Recovery
    Select Message type `Problem Recovery` and click add 
    Click on Update once you've added all the templates. 

- Once created media type, Goto Users and click on the desired User
    Then select the Media tab and click on Add

```
Choose Type: D7SMS
Add destaination number with country code for option "Send to"
Select type of alerts (severity) required and enable it. 

```

Click on Update and the alerts will be generated. Also you can check the /var/log/zabbix directory for logs incase if you need to check for errors
    
You can get the latest version of this script from GUTHUB : https://github.com/d7networks/zabbix

For all queries and help on installation please contact zabbix@d7networks.com
