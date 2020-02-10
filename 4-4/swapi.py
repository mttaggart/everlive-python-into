"""
SWAPI-CLI: Command-Line interface to the Star Wars API
"""
import requests
import csv

# Define constants
URL_BASE = "https://swapi.co/api/"

# Define endpoints
ENDPOINTS = {
    "ships": "starships",
    "planets": "planets",
    "people": "people"
}

class Result:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        s = ""
        for k in self.data:
            s += "{}: {}\n".format(k, self.data[k])
        s += "\n"
        return s

class Csv:

    @staticmethod
    def generate_headers(results):
        headers = []
        for r in results:
            for k in r.data:
                if k not in headers:
                    headers.append(k)
        return headers
    
    @staticmethod
    def generate_rows(headers, results):
        rows = []
        for r in results:
            row = []
            for h in headers:
                if h in r.data:
                    row.append(r.data[h])
                else:
                    row.append("")
            rows.append(row)
        return rows
    
    def __init__(self, results):
        self.headers = Csv.generate_headers(results)
        self.rows = Csv.generate_rows(self.headers, results)

    def write(self, filename):
        with open(filename, "w") as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)
            writer.writerows(self.rows)


def search(query_type, query_string):
    """Query the correct API endpoint and return a list of results."""
    res = requests.get(URL_BASE + ENDPOINTS[query_type] + "/?search=" + query_string)
    results = list(map(Result, res.json()["results"]))
    return results

