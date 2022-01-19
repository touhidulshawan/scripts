from random import randint
import colored
from colored import stylize
import subprocess
import optparse


# Generating a random mac address
random_mac = lambda: ":".join([f"{randint(0, 255):02x}" for _ in range(6)])

new_mac_address = random_mac()

# Get Arguments


def get_arguments():
    parse_arguments = optparse.OptionParser()
    parse_arguments.add_option(
        "-i", "--interface", dest="interface", help="Interface to change mac address"
    )
    (options, arguments) = parse_arguments.parse_args()

    # check if the user give interface arugument
    if not options.interface:
        parse_arguments.error(
            f"{stylize('[-]', colored.fg('red'))} Please specify an interface. Use --help for more info"
        )
    return options


# fucntion to change mac address


def change_mac_address(interface, new_mac_address):
    print(
        f"{stylize('[+]', colored.fg('green'))} changing mac address for {interface} to {new_mac_address}"
    )

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac_address(options.interface, new_mac_address)
