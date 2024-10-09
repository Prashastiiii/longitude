from flask import Flask, render_template, request
from geopy.geocoders import ArcGIS

app = Flask(__name__)
nom = ArcGIS()

@app.route('/', methods=['GET', 'POST'])
def index():
    latitude = None
    longitude = None
    if request.method == 'POST':
        location_name = request.form['location']
        location = nom.geocode(location_name)
        if location:
            latitude = location.latitude
            longitude = location.longitude
        else:
            latitude = "Not found"
            longitude = "Not found"
    return render_template('index.html', latitude=latitude, longitude=longitude)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5006)
