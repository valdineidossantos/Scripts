#!/usr/bin/env python

from commands import getstatusoutput as run
from time import sleep
from datetime import datetime
from sys import exit
from urllib2 import urlopen, HTTPError

MAX_TIMES=100

start = datetime.now()

def debug( status, output ):
  return False
  print "_" * 100
  print "\nstatus:[%s]" %  status 
  print "\noutput:"
  print output

def check_foglight_running(): 
    command =  "/bin/ps auxx | /bin/grep -v grep | /bin/grep -v python |  /bin/grep -i FogLight | wc -l"
    status, output =  run( command )
    debug( status, output )
    if int (output) > 0:
        return True
    else:
        return False



def foglight_console_available():
    url = "http://10.0.100.100:8080/"
    times = 1
    while times < 50:
        try:
            handle = urlopen ( url )
            http_status = int(handle.getcode())
	    if http_status == 200:
	        return True
                break
        except HTTPError, http: #Case http status 404
	    times =  times + 1 
        sleep (5)
    return False    

def stop_fogLight ( ):
    print "\nStopping Foglight"
    now =  datetime.now()
    print now.strftime("%d/%m/%Y %H:%M:%S")
    stop_command  = " /Quest_Software/Foglight/bin/fms -q " #option -q stop
    status, output =  run( stop_command )
    debug( status, output )
    times  = 1
    if output == 0:
        return True
    else:
        foglight_running = True

    while foglight_running:

    	 if not check_foglight_running():
	    foglight_runnig = False
            break;
         if times == MAX_TIMES:
            foglight_runnig = False
            stop_foglight_forced()
            break;
         times = times + 1 
         sleep(2)
    return True

def stop_foglight_forced ():
    print "\nStop forced"
    now =  datetime.now()
    print now.strftime("%d/%m/%Y %H:%M:%S")
    #Kids do not do this at home ...
    kill_command = "/bin/kill -9 `/bin/cat /Quest_Software/Foglight/state/.Foglight-fogserver.pid`"
    status, output =  run( kill_command )
    debug( status, output )
    if int(status) == 0:
        return True 
    return False 

def start_foglight():
    print "\nStarting Foglight"
    now =  datetime.now()
    print now.strftime("%d/%m/%Y %H:%M:%S")
    stop_command  = " /Quest_Software/Foglight/bin/fms -d " #option -d start as daemon
    status, output =  run( stop_command )
    debug( status, output )
    if int(status) == 0:
        return True 
    return False 

def restartFoglight():
    stop_fogLight()
    start_foglight()


#The program
restartFoglight()
print "\nFinished foglight restart operation"
now =  datetime.now()
print now.strftime("%d/%m/%Y %H:%M:%S")

finish =  datetime.now()

total  = finish - start

print "\nTotal seconds: %s" % total.seconds

print "\nConsole avaible? %s\n" % check_foglight_running() 

exit(0)
