from urllib import request
if __name__ == "__main__":
    response = request.urlopen("https://www.imdb.com/list/ls091520106/")
    html = response.read().decode("utf-8")
    print(html)
    start = html.find('<div class="lister-list">')
    end = html.find('<div class="row text-center lister-working hidden">')
    content = html[start:end]
    file = open('data.js','w',encoding="utf-8")
    file.write('data = ' + '`' + content + '`')