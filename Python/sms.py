import subprocess

def send(phone_num, message):
    subprocess.check_call(['./sms.sh', phone_num, message])
    #TODO: parse message output and figure out if it succeeded or not

def send_image(phone_num, image_filename, ip_addr, message_body):
    #message body is optional, send "" as a 4th argument if you don't want a message
    subprocess.check_call(['./sms_picture.sh', phone_num, image_filename, ip_addr, message_body])