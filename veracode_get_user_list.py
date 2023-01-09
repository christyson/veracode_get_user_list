import sys
import requests
import argparse
import json
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC
from veracode_api_py import VeracodeAPI as vapi
headers = {"User-Agent": "Python HMAC Example"}

def main():

# test comment
    parser = argparse.ArgumentParser(
        description='This script takes a user name and generates a list of their attributes or --all will generate a list of all users and attributes.')
    parser.add_argument('-u', '--user', help='print attributes for this user',required=False)
    parser.add_argument('--all',default=False, action='store_true', help='If set to True information for all users will be generated', required=False)
    parser.add_argument('--file',default=False, action='store_true', help='If set to True information will be placed in a file called user_list.csv', required=False) 
    args = parser.parse_args()
    file_name = "user_list.csv"

    if (args.file):
        # delete old files
        f = open(file_name, 'w')
        print("user name, ip restricted, allowed ip addresses", file=f)
    if (args.user is not None):
       data = vapi().get_user_by_search(args.user)
       for user in data:
          userguid = user["user_id"]
          data2 = vapi().get_user(userguid)
          if (str(data2["ip_restricted"]) == "True"):
             usr_str = user["user_name"]+","+str(data2["ip_restricted"])+","+str(data2["allowed_ip_addresses"])
          else:
             usr_str = user["user_name"]+","+str(data2["ip_restricted"])
          if (args.file):
             print(usr_str, file=f)
          else:
             print(usr_str)
    elif (args.all):
       data = vapi().get_users()
       for user in data:
          userguid = user["user_id"]
          data2 = vapi().get_user(userguid)
          if (str(data2["ip_restricted"]) == "True"):
             usr_str = user["user_name"]+","+str(data2["ip_restricted"])+","+str(data2["allowed_ip_addresses"])
          else:
             usr_str = user["user_name"]+","+str(data2["ip_restricted"])
          if (args.file):
             print(usr_str, file=f)
          else:
             print(usr_str)
             
    else:
       print ('You must specify either --all or a user with -u, --user ')
    exit(0)

if __name__ == '__main__':
    main()
