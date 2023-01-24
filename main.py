import os

import requests
import wget

URL_UPLOAD = "https://api.lottiefiles.com/v2/temp-file-upload"
URL_CONVERT = "https://api.dotlottie.io/todotlottie"
S3_STORAGE = "https://lottie-editor-api-temp.s3.amazonaws.com/"

files = os.listdir("./files")
print(files)

for f in files:
    file = open("./files/"+f)
    content = file.read()
    print(content)

    r = requests.post(URL_UPLOAD, {
        "payload": content
    })

    if r.status_code == 200:
        response = r.json()
        file_url = response["payload"]["data_file"]
        print(file_url)
        toLottie = requests.post(URL_CONVERT, json={
            "url": file_url
        })
        print(toLottie)
        if toLottie.status_code == 200:
            re = S3_STORAGE + toLottie.json()["file"]
            wget.download(re, "./converted/"+f.split(".")[0]+".lottie")
