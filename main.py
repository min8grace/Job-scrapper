from flask import Flask, render_template, request, redirect, send_file
from extractors.rok import extractor_rok_jobs
from extractors.wwr import extractor_wwr_jobs
from file import save_to_file

app = Flask("JobScrapper")

#caching
#once the keyword gets searched, then db will store it to pass it over quickly
db = {
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    _keyword = request.args.get("keyword")
    if _keyword == None:

        return redirect("/")
    if _keyword in db:

        _jobs = db[_keyword]
    else:    
        wwr = extractor_wwr_jobs(_keyword)
        rok = extractor_rok_jobs(_keyword)
        _jobs = wwr + rok
        db[_keyword] = _jobs
    return render_template("search.html", keyword = _keyword, jobs = _jobs)

@app.route("/export")
def export():
    _keyword = request.args.get("keyword")
    if _keyword == None:
        return redirect("/")    
    if _keyword not in db:
        return redirect(f"/search?keyword={_keyword}")    
    save_to_file(_keyword, db[_keyword])
    return send_file(f"{_keyword}.csv", as_attachment=True) # as_attachment=True ==> download is allowed

app.run("127.0.0.1")