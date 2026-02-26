# Standard Configurations
To apply the standard configurations to servers run the following playbook.  

`./standard_configurations.yml`  

This will apply the standard configuration that I have defined and install any packages that are deemed to be standard. 

Standard configuration includes:  
- User accounts
- Timezone
- SSH public keys and key only login

Standard applications includes:
- Zabbix agent
- dnsutils