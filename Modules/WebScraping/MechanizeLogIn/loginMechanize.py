import mechanize
from bs4 import BeautifulSoup
import urllib2 
import http.cookiejar ## cookielib in python2

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://id.arduino.cc/auth/login/")

br.select_form(nr=0)
br.form['username'] = 'username'
br.form['password'] = 'password.'
br.submit()

print(br.response().read())