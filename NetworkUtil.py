import psutil
import re

def get_interfaces_addresses():
    regex = re.compile("(?<=address=').*?(?=')")
    rez_string = str(psutil.net_if_addrs())
    return regex.findall(rez_string)