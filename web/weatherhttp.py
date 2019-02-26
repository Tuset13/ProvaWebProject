from urllib.request import urlopen
import bs4
import xmltodict
import json
import pprint

class WeatherClient(object):
    """Veure el temps que ens ofereix OpenWeather"""
    def __init__(self):
        super(WeatherClient, self).__init__()

    def do_request(self):
        f = urlopen("https://api.openweathermap.org/data/2.5/find?q=Lleida&units=metric&mode=json&appid=928c5cf213ebd781ade87ca8cbfeeee6")
        data = f.read()
        f.close()
        return data

#    def process_weather(self, html):
#        arbre = bs4.BeautifulSoup(html, features='lxml')
#        temperature = arbre.find("temperature")
#        weather = arbre.find("weather")
#        return(temperature["value"] + " and " + weather["value"])

    def process_weather(self, html):
        dic = json.loads(html)
        pprint.pprint(dic)
        temp = dic['list'][0]['main']['temp']
        weath = dic['list'][0]['weather'][0]['description']
        return (str(temp) + " and " + weath)

    def run(self):
        #Descarregar-me html
        data = self.do_request()
        data2 = self.process_weather(data)
        #print(infoLlibre)
        print(data2 )

if __name__ == "__main__":
    w = WeatherClient()
    w.run()
