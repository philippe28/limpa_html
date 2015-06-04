#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib
import urllib2
import os
#lista todos os diretorios
for root, dirs, files in os.walk("/home/philippe/Downloads/wikiSample/"):
    caminho= str(root)
    
    for x in files:
	#"file ://" e necessario porcausa urlilib2 caminho em sring mais arquivo
        url="file://"+caminho+"/" + str(x)
	cont=str(x)
	cont2=cont[0:-4]+"txt"
        arq1 = open(cont2,'w')
        URLObject = urllib2.urlopen(url)
        html = BeautifulSoup(URLObject.read())

        ##extrai e Filtra o conteudo do title
        for node in html.findAll('title'):
            #precisei converter para utf-8
            print >>arq1,''.join(node.findAll(text=True)).encode('utf-8')

        #extrai e Filtra o conteudo do body
        for node in html.findAll('p'):
            #precisei converter para utf-8
            print >>arq1,''.join(node.findAll(text=True)).encode('utf-8')
        arq1.close()
        
