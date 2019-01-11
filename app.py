from flask import Flask, render_template
import requests

app = Flask(__name__)
app.debug = True

def get_data():
    try:
        url = "http://worker1.datastream.center:9000/stat"
        r = requests.get(url)
    except requests.HTTPError as e:
        raise PipelineServiceError("{reason}".format(reason=e))
    return r.json()

@app.route('/')
def main_page():
    return render_template("table.html", data=get_data())


if __name__ == '__main__':
    app.run()
