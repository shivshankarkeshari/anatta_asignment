

import sys

import requests
from bs4 import BeautifulSoup


def get_res_txt(url, req_type):
    try:
        r = requests.request(req_type.upper(), url, headers={"User-Agent": "PostmanRuntime/7.26.8"})
    except Exception as e:
        return ""
    print(r.status_code)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.get_text()

def convert_args_into_dict(sys_args):
    input_dict = {}
    for arg in sys.argv:
        arg = arg.replace("--", "")
        if"=" in arg:
            if arg.split("=")[-1].split(",").__len__()>1:
                input_dict[arg.split("=")[0]] = arg.split("=")[-1].split(",")
            else:
                input_dict[arg.split("=")[0]] = arg.split("=")[-1]

    return input_dict


def return_final_output():
    data = convert_args_into_dict((sys.argv))
    res = get_res_txt(data.get("url"), "GET").lower()
    tem_dict = {}
    for o in data.get("words", []):
        try:
            tem_dict[o] = res.count(o.lower())
        except:
            tem_dict[o] = None

    return tem_dict


# print(convert_args_into_dict(sys.argv))
print(return_final_output())