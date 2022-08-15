import pandas as pd


def checker(data: pd.DataFrame) -> str:
    """

    :param data:
    :return:
    """
    popularity_idx = data['popularity_idx'][0]
    place_quality = 'neutral'
    # [-0.14500123 - 0.05931483 - 0.01466926  0.03800284  0.21860832]
    if popularity_idx <= -0.05931483:
        place_quality = "bad_place"
    elif -0.05931483 < popularity_idx <= 0.01466926:
        place_quality = "notbad_place"
    elif 0.01466926 < popularity_idx <= 0.03800284:
        place_quality = "good_place"
    elif popularity_idx > 0.03800284:
        place_quality = "perfect_place"

    return place_quality
