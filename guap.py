#-*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate



if __name__ == '__main__':
    name, name2 = [], []
    u = (r"http://portal.guap.ru/portal/priem/priem2019/lists/11_364_BO.html",r"http://portal.guap.ru/portal/priem/priem2019/lists/11_365_BO.html",
         r"http://portal.guap.ru/portal/priem/priem2019/lists/11_366_BO.html",
         r"http://portal.guap.ru/portal/priem/priem2019/lists/11_367_BO.html", r"http://portal.guap.ru/portal/priem/priem2019/lists/11_368_BO.html")
    number = ("02.04.03 Математическое обеспечение и администрирование информационных систем", "09.04.01 Информатика и вычислительная техника",
               "09.04.03 Прикладная информатика", "09.04.04 Программная инженерия", "11.04.04 Электроника и наноэлектроника")
    for url, value in zip(u, number):
        data = requests.get(url)
        if data.status_code != 200:
            raise ConnectionError("Connection interrupted")

        coding = data.content
        data.encoding = coding
        html = data.text

        tree = BeautifulSoup(html, "html.parser")
        students_data = tree.find('tbody')


        name = [[tree.contents[9].contents[1].contents[0].contents[0].contents[0],
              tree.contents[9].contents[1].contents[0].contents[1].contents[0],
              tree.contents[9].contents[1].contents[0].contents[2].contents[0],
              tree.contents[9].contents[1].contents[0].contents[3].contents[0],
              tree.contents[9].contents[1].contents[0].contents[5].contents[0]]]
        for student_data in students_data.find_all('tr'):
            if student_data.contents[1].contents[0] not in name2:
                if  "Кульпин" in student_data.contents[1].contents[0]:
                    print(student_data.contents[1].contents[0], student_data.contents[5].contents[0])


        print(len(name2))
            #name2.append([student_data.contents[0].contents[0],
            #      student_data.contents[1].contents[0],
            #      student_data.contents[2].contents[0],
            #     student_data.contents[3].contents[0],
            #      student_data.contents[5].contents[0]])


