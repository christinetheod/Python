import requests
url = input("Give url")
resp = requests.get(url)
txt = resp.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(resp.txt, 'lxml')

# The number of `<p>` tags.
p = len(soup.find_all('p'))

#The number of `<br>` tags.
br = len(soup.find_all('br'))

#The number of `<href>` tags.
href = len(soup.find_all('href'))

# The number of `<p>`  and '<br>' tags.
pANDbr = p + p

print("O ari8mos twn links einai: ")
print (href)
print("O ari8mos twn allagwn grammis einai: ")
print(pANDbr)

