import json

from contextlib import suppress


class RouterException(Exception):
    pass


class RestAPI:
    def __init__(self, database=None):
        if database is None:
            self._database = {
                "users": []
            }
        else:
            self._database = database

        self._routers = {
            "GET": ["/users"],
            "POST": ["/add", "/iou"]
        }

        self._template = {
            "name": None,
            "owes": {},
            "owed_by": {},
            "balance": 0.0
        }

    def get(self, url, payload=None):

        if url not in self._routers['GET']:
            raise RouterException(url, "Not found")

        if url == "/users":
            try:
                payload = json.loads(payload)
            except TypeError:
                payload = {"users": []}

            response = {
                "users": [self._load_user(user) for user in payload["users"]]
            }

        return json.dumps(response)

    def post(self, url, payload=None):

        if url not in self._routers['POST']:
            raise RouterException(url, "Not found")

        response = {}

        with suppress(TypeError):
            payload = json.loads(payload)

            if url == "/add":
                user = payload["user"]
                response = self._load_user(user)
                if not response:
                    response = self._template
                    response["name"] = user
                    self._save_user(response)

            elif url == '/iou':
                lender = payload["lender"]
                borrower = payload["borrower"]
                amount = payload["amount"]

                result = self._calc_debt(lender, borrower, amount)

                response = {
                    "users": sorted(
                        result,
                        key=lambda x: x["name"]
                    )
                }

                for entry in result:
                    self._save_user(entry)

        return json.dumps(response)

    def _load_user(self, name):
        for data in self._database["users"]:
            if data["name"] == name:
                return data

        return {}

    def _save_user(self, user_data):
        for index, data in enumerate(self._database["users"]):
            if data["name"] == user_data["name"]:
                break
        else:
            self._database["users"].append(user_data)
            return

        self._database["users"][index] = user_data

    def _calc_debt(self, lender, borrower, amount):

        lender_data = self._load_user(lender)
        borrower_data = self._load_user(borrower)

        # lender calc

        if borrower in lender_data["owed_by"]:
            lender_data["owed_by"][borrower] += amount
        elif borrower in lender_data["owes"]:
            lender_data["owes"][borrower] -= amount

            if lender_data["owes"][borrower] < 0:
                lender_data["owed_by"][borrower] = \
                    abs(lender_data["owes"][borrower])

                del lender_data["owes"][borrower]
            elif lender_data["owes"][borrower] == 0:
                del lender_data["owes"][borrower]

        else:
            lender_data["owed_by"][borrower] = amount

        lender_data["balance"] += amount

        # borrower calc

        if lender in borrower_data["owes"]:
            borrower_data["owes"][lender] += amount
        elif lender in borrower_data["owed_by"]:
            borrower_data["owed_by"][lender] -= amount

            if borrower_data["owed_by"][lender] < 0:
                borrower_data["owes"][lender] = \
                    abs(borrower_data["owed_by"][lender])

                del borrower_data["owed_by"][lender]
            elif borrower_data["owed_by"][lender] == 0:
                del borrower_data["owed_by"][lender]

        else:
            borrower_data["owes"][lender] = amount

        borrower_data["balance"] -= amount

        return [
            lender_data,
            borrower_data
        ]
