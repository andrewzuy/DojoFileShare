import psutil
import re

def get_interfaces_addresses():
    regex = re.compile("(?<=address=').*?(?=')")
    rez_string = str(psutil.net_if_addrs())
    interfaceList = regex.findall(rez_string)
    for line in interfaceList:
        if '-' in line:
            interfaceList.remove(line)
    return interfaceList