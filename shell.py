#!/usr/bin/python3
#Coded By Nii-sanHaxor 

# GAUSAH RECODE + GANTI AUTHOR ! KALO MAU DI HARGAIN :)

# INGAT ANDA NUB KALO MASIH RECODE ! AOWKAOKW BANGSAD 

# HAIKER KOK BUTA PROGRAM 

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import argparse
import sys
import time

global starttime

class Searcher():

    def __init__(self):
        self.scan()
        
    def scan(self):
        # argument parser like shit
        parser = argparse.ArgumentParser(prog="Nii-san.py", description="Simple Find Shell in Website")
        parser.add_argument("-u", dest="domain", help="your url")
        parser.add_argument("-w", dest="wordlist", help="your wordlsit")
        args = parser.parse_args()
        if not args.domain:
            sys.exit("\033[36musage: shell.py -u example.com -w wordlist.txt")
        if not args.wordlist:
            sys.exit("\033[36musage: shell.py -u example.com -w wordlist.txt")
            
        # handle url website format
        site = args.domain
        print("\033[96m\033[96m[\033[90m{0}\033[96m]".format(time.strftime("%H:%M:%S")),"\033[97m[\033[92mInfo\033[97m] \033[0mStarting This Tools...")
        print("\033[96m[\033[90m{0}\033[96m]".format(time.strftime("%H:%M:%S")),"\033[97m[\033[92mInfo\033[97m] \033[0mWaiting To Response....","\n")
        time.sleep(3)
        if not site.startswith("http://"):
            site = "http://"+site
        if not site.endswith("/"):
            site = site+"/"
        # load wordlist
        try:
            pathlist = args.wordlist
            wlist = open(pathlist, "r")
            wordlist = wlist.readlines()
        except FileNotFound as e:
            print("\033[91mSorry, Wordlist Not Found!\033[0m")
            exit()
        finally:
            try:
                wlist.close()
            except:
                print("\033[91mWordlist Can\'t Close!\033[0m")
        # user-agent
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
        #list to hold the results we find
        found = []
        # respon code
        resp_codes = {403 : "403 forbidden", 401 : "401 unauthorized"}
        # loop with join pathlist
        starttime = time.time()
        for psx in wordlist:
            try:
                psx = psx.replace("\n", "")
                url = site+psx
                req = Request(url, headers={"User-Agent": user_agent})
                time.sleep(0.1)
                try:
                    connection = urlopen(req)
                    print("\033[96m[\033[90m{0}\033[96m]".format(time.strftime("%H:%M:%S")),"\033[97m[\033[96mFound\033[97m] :","\033[0m/"+psx)
                    found.append(url)
                    
                except HTTPError as e:
                    if e.code == 404:
                        print("\033[96m[\033[90m{0}\033[96m]".format(time.strftime("%H:%M:%S")),"\033[97m[\033[31mWarning\033[97m] :","\033[0m/"+psx)
                    else:
                        print("\033[96m[\033[90m{0}\033[96m]".format(time.strftime("%H:%M:%S")),"\033[97m[\033[92mInfo\033[97m] :","\033[33m/"+psx,"\033[92mstatus:\033[33m",resp_codes[e.code])
                        
                except URLError as e:
                    sys.exit("\033[97m[\033[31mWarning\033[97m] Sorry, No Internet Connection")
                except Exception as er:
                    print("\n\033[93m[?] \033[0mYour Connection Is Bad")
                    print("\033[97m[\033[31mWarning\033[97m] \033[0mExit Program")
                    time.sleep(3)
                    exit()
            except KeyboardInterrupt as e:
                print("\033[97m[\033[31mWarning\033[97m] \033[0mCTRL+C Detected")
                print("\033[97m[\033[31mWarning\033[97m] \033[0mExiting This Program....")
                time.sleep(4)
                exit()
        
        if found:
            print("\n\033[96m[+] \033[0mResult Found\033[92m")
            print("\n".join(found))
            print("\033[96m[?] \033[0mTime Elasped: \033[35m%.2f\033[0m Seconds" % float(time.time()-starttime))
        else:
            print("\n\033[97m[\033[31mWarning\033[97m] \033[0mCould Not Find Any Shell Backdoor")
            print("\033[96m[?] \033[0mTime Elasped: \033[33m%.2f\033[0m Seconds" % float(time.time()-starttime))
                
    def banner():
        # just the screen display like this
        info = """
\033[97m[*]====================================\033[97m[*]  
\033[5m
 _____ _       _ _ _____             
|   __| |_ ___| | |   __|___ ___ ___ 
|__   |   | -_| | |__   |  _| .'|   |
|_____|_|_|___|_|_|_____|___|__,|_|_| V.2
          
\033[0m                    
\033[97m[*]====================================\033[97m[*]
\033[33mCoded By : Nii-san Haxor
\033[34mTeam     : IndoSec | BekasiSec
\033[31mFamilly  : Indramayu Cyber Team
\033[96mSince    : 2017
\033[96mNb : Kalian Boleh Edit/Bikin Sendiri Wordlistnya
\033[97m[*]====================================\033[97m[*]
              """
        return info
    print(banner())
                
if __name__ == '__main__':
    Searcher()