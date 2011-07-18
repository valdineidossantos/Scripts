from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

class Forecast ( object ):
  """
  @Constructor
  """
  def __init__(self):
    self.temperature = {'max':0, 'min':0}
    """
    URL de Petropolis
    """
    self.url = 'http://www.inmet.gov.br/webservice/previsao/?geraXml=&TP=MC&UF=RIO%20DE%20JANEIRO&MC=PETROPOLIS'
    try: 
      source =  urlopen( self.url ).readlines()
      self.soup   = BeautifulSoup ("".join( source ) )
    except:
      raise Exception ("A url informada para aquisicao do XML nao esta acessivel ou e inexistente")

    self._set_temperatures()
 
  """
  @Methods
  """
  def _get_minimum ( self ): 
     return self.temperature['min'] 

  def _get_maximum ( self ): 
     return self.temperature['max'] 

  def _set_temperatures( self ):
    self.temperature['max'] = int ( self.soup.find("max").getText() )
    self.temperature['min'] = int ( self.soup.find("min").getText() )
    return self.temperature   

  def _get_forecast ( self ):
    return self.soup.find("previsao").getText() 

  def _get_trend ( self ):
    return self.soup.find("tendencia").getText()
 
 
  """
  Forecast Atributes
  """
  maximum  =  property ( _get_maximum  )
  minimum  =  property ( _get_minimum  )
  forecast =  property ( _get_forecast )
  trend    =  property ( _get_trend    )
