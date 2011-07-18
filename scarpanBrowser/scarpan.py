import twill.commands
from BeautifulSoup import BeautifulSoup
from time import sleep
import twill.commands as firefox
from sets import Set
from splinter.browser import Browser
from random import randint
class ScarpanBrowser ( object ) : 
    def __init__ ( self ):
        #self.base_url     = "http://www.webcamps.com.br/"
        #self.base_url     = "http://localhost"
        self.base_url     = "http://www.scarpan.com.br"
        self.links   = []
        self.visited = ["%s/" % self.base_url]
        browsers = ["webdriver.firefox", "webdriver.chrome", "zope.testbrowser"]
        self.browser =  Browser(browsers[randint(0,2)])
        #Redirect Messages
        firefox.redirect_error("/tmp/twill.err")
        firefox.redirect_output("/tmp/twill.out")  
        firefox.go( self.base_url )
        self.browser.visit( self.base_url )
        self.extractAllLinks ( firefox.showlinks() )
        self.visitAllLinks()

    def extractAllLinks(self, links):
        for link in links:
            if self.checkImage( link.url ) or link.absolute_url == link.url:
                continue
            if "page=" in link.url:
                link.url =  "/produtos/%s" % link.url

            url = "%s%s" % ( self.base_url, link.url )
            self.links.append( url )
        return self.links

    def visitAllLinks(self):
        valid_links = True
        while valid_links:
            wait = randint (0,60)
            #print "Wait %s for surf new page" % wait
            #sleep (wait)
            if len( self.links ) == 0:
                valid_links = False
                break
            link =  self.links.pop()
            if link not in self.visited:
                try:
                    #Debug
                    print "Visit : %s" % link
                    firefox.go(link)
                    self.browser.visit( link )
                    self.visited.append (link)
                    self.extractAllLinks ( firefox.showlinks() )
                except:
                    pass
            else:
                #print "Visited: %s" % link
                pass

        self.extractAllLinks( firefox.showlinks() )
        for link in self.links:
            if self.checkImage ( link ):
                continue
            if link not in self.visited:
                self.visitAllLinks() 
                
        print "Finished close browser"
        try:
            self.browser.quit()
        except Exception , e:
            print "%s %s" % ( e.__doc__ , e )
        self.showResume() 

    def showResume(self):
        self.visited.sort()
        for link in self.visited:
            print link
        print "Total Links Visited: %s " %  len( self.visited)
                     
    def checkImage(self, url):
        url =  str( url ).lower()
        if url[-3:] == 'png' or url[-3:] == 'jpg' or url[-3:] == 'gif':
	    return True
	return False
     
s =  ScarpanBrowser()


