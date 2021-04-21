#parsing arguments before start
import argparse
PermissionError= 0
arg = argparse.ArgumentParser()
arg.add_argument("-i", "--install", help="install requirements (packages)", action="store_true")
arg.add_argument("-nt", "--notor", help="disable tor (not recommended / faster)", action="store_true")
arg.add_argument("-m", "--message", help="Message you want to send (MAX 70 CHARRACTERS)")
arg.add_argument("-to", "--receiver", help="the phone number you want to send sms (without + and with country code) (example: '18051112222' / '1 (805) 111 2222)'")
isset_number=False
isset_message=False

def setnumber(number):
  number=number.replace('+', '').replace('(', '').replace(')', '').replace(' ', '')
  try:
    int(number)
    return int(number)
  except ValueError:
    print('\033[0;33;40m!!!\n    ERROR: illegal number\n!!!\n\033[0;37;40m   Valid Numbers:\n    +1 (805) 102 1020\n    +1 805 102 1020\n    1 805 1020\n    18051021020\n   NOT:\n    ' + number)
    return False

args = arg.parse_args()
if args.install:
  import subprocess
  import sys
  sys.stderr = object
  def install(x):
    subprocess.check_call([sys.executable, "-m", "pip", "install", x])
  packages=[
    'pycurl',
    'psutil'
    ]
  print('installing \033[1;37;40m' + str(len(packages)) + '\033[0;37;40m packages\n those are: \033[1;37;40m' + ', '.join([str(package) for package in packages]))
  for packet in packages:
    install(packet)
  exit()
try:
  import pycurl
  if not args.notor:
      try:
        import psutil
      except PermissionError:
        Permissionerr= 1
except ModuleNotFoundError:
  print('\033[1;31;40mERROR: One or more of the required modules are missing! \n  Run python3 nizemes.py -i\n\n\033[1;37;40m')
  exit()
import certifi
import json
import io
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

class Loader:
    def __init__(self, desc, end, timeout=0.1):
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        self.stop()

if args.message:
  isset_message=True
  if len(args.message) > 70:
    print('\033[0;33;40m!!!\n    WARNING: message exceeds 70 character limit\n!!!\033[0;37;40m\n\n\033[1;32;40m ' + args.message[0:70] + '\033[1;31;40m' + args.message[70:len(args.message)] + '\n\n\033[1;37;40m Y => Continue and send the green highlighted part\n N => Exit\n')
  if not message:
    temp=input('what tf to do? sir... >>> ')
    if temp.lower == 'y':
      message = args.message[0:70]
      print('Continue>\n  New message: ' + message)
    else:
      exit()
  else:
    message = args.message

use_tor = True
if args.notor:
  use_tor= False

if args.receiver:
  isset_number=True
  number=args.receiver
  number = setnumber(number)
  if not number:
    exit()
if not isset_number:
  while not isset_number:
    number = input('The phone number to send the sms to -=> ')
    number = setnumber(number)
    if number:
      isset_number = True
  print('\n')
if not isset_message:
  while not isset_message:
    message = input('write the message to send -=> ')
    if len(message) > 70:
      gecerli_yanit = False
      print('\033[0;33;40m!!!\n    WARNING: message exceeds 70 character limit\n!!!\033[0;37;40m\n\n\033[1;32;40m ' + message[0:70] + '\033[1;31;40m' + message[70:len(message)] + '\n\n\033[1;37;40m Y => Continue and send the green highlighted part\n N => Edit message\n')
      while not gecerli_yanit:
        temp=input('what tf to do? sir... >>> ')
        if temp.lower =='y':
          isset_message=True
          message=message[0:70]
          gecerli_yanit=True
        if temp.lower =='n':
          gecerli_yanit=True
    else:
     isset_message = True
     message = message
#prepare tor if need
if use_tor:
  temp=False
  output=""
  response = io.StringIO()
  import subprocess
  proc = subprocess.Popen('tor', stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
  while not temp:
    with Loader("Connecting to tor network...", 'Connected ✓'):
     while not temp:
      output = output + str(proc.stdout.read(1), 'utf-8')
    #  print (output)
      x = output.find('Bootstrapped 100% (done): Done')
      depug = output.find('Could not bind to 127.0.0.1:9050: Address already in use. Is Tor already running?')
      if depug > -1:
        output = ""
        print('Existing tor processes are killing')
        #this is a vulnerability ikr
        if Permissionerr==0:
          PROCNAME = "tor"

          for proc2 in psutil.process_iter():
          # check whether the process name matches
           if proc2.name() == PROCNAME:
              proc2.kill()
        else:
          print('type: killall tor')
          exit()
      if x > -1:
        temp=True
  tor_proxy='127.0.0.1:9050'
  proxy = tor_proxy.split(':')
  print(output[(len(output)-18):len(output)])
else:
  print('The tor connection is bypassed, this is not recommended!')
with Loader("Request sending to the server...", 'Request sent✓'):
#send sms
 response = ""
 number = '+' + str(number)
 smsapi = 'https://textbelt.com/text'
 
 curl = pycurl.Curl()
 curl.setopt(pycurl.URL, smsapi)
 curl.setopt(pycurl.USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:8.0) Gecko/20100101 Firefox/8.0')
 if use_tor:
    curl.setopt(pycurl.PROXY, proxy[0])
    curl.setopt(pycurl.PROXYPORT, int(proxy[1]))
    curl.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
 curl.setopt(pycurl.HTTPHEADER, ['Accept: application/json',
                                'Content-Type: application/json'])
 curl.setopt(pycurl.POST, 1)
 curl.setopt(pycurl.TIMEOUT_MS, 10000)
 curl.setopt(pycurl.VERBOSE, 1)
 body_as_dict = {"phone": number, "message": message, "key": "textbelt"}
 body_as_json_string = json.dumps(body_as_dict)
 body_as_file_object = io.StringIO(body_as_json_string)
 #curl.setopt(curl.WRITEFUNCTION, response.write)
 curl.setopt(pycurl.READDATA, body_as_file_object) 
 curl.setopt(pycurl.POSTFIELDSIZE, len(body_as_json_string))
 response = curl.perform()

 status_code = curl.getinfo(pycurl.RESPONSE_CODE)
 if status_code != 200:
    print("\033[0;33;40ma problem occured... :// .. Server http status code is " + str(status_code) + '\033[1;37;40m')
 else:
  print('\nmessage:' + message + '\n\n is sent to ' + number)
 curl.close()
print(str(response)+'\n')