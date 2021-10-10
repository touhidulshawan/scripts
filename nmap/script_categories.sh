#!/bin/bash

PS3="Select type of script: "

select type in auth broadcast brute dos malware vuln; do
    read -t 20 -p "Enter target IP : " target_ip
    sudo nmap --script $type $target_ip -sS
    break
done
