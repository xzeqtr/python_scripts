from platform   import system as system_name  # Returns the system/OS name
from subprocess import call   as system_call  # Execute a shell command

def ping(host):
    param = '-n' if system_name().lower()=='windows' else '-c'
    response = system_call(['ping', param, '1', host])
    return response

print(ping('192.168.0.1'))