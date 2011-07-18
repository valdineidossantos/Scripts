from unittest import TestCase, main
from crawler import Crawler
"""
class Test_Crawler( TestCase ):
    def test_google_title ( self ):
        crawler = Crawler()
        crawler.search( "python" )
"""


#Start Tests Go :P
if __name__ == '__main__':
    #main()
    crawler = Crawler()
    crawler.silent = False
    crawler.search( "python" )

