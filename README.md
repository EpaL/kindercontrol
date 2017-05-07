# kindercontrol
A command-line tool that enables/disables pfSense rules.

## Introduction
As any parent with young children these days knows, electronics and the Internet serve as an all-too-tempting distraction that can be hard to control.

To regain control, I wanted a way of quickly disabling Internet access on the kids devices. 

There are of course several out-of-the-box solutions out there but they involve cost, extra hardware and some use 'hacker'-like techniques like ARP Poisoning.

I've been a fan of pfSense for years and so went looking for a way to control it remotely.

This script forms a part of the control mechanism. Using this script I can quickly enable and disable rules on pfSense that are set up to block my kid's devices. To run the scripts from my phone, I use the excellent Alfred (https://www.alfredapp.com) and it's companion iOS app.

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