#! /usr/bin/env python

from unittest import TestCase, main
from weather import Forecast


class TestForecast( TestCase ):

  def setUp (self): 
    self.forecast =  Forecast()

  def test_maximum_temperatures_as_number ( self ):
    result   = type(self.forecast.maximum)
    expected = type( 32 )
    self.assertEqual ( result, expected )    
  
  def test_minimum_temperatures_as_number ( self ):
    result   = type(self.forecast.minimum)
    expected = type( 0 )
    self.assertEqual ( result, expected )
    
  def test_minimum_temperatures_negative_as_number ( self ):
    result   = type(self.forecast.minimum)
    expected = type( -10 )
    self.assertEqual ( result, expected )    
  

  def test_get_forecast( self ):
    result   =  type (self.forecast.forecast)
    expected =  type ( unicode (" vai chover um dia ") )
    self.assertEqual( result, expected )






if __name__ == '__main__':
  main() 

