from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


def get_res_txt(url, req_type):
    try:
        r = requests.request(req_type.upper(), url, headers={"User-Agent": "PostmanRuntime/7.26.8"})
    except Exception as e:
        return ""
    print(r.status_code)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.get_text()

@app.route('/', methods=["POST"])
def hello():
    data = request.get_json()
    res = get_res_txt(data.get("url"), "GET").lower()
    tem_dict = {}

    for o in data.get("words"):
        try:
            tem_dict[o] = res.count(o.lower())
        except:
            tem_dict[o] = None
    return {
        "type": "success",
        "body": request.get_json(),
        "response": tem_dict
    }

if __name__ == "__main__":
    app.run(debug=True)