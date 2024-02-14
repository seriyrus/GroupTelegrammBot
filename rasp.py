import json


raspisanie = {
    "Понедельник":{
            "1 урок": ['lesson1 name', "time1"],
            "2 урок": ['lesson2 name', "time2"],
            "3 урок": ['lesson3 name', "time3"],
            "4 урок": ['lesson4 name', "time4"],
            "5 урок": ['lesson5 name', "time5"],
            "6 урок": ['lesson6 name', "time6"],
            "7 урок": ['lesson7 name', "time7"],
            "8 урок": ['lesson8 name', "time8"],
        },
    "Вторник":{
            "1 урок": ['lesson1 name', "time1"],
            "2 урок": ['lesson2 name', "time2"],
            "3 урок": ['lesson3 name', "time3"],
            "4 урок": ['lesson4 name', "time4"],
            "5 урок": ['lesson5 name', "time5"],
            "6 урок": ['lesson6 name', "time6"],
            "7 урок": ['lesson7 name', "time7"],
            "8 урок": ['lesson8 name', "time8"],
        },
    "Среда":{
            "1 урок": ['lesson1 name', "time1"],
            "2 урок": ['lesson2 name', "time2"],
            "3 урок": ['lesson3 name', "time3"],
            "4 урок": ['lesson4 name', "time4"],
            "5 урок": ['lesson5 name', "time5"],
            "6 урок": ['lesson6 name', "time6"],
            "7 урок": ['lesson7 name', "time7"],
            "8 урок": ['lesson8 name', "time8"],
        },
    "Четверг":{
            "1 урок": ['lesson1 name', "time1"],
            "2 урок": ['lesson2 name', "time2"],
            "3 урок": ['lesson3 name', "time3"],
            "4 урок": ['lesson4 name', "time4"],
            "5 урок": ['lesson5 name', "time5"],
            "6 урок": ['lesson6 name', "time6"],
            "7 урок": ['lesson7 name', "time7"],
            "8 урок": ['lesson8 name', "time8"],
        },
    "Пятница":{
            "1 урок": ['lesson1 name', "time1"],
            "2 урок": ['lesson2 name', "time2"],
            "3 урок": ['lesson3 name', "time3"],
            "4 урок": ['lesson4 name', "time4"],
            "5 урок": ['lesson5 name', "time5"],
            "6 урок": ['lesson6 name', "time6"],
            "7 урок": ['lesson7 name', "time7"],
            "8 урок": ['lesson8 name', "time8"],
        },
}

with open('raspisanie.json', 'w') as rasp:
    json.dump(raspisanie,rasp)
    rasp.close()


