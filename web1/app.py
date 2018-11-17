from flask import Flask, render_template #phu trach chay server

app = Flask(__name__) #nho chay chung cac tai nguyen trong cung folder cua app.py

#function binding
@app.route("/") #neu nhu user truy cap vao home page
def home(): #truy cap ngay vao ham home
    return "Hello Flask"

@app.route("/c4e")
def c4e():
    return "Hello c4e, hihi"

@app.route("/chao/<tenban>")
def chao(tenban):
    return "what?"+ tenban

@app.route("/add/<int:x>/<int:y>")
def add(x,y):
    sum = x+y #phep cong khong sai
    return str(sum) #nhung return phai ra string

@app.route("/posts/<int:index>/<int:index1>")
def posts(index, index1):
    titles = [
        "Mua",
        "Nang",
        "Ret",
        "Dep",
    ]
    title = titles[index]

    contents = [
        "toi di dao",
        "toi di tam bien",
        "toi di da bong",
        "toi di xe may",
    ]
    content = contents[index1]
    return render_template("post.html", title = "hom nay troi "+title, content = content)

@app.route("/movie")
def movie():
    return render_template("movie.html", name = "deadpool", image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKxP5yrTOYkXlk_XGaaYOklnqhEb5C_dbx5p2CtLPlHeVuj072")

@app.route("/movies")
def films():
    # film_titles = [
    #     "supaman",
    #     "kongfuang",
    #     "catwoman",
    #     "nick fury",
    #     "charlie",
    # ]
    films_list = [
        {
            "title":"supaman",
            "image":"https://img.maximummedia.ie/joe_ie/eyJkYXRhIjoie1widXJsXCI6XCJodHRwOlxcXC9cXFwvbWVkaWEtam9lLm1heGltdW1tZWRpYS5pZS5zMy5hbWF6b25hd3MuY29tXFxcL3dwLWNvbnRlbnRcXFwvdXBsb2Fkc1xcXC8yMDE4XFxcLzAyXFxcLzAxMTcwNDU1XFxcL1BlYWt5LmpwZ1wiLFwid2lkdGhcIjo3NjcsXCJoZWlnaHRcIjo0MzEsXCJkZWZhdWx0XCI6XCJodHRwczpcXFwvXFxcL3d3dy5qb2UuaWVcXFwvYXNzZXRzXFxcL2ltYWdlc1xcXC9qb2VcXFwvbm8taW1hZ2UucG5nP3Y9NVwifSIsImhhc2giOiJmYTRkMjU1NzI5NTI2NmE3ZGI1MjY5ODJiMjFiM2VhNzA3YTU2ZGIwIn0=/peaky.jpg"
        },
        {
            "title":"kongfuang",
            "image":"https://static.bongda24h.vn/medias/standard/2017/8/19/u22-viet-nam-de-cong-phuong-du-bi-tai-sao-khong.jpg"
        },
        {
            "title":"charlie",
            "image":"https://znews-photo.zadn.vn/w1024/Uploaded/xbhunku/2018_10_06/008.jpg",
        }
    ]

    return render_template("films.html", films = films_list)
if __name__ == "__main__":
    app.run(debug=True)