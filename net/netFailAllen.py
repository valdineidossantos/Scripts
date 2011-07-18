#!-*- coding: utf-8 -*-

#imports
from twill import commands 
from twill.browser import BrowserStateError
from BeautifulSoup import BeautifulSoup
from time import time

def getStatus (url, keyWord):
  """
  @Function getStatus:
    Verify an url and return True for valid connection and search an key word  in contents
  @params:
    url: Url host for access -> http://www.google.com.br/
    keyWord: Word search in source code host
  """
  try:
    start = 0 #Start time elapse 
    end   = 0 #time elapse for request
    my_browser =  commands
    my_browser.redirect_output("/dev/null")
    my_browser.debug("http", 0)
    my_browser.debug("commands", 0)
    my_browser.debug("equiv-refresh", 0)
    my_browser.redirect_error("/dev/null")
    start =  time()
    my_browser.go ( url )
    end =  time()
    html  = my_browser.browser.get_html() 
    #print "\nTime Elapse: %s\n" % (end - start)
  except BrowserStateError, bs:
    return False
  except Exception, e:
    raise Exception("Error [%s] [%s]" % ( e.__doc__ , e ) )
  
  source_code =  BeautifulSoup( html )
  
  title_page  =  source_code.findAll('title')

  if len(title_page) == 0:
    return False

  title = str(title_page[0]).lower()
 
  if str( keyWord ).lower() in title:
    return True  
   
   
  return False 

