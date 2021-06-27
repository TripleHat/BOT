#!/bin/python

try:
 import requests
 from os import system as shell
 from requests import *
 import gtts
 from gtts import gTTS as bot
 import string,sys,time
 from core.banner import BN
except:
 print("\033[31;1mERROR: Run \033[32;1mbash install.sh\033[31;1m first\033[0m")
 sys.exit()

yellow = '\033[33m'
blue = '\033[34m'
cyan = '\033[36m'
green = '\033[32;1m'
red = '\033[31;1m'
close = '\033[0m'

reqSucc = [200, 201, 202, 203]

def Textout(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)

''' check if internet is active '''

try:
 net = get("https://github.com/TripleHat", timeout=3)
#except (ConnectionError, Timeout) as Ex:
except Exception as Ex:
 if Ex == str("ConnectionError") or str("Timeout"):
  Textout(red+"\n[!] No Internet Connection [!]\n\n"+close)
  sys.exit()
 elif Ex == str("KeyboardInterrupt"):
  sys.exit(red+"\n"+Ex+close+"\n\n")
 else:
  sys.exit(red+"\n"+Ex+close+"\n\n")

''' Done '''

''' check for update xD '''
try:
 upd = get("https://github.com/TripleHat/BOT/blob/master/core/.V1")
 if upd.status_code == 200:
  ''' No Update '''
  pass
 if upd.status_code == 404:
  ''' New Update Available '''
  Textout(green+"\nNew Update Available\n"+close)
  Textout(yellow+"Updating..."+close)
  shell("bash core/update.sh")
except:
 pass

# which type of device is this

if sys.platform != str("linux"):
 Textout(red+"[!] Ooops, This is For Linux Users Only"+close)
 sys.exit(red+"\nProgram Stopped\n\n"+close)

elif shell("which play-audio > /dev/null") == 256:
 Textout(red+"\ninplay audio package Not Found "+green+"Installing...\n\n"+close)
 shell("pkg install play-audio -y > /div/null || apt-get --assume-yes install play-audio > /dev/null")

else:
 pass

# lets Define Talking Field

def say(info):
 sound = shell("play-audio "+info)
 return sound

def getText():
 try:
  Text = input(green+"\nEnter Text: "+cyan)
  print(close+"")
  return Text
 except Exception as Essau:
  Textout(red+"\n"+Essau+"\n\n"+close)
  sys.exit(red+"Exiting...\n\n")

def getTextfile():
 say("sound/attention.mp3")
 print(red+"\nAttention! "+yellow+"Here You must copy your Text file To this Directory\n"+close)
 try: 
  file = input(green+"Enter File Name: "+cyan)
  print(close)
#  file.replace(".", "")
  if file == "":
   Textout(red+"\nYou Dont provide any file To read\n\n"+close)
   sys.exit(red+"Exiting...\n\n"+close)
 except Exception as Essau:
  Textout(red+Essau+"\n\n"+close)
 try:
   with open(file, "r") as F:
    TextFile = F.read()
    return TextFile
 except FileNotFoundError as Nf:
  Textout(red+"\nFile not Found!\n"+close)
  sys.exit(red+"\nExiting...\n\n"+close)

class Talk:

 def talk(Text):
  try:
   if Text == "":
    say("sound/error.mp3")
    Textout(red+"Exiting Program...\n\n"+close)
    sys.exit()
   Say = bot(Text)
  except Exception as Essau:
   Textout(red+"\n"+Essau+"\n"+close)
   sys.exit()
#  say("save.mp3")
  accept = [ "Yes", "Y", "yes", "YES", "y" ]
  if input(cyan+"\nDo You want To save Audio for Future Use? <Yes/No>: "+close) in accept:
   print("\n")
   shell("play-audio sound/entName.mp3")
   try:
    filename = input(green+"Enter name Without extension: "+close)
    filename.replace(".", "")
   except Exception as Essau:
    Textout(red+"\n\n"+Essau+close)
    sys.exit()
   if filename == "":
    filename = "default"
   try:
    Say.save(filename+".mp3")
    shell("mv "+filename+".mp3 -t SAVED")
    shell("play-audio "+"SAVED/"+filename+".mp3")
    Textout(cyan+"\nSaved to:"+green+" SAVED/"+green+filename+".mp3"+close+"\n")
    time.sleep(3)
#    arg = input("\n  "+green+"<BoT>-->: "+cyan)
   except Exception as Expt:
     Textout(red+str(Expt)+close+"\n")
     sys.exit()
  else:
   try:
    Say.save("tht3.mp3")
    shell("play-audio tht3.mp3")
    shell("rm tht3.mp3")
#    sys.exit()
   except Exception as X:
    Textout(red+str(X)+close+"\n")
    sys.exit()

#Talk.talk(getText())

def main():

 def argue():
#  Textout(" "+blue+"Enter Option\n"+close)
  try:
   #arg = ""
   arg = input("\n  "+green+"<BoT>-->: "+cyan)
   suc = ["1", "2", "99"]
#   if args.isalpha() == True:
 #   arg = str(args)
  # elif args.isnumeric() == True:
#    arg = int(args)
   if arg == "1":
    Talk.talk(getText())
   elif arg == "2":
    Talk.talk(getTextfile())
   elif arg == "99":
    Textout(cyan+"\nCoded by TripleHat\n"+close)
    sys.exit()
   else:
    Textout(red+"\n Option Not Exist!\n"+close)
    option()
   option()
  except KeyboardInterrupt:
   Textout(red+"\nCancelled by User"+close+"\n")
   sys.exit(red+"\nExiting..."+close+"\n")

 def option():
  shell("clear")
  BN.banner()
  print("\n")
  print(" "+yellow+"["+red+"1"+yellow+"]"+green+" Enter Text "+close)
  print("\n")
  print(" "+yellow+"["+red+"2"+yellow+"]"+green+" Take Text From File "+close)
  print("\n")
  Textout(" "+red+"<99> To quit"+close)
  print("\n")
  argue()

 option()

if __name__ == "__main__":
 main()
