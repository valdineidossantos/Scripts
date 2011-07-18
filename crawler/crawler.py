import twill.commands as mybrowser
from urllib2 import HTTPError

class Crawler(object):
    def __init__(self):
        self.base_url = "http://www.google.com.br"
        self.silent = True
    
    def search (self, key_word):
        mybrowser.go( self.base_url )

        #Silent Mode default True'
        if self.silent:
            mybrowser.redirect_error("/dev/null")       
            mybrowser.redirect_output("/dev/null")
        try:    
            mybrowser.formclear("1")#reset For first Form
            mybrowser.fv("1", "q", key_word) #change First Form with Key Word
            mybrowser.submit("btnG") #Click Search in Google not
            print "Request Finished"
        except HTTPError, httpe:
            print "\nError: %s\n%s\n%s" % (httpe.code, httpe.msg, httpe.__doc__)
        except IOError, io:
            print "IOError: %s " % io
        except Exception, e:
            print "Generic Error: %s" % e

        print "Retrieve Links"
        links = mybrowser.showlinks()
        follow_links = []

        for link in links:
            follow_links.append ( link.url )

        print follow_links
        
