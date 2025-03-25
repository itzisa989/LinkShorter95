import sys
import time
import pyshorteners

text = '''\x1b[38;5;46m
Hi Termux Hecker
This Username is : isa.py
This Password is : isa.py
'''
for x in text:
  sys.stdout.write(x)
  sys.stdout.flush()
  time.sleep(0.05)
  
username = "isa.py"
password = "isa.py"

def end():
  python = print()
  sys.end




givenUsername = input("\x1b[37mEnter Your Username:")
if givenUsername == username:
  print("	\x1b[38;5;41mCorrect Username :)")
  givenPassword = input("\x1b[37mEnter Your Password:")
  if givenPassword == password:
    print("	\x1b[38;5;41mCorrect Password :)")
  
  else:
    print("\x1b[31mNot Available :(")
    time.sleep(1)
    print("Press Entar to end")
    end()
else:
  print("\x1b[31mNot Available :(")
  time.sleep(1)
  print("Press Entar to end")
  end() 
  
logo = '''\x1b[38;5;10m

  _      _       _       _____ _                _            ___  _____ 
 | |    (_)     | |     / ____| |              | |          / _ \| ____|
 | |     _ _ __ | | __ | (___ | |__   ___  _ __| |_ ___ _ _| (_) | |__  
 | |    | | '_ \| |/ /  \___ \| '_ \ / _ \| '__| __/ _ \ '__\__, |___ \ 
 | |____| | | | |   <   ____) | | | | (_) | |  | ||  __/ |    / / ___) |
 |______|_|_| |_|_|\_\ |_____/|_| |_|\___/|_|   \__\___|_|   /_/ |____/ 
                                                                        
                                                                        

'''

for x in logo:
  sys.stdout.write(x)
  sys.stdout.flush()
  time.sleep(0.005)
  
  
link = input("\x1b[38;5;47mEnter Link : ")

s = pyshorteners.Shortener()
provide = s.tinyurl.short(link)

print(f"\x1b[38;5;47mYour short Link : {provide}")

  