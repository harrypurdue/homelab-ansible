# DNS Servers
There are four DNS servers. Two in `production` and two in `dev`. There are currently two DNS zones, `lab.lan` and `dev.lab.lan`.  

To install, and configure (including dns records) run the following playbook
`./dns_servers.yml`

Use the following tags to limit the action performed  
`install`  
`config`  
`records`  
