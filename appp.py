from flask import Flask,render_template,request,redirect
import youtube_dl

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')    

@app.route('/download',methods=["POST","GET"])
def download():
    url = request.form["url"]
    print("Someone is trying to download",url)
    with youtube_dl.YoutubeDL() as ydl:
        url=ydl.extract_info(url,download=False)
        #print(url)
        download_link=(url["formats"][-1]["url"])
        return redirect(download_link+"&dl=1")
       




if __name__ == '__main__':
	app.run(debug=True)