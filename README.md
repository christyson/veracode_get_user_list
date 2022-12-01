# Veracode Get User List of allowed IPs

A simple example script to generate a list of users and if enabled the IP Ranges they can login from.

## Setup

Clone this repository:

    git clone https://github.com/christyson/veracode_get_user_list.git

Install dependencies:

    cd veracode_get_user_list
    pip install -r requirements.txt

(Optional) Save Veracode API credentials in `~/.veracode/credentials`

    [default]
    veracode_api_key_id = <YOUR_API_KEY_ID>
    veracode_api_key_secret = <YOUR_API_KEY_SECRET>

## usage for a single app profile or and app profile with a sandbox

usage: veracode_get_user_list.py [-h] [-u USER] [--all] [--file]

This script takes a user name and generates a list of their attributes or --all will generate a list of all users and
attributes.

options:
  -h, --help            show this help message and exit
  -u USER, --user USER  print attributes for this user
  --all                 If set to True information for all users will be generated
  --file                If set to True information will be placed in a file called user_list.csv

## Run

If you have saved credentials as above you can run:

    python veracode_get_user_list.py -u <your user of interest>

	or 
	
	python veracode_get_user_list.py --all

Otherwise you will need to set environment variables before running `veracode_get_user_list.py`:

    export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
    export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>
    python veracode_get_user_list.py -u <your user of interest>
	
	or 
	
	python veracode_get_user_list.py --all
	

Both of these methods can also have the --file option added and then the results will be stored in a file called "user_list.csv"

If the app is not found an error message will be printed.
