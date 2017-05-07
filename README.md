# kindercontrol
A command-line tool that enables/disables pfSense rules

## Requirements
### Script Host
The script is designed to run on a host separate to the firewall. It was developed on macOS Sierra with python3 installed via HomeBrew.

### pfSense Firewall
Requires:
- pfSense 2.3 or greater.
- FauxAPI (https://github.com/ndejong/pfsense_fauxapi)

## Usage
Examples of usage:

`kinder-control.py firewall.mynetwork.com PFFAFirewallControl 84ru5oghego3hgwtwhf4oohgewronrlg3 gaming-pcs disable`

* On pfSense firewall 'firewall.mynetwork.com', disable rule containing the string 'gaming-pcs' in the description.