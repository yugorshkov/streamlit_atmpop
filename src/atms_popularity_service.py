import requests
import pandas as pd


def send_request(data: pd.DataFrame) -> pd.DataFrame:
    """
    Function sends a request to remote server with model to assess the quality of ATM placement
    :param data: Prepared DataFrame with features based on object geolocation
    :return: DataFrame with ids and popularity indexes of the place
    """
    data = data.set_index("id")

    host = "81.163.27.44"
    port = "8080"
    url = f"http://{host}:{port}/invocations"

    headers = {"Content-Type": "application/json"}
    http_data = data.to_json(orient="split")

    response = requests.post(url=url, headers=headers, data=http_data)

    return pd.DataFrame({"id": list(data.index), "popularity_idx": response.json()})
