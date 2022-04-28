import subprocess

def send(phone_num, message):
    subprocess.check_call(['./sms.sh', phone_num, message])
    #TODO: parse message output and figure out if it succeeded or not
    