"""functions for adding/updating, deleting, syncing fqdns from ipam with the configuration context in netbox used by dns servers"""
import pynetbox
import requests
import os
import re

default_domain = "lab.lan"
default_dns_config_context = "dns_records"

def init_netbox_api(netbox_api = None, netbox_token = None, session = None):
    if netbox_api is None: netbox_api =  os.environ.get("NETBOX_API")
    if netbox_token is None: netbox_token = os.environ.get("NETBOX_TOKEN")

    # creating a requests session to use that will trust my ca root
    if session is None:
        session = requests.Session()
        session.verify = "/mnt/x/homelab/keys and certs/certs/ca-02/homelab_root_ca.pem"

    nb = pynetbox.api(netbox_api, netbox_token, threading = True, strict_filters = True)
    nb.http_session = session

    return nb

def get_config_context(name = default_dns_config_context):
    nb = init_netbox_api()
    return nb.extras.config_contexts.get(name = name)

def update_from_ipam():
    raise NotImplementedError("update_from_ipam is not implemented")
    nb = init_netbox_api()
    config_context = get_config_context()

    records_from_ipam = {"domains" : {}}
    for x in nb.ipam.ip_addresses.filter(dns_name__empty = False):
        match = prog.match(x.dns_name)
        domain_name = match.group(2).removeprefix(".")

        if not records_from_ipam["domains"].get(domain_name):
            records_from_ipam["domains"].update({domain_name : {}})
        records_from_ipam["domains"][domain_name].update({
                match.group(1) : {
                "type" : "A",
                "value" : x.address.rsplit("/")[0] # removing cidr notation
        }})

    # update the config context for each domain listed
    for domain in records_from_ipam["domains"]:
        if config_context.data["domains"].get(domain):
            config_context.data["domains"][domain].update(records_from_ipam["domains"][domain])

    # push to netbox
    config_context.save()

def delete(args):
    """delete a dns record from the dns record config context"""
    host = args.host
    config_context = get_config_context()
    

    if config_context.data.get("domains").get(default_domain).get(host):
        del config_context.data["domains"][default_domain][host]
        config_context.save()
    else:
        print(f"Error: {host} not found.")

def add(args):
    """add or update a dns record to the dns record config context"""
    name, value, record_type = args.host, args.value, args.type
    config_context = get_config_context()

    if config_context.data.get("domains").get(default_domain):
        config_context.data["domains"][default_domain][name] = {"value" : value, "type" : record_type}
        config_context.save()
    else:
        print(f"Error: {default_domain} not found in config context.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    # parser.add_argument("--domain-name", required = False, help = "domain name for records", default = default_domain)

    subparsers = parser.add_subparsers()

    add_subparser = subparsers.add_parser("add")
    add_subparser.set_defaults(func = add)

    delete_subparser = subparsers.add_parser("delete", aliases = ["del"])
    delete_subparser.set_defaults(func = delete)

    # sync_subparser = subparsers.add_parser("sync")

    add_subparser.add_argument(dest = "host", help = "node to add")
    add_subparser.add_argument(dest = "value", help = "value of dns record for node")
    add_subparser.add_argument("-t", required = False, dest = "type", help = "type of dns record default: A", default = "A", choices = ["A", "CNAME"])

    delete_subparser.add_argument(dest = "host", help = "node to delete")

    args = parser.parse_args()
    args.func(args)
