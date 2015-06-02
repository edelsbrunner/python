"""
Simple script to get the citzen name by its CPF (Brazil's SSN)
"""
from BeautifulSoup import BeautifulSoup as bs
import requests
import urllib2
 
with requests.session() as session:
    url = 'http://www.receita.fazenda.gov.br/aplicacoes/atcta/cpf/ConsultaPublica.asp'
    response = session.get(url)
    element = bs(response.content)
 
    image_url = 'http://www.receita.fazenda.gov.br/scripts/srf/intercepta/captcha.aspx?opt=image&v=123'
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(response.request.cookiejar))
    urllib2.install_opener(opener)
 
    #download image as a file
    url_imagem = urllib2.urlopen(image_url)
 
    #saves the image on disk
    image_file = open('imagem.gif', 'wb')
    image_file.write(url_imagem.read())
    image_file.close()
 
    #ask user to input his/her data
    captcha = raw_input('Digite o captcha:')
    cpf  = raw_input('Digite o cpf:')
 
    #sends the request using the user data
    dados = {'txtCpf':cpf,'idLetra':captcha} 
    response = session.post(url, data=dados)
    element = bs(response.content)
    nome = element.findAll('span',{'class':'clConteudoDados'})[1].string.split(':')[1].lstrip().rstrip()
    print(nome)
