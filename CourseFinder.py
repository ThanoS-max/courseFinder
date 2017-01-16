import urllib
import urllib.request
from bs4 import BeautifulSoup

theurl = "http://registrar.indiana.edu/browser/soc4172/index.shtml"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")

print(soup.title.text)

dept = input('Please enter a department: ')
dept = dept.upper()


while True:
    
    level = input('Graduate or Undergraduate: ')
    level = level.lower()
    
    if level == 'graduate':
        level = 'grad'
        break

    if level == 'grad':
        level = 'grad'
        break
   
    if level == 'undergraduate':
        level ='under'
        break
    
    if level == 'under':
       level ='under'
       break

    else:
        print ('That\'s not valid. Please enter "Graduate" or "Undergraduate"')


theurl2 = "http://registrar.indiana.edu/browser/soc4172/" + dept + "/index.shtml"
thepage2 = urllib.request.urlopen(theurl2)
soup2 = BeautifulSoup(thepage2, "html.parser")


if level == 'grad':
    for link in soup2.findAll('a'):
        if link.text[:4] == str(dept):
            if link.text[-3] in (str('5'),str('6'),str('7'),str('8'),str('9')):
                print(link.text)
    
if level == 'under':
    for link in soup2.findAll('a'):
        if link.text[:4] == str(dept):
            if link.text[-3] in (str('1'),str('2'),str('3'),str('4')):
                print(link.text)               
