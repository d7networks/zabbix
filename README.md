# Zabbix SMS Plugin

Zabbix SMS notification via D7SMS allows to sending of worldwide SMS notifications for each host and service. 

For FREE sms credits signup at https://d7networks.com. 

We used a Python script for sending SMS notifications in the Zabbix platform using D7SMS gateway.

## Getting Started
These instructions will get you a copy of the script and configuration guidelines for setting it up in Zabbix

### Prerequisites
- D7SMS Subscription

     Sign up at https://d7networks.com for subscription and FREE SMS credits. 

### Zabbix Setup


- Get "AlertScriptsPath" of Zabbix setup from `zabbix_server.conf` (also you can get the default path from the following command) and navigate to same.
- Default AlertScriptsPath is: /usr/lib/zabbix/alertscripts

![Get Script Path](https://d7networks.com/images/zabbix/Get-script-path.gif)


```
     zabbix_server --help | grep AlertScriptsPath
     or
     cat /etc/zabbix/zabbix_server.conf | grep "AlertScriptsPath"
      
```
  
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
- Click on Message templates tab on the same window and click `add`.

     Select Message type as `Problem`, and you will get a predefined script. Click on `add`.

- Now add one more template for Recovery.

     Select Message type `Problem Recovery` and click `add`.

     Click on `Update` once you've added all the templates. 

- Once created media type, Goto Users and click on the desired User

     Then select the Media tab and click on `Add`

```
     Choose Type: D7SMS
     Add destination number with country code for the option `Send to`
     Select the type of alert (severity) required and `enable` it. 
```

- Click on Update and the alerts will be generated. 

- Also, you can check the /var/log/zabbix directory for logs in case if you need to check for errors

### Support and Update 

You can get the latest version of this script from Github: https://github.com/d7networks/zabbix

For all queries and help with installation please contact support@d7networks.com
