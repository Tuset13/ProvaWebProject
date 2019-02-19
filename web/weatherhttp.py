from urllib.request import urlopen
import bs4

class WeatherClient(object):
    """Veure el temps que ens ofereix OpenWeather"""
    def __init__(self):
        super(WeatherClient, self).__init__()
        pass

    def do_request(self):
        f = urlopen("https://api.openweathermap.org/data/2.5/find?q=Lleida&units=metric&mode=xml&appid=928c5cf213ebd781ade87ca8cbfeeee6")
        data = f.read()
        f.close()
        return data

    def process_weather(self, html):
        arbre = bs4.BeautifulSoup(html, features='lxml')
        temperature = arbre.find("temperature")
        weather = arbre.find("weather")
        print(temperature["value"] + " and " + weather["value"])

        return None

    def run(self):
        #Descarregar-me html
        data = self.do_request()
        data2 = self.process_weather(data)
        #print(infoLlibre)

if __name__ == "__main__":
    w = WeatherClient()
    w.run()
