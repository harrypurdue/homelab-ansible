# Updates
Updates can be run on all machines in the environment or using tags.  
`tags_prod` or `tags_dev`  

A proxmox snapshot is taken before updates and if the update task fails, the virtual machine is reverted to the snapshot.  

Updates are usually ran on the dev environment first and then production.  
`ansible-playbook updates.yml -t tags_dev`  
`ansible-playbook updates.yml -t tags_prod`  