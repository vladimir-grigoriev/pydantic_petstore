class Config:
    URL = "https://petstore.swagger.io/v2/pet"
    DATA = {"id": 100200300,
        "category": {
            "id": 0,
            "name": "Bobik"
        }, 
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {"id": 0,
            "name": "string"
            }
        ],
        "status": "available"
    }
    HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
        