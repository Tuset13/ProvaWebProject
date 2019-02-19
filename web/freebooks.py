from urllib.request import urlopen
import bs4

class FreeBooks(object):
    """Veure el nou llibre que ens ofereix Packt"""
    def __init__(self):
        super(FreeBooks, self).__init__()
        pass

    def descarregar_html(self):
        f = urlopen("https://www.packtpub.com/packt/offers/free-learning/")
        html = f.read()
        f.close()
        return html

    def buscar_info_llibre(self, html):
        arbre = bs4.BeautifulSoup(html, 'html.parser')
        informacio = arbre.find("div", "product__right")
        print(informacio)
        #print (informacio)
        bookInfo = []
        #for info in informacio:
            #title = info.find("span", "flink-title")
            #link = info.find("li")
            #bookInfo.append((title.text, link["href"]))
        return bookInfo

    def run(self):
        #Descarregar-me html
        html = self.descarregar_html()
        infoLlibre = self.buscar_info_llibre(html)
        #print(infoLlibre)

if __name__ == "__main__":
    f = FreeBooks()
    f.run()
