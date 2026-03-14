# Netbox
Netbox is running on a stand alone server with the database colocated on the same server.  


The [installation guide](https://netboxlabs.com/docs/netbox/installation/) was followed for install. The following changes or additions have been made to the server.
- added backup script to /etc/cron.daily for the database with the backup folder `/opt/backups/netbox`  
