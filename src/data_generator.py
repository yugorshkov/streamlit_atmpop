import pandas as pd


def generate_data(
    city: str,
    distance: float,
    bank: float,
    cafe: float,
    stores: float,
    pois: float,
) -> pd.DataFrame:
    """

    :param city:
    :param distance:
    :param bank:
    :param cafe:
    :param stores:
    :param pois:
    :return:
    """
    test_line = pd.DataFrame(
        {
            "atm": [0.0],
            "attraction": [0.0],
            "bank": [bank],
            "bar": [0.0],
            "bureau_de_change": [0.0],
            "bus_station": [0.0],
            "bus_stop": [0.0],
            "cafe": [0.0],
            "clinic": [0.0],
            "college": [0.0],
            "dentist": [0.0],
            "fast_food": [0.0],
            "fuel": [0.0],
            "geo_city": [city],
            "hospital": [0.0],
            "hotel": [0.0],
            "ice_cream": [0.0],
            "id": ["test_line"],
            "marketplace": [0.0],
            "near_atm_dist": [distance],
            "office": [0.0],
            "parking": [0.0],
            "payment_terminal": [0.0],
            "pharmacy": [0.0],
            "photostudio": [0.0],
            "pois_cnt": [pois],
            "post_office": [0.0],
            "pub": [0.0],
            "public_building": [0.0],
            "restaurant": [cafe],
            "shop": [stores],
            "theatre": [0.0],
            "townhall": [0.0],
            "train_station": [0.0],
            "university": [0.0],
            "veterinary": [0.0],
        }
    )
    test_line = test_line[
        [
            "id",
            "atm",
            "attraction",
            "bank",
            "bar",
            "bureau_de_change",
            "bus_station",
            "bus_stop",
            "cafe",
            "clinic",
            "college",
            "dentist",
            "fast_food",
            "fuel",
            "hospital",
            "hotel",
            "ice_cream",
            "marketplace",
            "office",
            "parking",
            "payment_terminal",
            "pharmacy",
            "photostudio",
            "post_office",
            "pub",
            "public_building",
            "restaurant",
            "shop",
            "theatre",
            "townhall",
            "train_station",
            "university",
            "veterinary",
            "pois_cnt",
            "near_atm_dist",
            "geo_city",
        ]
    ]

    return test_line


def get_cities_list():
    cities = [
        "г Москва",
        "г Нижний Новгород",
        "г Казань",
        "г Воронеж",
        "г Саратов",
        "г Краснодар",
        "г Тольятти",
        "г Ярославль",
        "г Тула",
        "г Волгоград",
        "г Ульяновск",
        "г Курск",
        "г Белгород",
        "г Пенза",
        "г Иваново",
        "г Ростов-на-Дону",
        "г Тверь",
        "г Чебоксары",
        "г Сочи",
        "г Ставрополь",
        "г Брянск",
        "г Тамбов",
        "г Астрахань",
        "г Йошкар-Ола",
        "г Липецк",
        "г Мытищи",
        "г Владимир",
        "г Рязань",
        "г Рыбинск",
        "г Калуга",
        "г Сызрань",
        "г Балашиха",
        "г Новомосковск",
        "г Красногорск",
        "г Старый Оскол",
        "г Химки",
        "г Элиста",
        "г Одинцово",
        "г Кострома",
        "г Новороссийск",
        "г Волжский",
        "г Саранск",
        "г Пятигорск",
    ]
    return cities
