from flask import Flask, render_template, request
from extractors.rok import extractor_rok_jobs
from extractors.wwr import extractor_wwr_jobs

app = Flask("JobScrapper")

#caching
#once the keyword gets searched, then db will store it to pass it over quickly
db = {
}

@app.route("/")
def home():
    return render_template("home.html", name = "nico")

@app.route("/search")
def search():
    _keyword = request.args.get("keyword")
    if _keyword in db:
        jobs = db[_keyword]
    else:    
        wwr = extractor_wwr_jobs(_keyword)
        rok = extractor_rok_jobs(_keyword)
        # print(wwr)
        # print(rok)
        _jobs = wwr + rok
        db[_keyword] = jobs
    return render_template("search.html", keyword = _keyword, jobs = _jobs)
app.run("127.0.0.1")