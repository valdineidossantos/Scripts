#! /usr/bin/env python

from unittest import TestCase, main
from netFailAllen import getStatus

class TestNetFail( TestCase ):

  def setUp( self ):
    """
    Jobs for all tests here
    """ 

  def test_retorna_verdadeiro_pagina_valida( self ):
    url_acesso    = "http://10.0.1.6"
    uri_acesso    = ""
    url           = "%s/%s" % (url_acesso, uri_acesso)
    palavra_chave = 'Fedora'
    resultado     = getStatus( url, palavra_chave )
    self.assertTrue(resultado)


  def test_retorna_false_pagina_valida( self ):
    url_acesso    = "http://10.0.1.6"
    uri_acesso    = ""
    url           = "%s/%s" % (url_acesso, uri_acesso)
    palavra_chave = 'JAVA_E_DOT_NET_SAO_FODAS? #NOT'
    resultado     = getStatus( url, palavra_chave )
    self.assertFalse (resultado)

  def test_retorna_false_pagina_invalida (self):
    url_acesso    = "http://www.google.com"
    uri_acesso    = ""
    url           = "%s/%s" % (url_acesso, uri_acesso)
    palavra_chave = 'JAVA_E_DOT_NET_SAO_FODAS? #NOT'
    resultado     = getStatus( url, palavra_chave )
    self.assertFalse (resultado)

 
  def test_retorna_true_pagina_valida_palavra_valida_google( self ):
    url_acesso    = "http://www.google.com.br"
    uri_acesso    = ""
    url           = "%s/%s" % (url_acesso, uri_acesso)
    palavra_chave = 'GoOglE'
    resultado     = getStatus( url, palavra_chave )
    self.assertTrue(resultado)

 
  def test_retorna_true_pagina_valida_palavra_valida_quest( self ):
    url_acesso    = "http://www.quest.com"
    uri_acesso    = ""
    url           = "%s/%s" % (url_acesso, uri_acesso)
    palavra_chave = 'quest'
    resultado     = getStatus( url, palavra_chave )
    self.assertTrue(resultado)

  def test_retorna_false_host_invalido ( self ): 
    url_acesso    = "http://www.sitemuitodoidosemnocao.com"
    uri_acesso    = "nada.html"
    url           = "%s/%s" % (url_acesso, uri_acesso)
    palavra_chave = 'nuncaAchara'
    resultado     = getStatus( url, palavra_chave )
    self.assertFalse(resultado)




if __name__ == '__main__':
  main()

