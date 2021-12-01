from datetime import datetime


def show_duty():
    text = "Черговий: "
    with open("duty.txt", "r", encoding="utf-8") as file_read:
        text += file_read.readline()
        ls = []
        for line in file_read.readlines():
            ls.append(line[:-1])
        if len(ls):
            text += "Також проживають: "
            for i in ls[:-1]:
                text += i + ", "
            text += ls[-1]
        else:
            text += "Більше ніхто не проживає"
    return text


def add_roommate(name: str):
    with open("duty.txt", "r", encoding="utf-8") as file_read:
        for line in file_read.readlines():
            if name == line[:-1]:
                return f"Жилець з таким іменем уже проживає"
            elif name == "":
                return "Ім'я не вказано"
    with open("duty.txt", "a", encoding="utf-8") as file_write:
        file_write.write(name + '\n')
        return f"Жильця {name} додано до списку чергових"


def delete_roommate(name: str):
    ls = []
    flg = False
    with open("duty.txt", "r", encoding="utf-8") as file_read:
        for line in file_read.readlines():
            if name == line[:-1]:
                flg = True
            else:
                ls.append(line)
    if flg:
        with open("duty.txt", "w", encoding="utf-8") as file_write:
            for el in ls:
                file_write.write(el)
        return f"Жильця {name} видалено"
    else:
        return f"Жильця під іменем {name} не знайдено"

def change_duty():
    ls = []
    with open("duty.txt", "r", encoding="utf-8") as file_read:
        for line in file_read.readlines():
            ls.append(line)
    if len(ls):
        ls.append(ls[0])
        del ls[0]
        with open("duty.txt", "w", encoding="utf-8") as file_write:
            for el in ls:
                file_write.write(el)
        return f"Черговий на цей тиждень тепер {ls[0]}"
    else:
        return "У кімнаті немає жильців для чергування"


def distribution(date: datetime):
    Date = date.strftime("%d/%m/%Y %H:%M:%S").split()[0].split('/')
    Time = date.strftime("%d/%m/%Y %H:%M:%S").split()[1].split(':')
    Day = date.weekday()
    with open("duty.txt", "r", encoding="utf-8") as file_read:
        duty = file_read.readline()[:-1]

    if Day == 5 and Time[:2] == ["15", "00"]:
        return f"{duty}, пора позамітати"
    elif Day == 6 and Time[:2] == ["13", "00"]:
        return f"{duty}, пора постірати речі"
    elif ((Day == 6 and Day >= abs(30 - int(Date[0])) and Date[0] != '31') or (Day == 6 and Day >= abs(28 - int(Date[0])) and Date[1] == '02')) and Time[:2] == ["11", "00"]:
        return f"Хлопці, може генералочку зробимо? {duty} візьметься за підлогу"
    elif Day == 6 and Time[:2] == ["20", "00"]:
        return change_duty()
    else:
        return ""
