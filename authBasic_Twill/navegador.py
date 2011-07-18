import twill
from time import sleep
url_="http://10.0.1.172"
uri_="protegido"
full_url = "%s/%s" % (url_, uri_)
realm =  "Acesso Restrito"
uri   =  url_ 
user  = "test_user"
passwd= "pass_crazy" 
twill.commands.add_auth(realm, uri, user, passwd)
firefox =  twill.commands

firefox.go ( full_url )
print "\n\nSource for this URL: %s\n\n" %  firefox.browser.get_url()
sleep ( 5 )

firefox.showforms()
firefox.submit('0')
source = firefox.browser.get_html( )

print "\n\nSource for this URL: %s\n\n" %  firefox.browser.get_url()
sleep ( 5 )
for line in source.split("\n"):
    sleep ( 0.5 )
    print line
