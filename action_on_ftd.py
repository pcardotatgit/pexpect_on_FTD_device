import yaml
import pexpect
from pexpect import pxssh
from crayons import blue, green, yellow, white, red, cyan


def yaml_load(filename):
    fh = open(filename, "r")
    yamlrawtext = fh.read()
    yamldata = yaml.load(yamlrawtext,Loader=yaml.FullLoader)
    return yamldata


def DataRetrieval(**device):
    '''
    Data Retrieval from Devices
    Input Device dictionary
    Returns All lines in a list : line_lists
    '''
    lines=[]
    try:
        # Use PXSSH to Open Connection
        print(yellow(f"Trying to SSH connect to device : {device['ipaddr']}"))
        child = pxssh.pxssh()
        print(yellow("Login in progress... Wait at least 30 secondes..."))
        child.login(device['ipaddr'], device['username'],device['password'], auto_prompt_reset=False)
        child.expect('>')
        print(yellow("Ok Connected. Prompt > received"))
        # Ask for CPU Stats
        print(yellow(f"Send {device['command']} CLI Commands To FTD device : {device['ipaddr']}"))
        child.sendline(device['command'])
        child.expect('>')
        show_command = child.before
        print(green("DONE ", bold=True))

        # Close Connection
        # child.sendline ('exit')
        # child.expect(pexpect.EOF)
        child.logout()

        # Assigns Output to arrays
        for item in str(show_command.decode('utf-8')).splitlines():
            lines.append(item.lstrip())

    except Exception as e:
        # logger.error('Failed to pull data from {} '.format(
            # device['hostname']),  exc_info=True)
        raise

    return lines

if __name__ == '__main__':
    device = {}
    devices = yaml_load("actions.yml")
    # loop through devices and parse them one-by-one
    for device in devices["devices"]:
        print(yellow(f"Start action : {device['action']} on {device['ipaddr']}",bold=True))
        #pprint(device)    
        FDM_USER = device ['username']
        FDM_PASSWORD = device ['password']
        FDM_HOST = device ['ipaddr']       
        #print(yellow(FDM_HOST,bold=True))
        print("===================================================")
        lines_list=DataRetrieval(**device)
        for line in lines_list:
            print(green(line,bold=True))
        print(green("==================================================="))
 
