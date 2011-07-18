#imports
import twill
from time import sleep
from commands import getstatusoutput as run

#VARS
url_="http://192.168.0.1"
uri_=""
full_url = "%s/%s" % (url_, uri_)

realm =  "valdineirouter"
uri   =  url_ 
user  = "admin"
passwd= "d1n31" 


command = "ping -c 2 google.com"
repeat = True
times  = 1


twill.commands.add_auth(realm, uri, user, passwd)

firefox =  twill.commands

firefox.go ( full_url )
print "\n\nSource for this URL: %s\n\n" %  firefox.browser.get_url()

#Go to Admin link
firefox.go('tools_admin.html')

#Go to Misc link
firefox.go('tools_misc.html')

#Show all Forms 
firefox.showforms()


formname  = "form2"  
fieldname = "restart"  
value     = "None"

#Change Form2 to submit
firefox.fv(formname, fieldname, value)

firefox.submit()

#HARD reset :D
#firefox.go("restart.cgi")


#ping google  finishing the process
while repeat:
    
    status, output = run ( command )
    
    print "\nStatus: %s" % status
    print "\nOutput: %s" % output
    
    if int(status) == 0 or times == 10:
        repeat =  False
        break
    else:
      times = times + 1    
      sleep (10)
    

print "\nRouter restarted..."
