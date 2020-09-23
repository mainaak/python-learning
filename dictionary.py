myFirstJson = {
    "userDetails": {
        "id": 1234,
        "fname": "Mainaak",
        "lname": "Aanand",
        "cars": [{
            "make": "Volkswagen",
            "model": "Vento"
        }, {
            "make": "Honda",
            "model": "City"
        }]
    },
    "contactInformation": {
        "numbers": [8447048569, 9873097170, 8447822383],
        "emailId": "mainaak@gmail.com"
    }
}

print(myFirstJson["userDetails"]["cars"][1]["make"])
print(myFirstJson.get("contactInformation", "this prints if key was not found"))
