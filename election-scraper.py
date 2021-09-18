import requests
from bs4 import BeautifulSoup
import xlsxwriter



def main(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html.parser", from_encoding="utf8")
    workbook = xlsxwriter.Workbook('projekt_3.xlsx')
    worksheet = workbook.add_worksheet()
    m = q = s = 1

    voh(soup,worksheet)
    zapis_cisla(soup,worksheet,q,m)
    volebni_strany(worksheet,workbook)
def voh(soup,worksheet):
    m = 1
    n = 1
    celkem_list = []

    for tag in soup.find_all("a"):
        kod = str(tag.string)
        if kod.isdigit():
            m += 1

            URL1 = f"https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec={kod}&xvyber=7103"
            r = requests.get(URL1)
            soup1 = BeautifulSoup(r.content, "html.parser", from_encoding="utf8")
            for neco in soup1.find_all("td",class_="cislo",headers="t1sa2 t1sb3"):
                celkem = neco.get_text()
                celkem_list.append(celkem)
            for neco in soup1.find_all("td",class_="cislo",headers="t2sa2 t2sb3"):
                celkem1 = neco.get_text()
                celkem_list.append(celkem1)

            worksheet.write_row(n,5,celkem_list)
            celkem_list = []
            n += 1
            volici = soup1.find("td", class_="cislo", headers="sa2")
            obalky = soup1.find("td", class_="cislo", headers="sa3")
            hlasy_ok = soup1.find("td", class_="cislo", headers="sa5")

            volici = volici.get_text()
            obalky = obalky.get_text()
            hlasy_ok = hlasy_ok.get_text()
            worksheet.write(f"A{m}", kod)
            worksheet.write(f"C{m}", volici)
            worksheet.write(f"D{m}", obalky)
            worksheet.write(f"E{m}", hlasy_ok)
            zapis_nazvy(worksheet)


def zapis_nazvy(worksheet):
    hlavicka = ["KOD","JMENO","VOLICI","OBALKY","HLASY"]
    worksheet.write_row(0,0,hlavicka)

def zapis_cisla(soup,worksheet,q,m):
    q = 1
    for tag in soup.find_all("td", headers="t1sa1 t1sb2"):
        jmeno = tag.get_text()
        q += 1
        worksheet.write(f"B{q}", jmeno)

    for tag in soup.find_all("td", headers="t2sa1 t2sb2"):
        jmeno1 = tag.get_text()
        q += 1
        worksheet.write(f"B{q}", jmeno1)

    for tag in soup.find_all("td", headers="t3sa1 t3sb2"):
        jmeno2 = tag.get_text()
        q += 1
        if jmeno2 != "-":
            worksheet.write(f"B{q}", jmeno2)
def volebni_strany(worksheet,workbook):
    URL2 = "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=506761&xvyber=7103"
    r = requests.get(URL2)
    soup = BeautifulSoup(r.content, "html.parser", from_encoding="utf8")

    list_stran = []

    for tag in soup.find_all("td", headers="t1sa1 t1sb2"):
        strany = tag.get_text()
        list_stran.append(strany)
    for tag in soup.find_all("td", headers="t2sa1 t2sb2"):
        strany1 = tag.get_text()
        list_stran.append(strany1)

    worksheet.write_row(0, 5, list_stran)

    workbook.close()


main("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7101")
