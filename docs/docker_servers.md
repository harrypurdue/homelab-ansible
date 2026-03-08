# Docker Servers
There are multiple docker servers in the homelab.  

There are currently two different applications hosted by the docker servers

[Netbox](netbox_docker.md)  
`ejbca`  

All servers that are in the `docker` or `cert_auth` groups will have docker installed.

Servers in the `cert_auth` group will have `ejbca` installed.

Servers in the `docker` group and have `netbox_docker` defined and `true` will have netbox installed.



