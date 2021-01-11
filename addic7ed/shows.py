import requests

from addic7ed.constants import ADDIC7ED_URL
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from termcolor import colored

"http://www.addic7ed.com/search.php?search=bless+this+mess"


class Shows:
    def __init__(self):
        print(colored("Fetching shows list, please wait...", "yellow"))
        data = requests.get(ADDIC7ED_URL + "/search.php").text
        soup = BeautifulSoup(data, "html.parser")
        self.list = [str(x.text) for x in
                     soup.find(id="qsShow").find_all("option")]

    def get(self, name):
        return process.extractOne(name, self.list)[0]
"""

        data = requests.get("http://www.addic7ed.com/search.php?search=bless+this+mess").text
        soup = BeautifulSoup(data, "html.parser")
        rows = soup.select('table.tabel tr>td:nth-child(2)>a')
        rows[0].get_text()
        rows[0].get('href')
        urljoin("http://www.addic7ed.com/search.php?search=bless+this+mess", rows[0].get('href'))
"""
