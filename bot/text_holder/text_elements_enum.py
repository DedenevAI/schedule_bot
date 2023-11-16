import enum


class ButtonsName(enum.Enum):
    schedule_main = "хочу узнать расписание!🎫"
    author = "автор🖥"
    schedule = ["расписание по потоку", "расписание по преподователю"]
    graduate = {"Д": "дневная", "В": "вечерняя", "З": "заочная", "2": "второе высшее",
                "М": "магистратура", "А": "аспирантура", "У": "дистанционное"}
    kurs = {"1": "курс 1", "2": "курс 2", "3": "курс 3", "4": "курс 4",
            "5": "курс 5", "6": "курс 6"}
    srok = {"today": "на сегодня/завтра", "week": "на неделю", "month": "на месяц", "sem": "на семестр"}
    again = "хочу посмотреть расписание еще раз:/return"