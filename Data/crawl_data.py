import argparse
import requests
import json
from bs4 import BeautifulSoup, NavigableString, Tag


def setFile(filename, is_append):
    if is_append:
        mod = "a+"
        bra = ']'
    else:
        mod = "w"
        bra = '['
    with open(filename, mod) as f:
        f.writelines(bra)


def writeFile(filename, data, deli):
    with open(filename, "a+", encoding="utf-8") as f:
        f.writelines(deli)
        json.dump(data, f, indent=2, ensure_ascii=False)


def addContents(contents, data):
    for header in contents.find_all('h3'):
        nextNode = header
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, NavigableString):
                pass
            if isinstance(nextNode, Tag):
                if nextNode.name == "h3":
                    break
                data[header.text] = nextNode.get_text(strip=True).strip()


def getListOfLink(begin, end):
    links = []
    for i in range(begin, end + 1):
        links.append("https://www.topcv.vn/tim-viec-lam-it-phan-mem-c10026?salary=0&exp=0&company_field=0&sort=up_top&page=" + str(i))
    return links


def getTittles(list_link):
    titles = []
    for link in list_link:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.findAll('h3', class_='title')
        for tit in title:
            titles.append(tit)
    return titles


def getLinkCompany(titles):
    links_company = []
    for link_company in titles:
        link_obj = link_company.find('a', class_="underline-box-job", href=True)
        if link_obj != None:
            link = link_obj['href']
            links_company.append(link)
    return links_company


def crawlContents(filename, links_company):
    setFile(filename, False)
    deli = ""

    for link in links_company:
        news = requests.get(link)
        soup = BeautifulSoup(news.content, "html.parser")
        names_obj = soup.find('a', class_="company-logo")
        if names_obj == None:
            continue
        names = names_obj.attrs["title"]
        contents = soup.find("div", class_="job-data")

        data = {}
        data['name'] = names
        addContents(contents, data)

        writeFile(filename, data, deli)
        deli = ",\n"
        print(data)
    setFile(filename, True)


if __name__ == "__main__":
    # create parser
    print("Parsing Args")
    parser = argparse.ArgumentParser()
    parser.add_argument("begin")
    parser.add_argument("end")
    args = parser.parse_args()

    print("begin crawling from ", args.begin, " to ", args.end)
    links = getListOfLink(int(args.begin), int(args.end))
    print("list of links")
    print(links)
    title = getTittles(links)
    links_company = getLinkCompany(title)
    print(links_company)
    filename = "recruit_" + args.begin + "_" + args.end + ".json"
    crawlContents(filename, links_company)