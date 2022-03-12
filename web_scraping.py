from bs4 import BeautifulSoup
import requests
# objeto recenbo todo o conteudo da requisicao htto do site
site = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp/").content
#objeto soup baixando do site o html
soup  = BeautifulSoup(site, 'html.parser')
#convert html em string
print(soup.prettify())

# temperature_min = soup.find("span", class_="-gray-light", id_="min-temp-1")
# print(temperature_min.string)
# temperature_max = soup.find("span", class_="-gray-light", id_="max-temp-1")
# print(temperature_max.string)

# scraping data from the site
print(soup.title.string)
print(soup.find('admin'))

#busca temperaturas máximas e mínimas from the city
temperature_max = soup.find("span", id="max-temp-1")
print(temperature_max.string)
temperature_min = soup.find("span", id="min-temp-1")
print(temperature_min.string)

