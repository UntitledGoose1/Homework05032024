from csv import DictReader
with open("FIOandTelephone.csv", "r", encoding="utf-8-sig") as file:
    data = DictReader(file)
    name = input("Введите ФИО")
    for row in data:
        if name == row["FIO"]:
            print("Телефон человека",row["Telephone"])
        else:
            continue
