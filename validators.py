from __future__ import annotations
import requests

from pydantic import BaseModel

from config import Config


class Category(BaseModel):
    id: int
    name: str


class Tag(BaseModel):
    id: int
    name: str


class ModelItem(BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: list
    tags: list[Tag]
    status: str


class Model(BaseModel):
    __root__: list


def send_request_for_pets_with_status(status):
    response = requests.get(
        url=Config.URL + "/findByStatus",
        params={"status": status}
    )
    status_code = response.status_code
    data = Model.parse_raw(response.text).dict()
    return status_code, data

def get_pet_by_id():

    response = requests.get(
        url=Config.URL + "/" + str(Config.DATA["id"]),
        headers=Config.HEADERS
    )
    response_text = response.text
    data = ModelItem.parse_raw(response_text).dict()
    return response.status_code, data
