import requests

fileList = requests.get("http://cs7ns1.scss.tcd.ie/index.php/?shortname=nairam&download=noresume_speed").text


for i in fileList.split(',\n'):
    f = requests.get("http://cs7ns1.scss.tcd.ie/index.php/?shortname=nairam&download=noresume_speed&myfilename="+i)
    file = open(i, "wb")
    file.write(f.content)
    file.close()
