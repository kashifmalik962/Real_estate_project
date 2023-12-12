from flask import Flask,jsonify,request,render_template,url_for
import util

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def main():
    if request.method=='POST':
        total_sqft = float(request.form['total_sqft'])
        bath = int(request.form['bath'])
        bhk = int(request.form['bhk'])
        location = request.form['location']
        response = util.get_estimated_price(total_sqft,bath,bhk,location)
        if response:
            predict_val = abs(response)
            # formatted_number = "{:,}".format(predict_val)
            # formatted_number = formatted_number.replace(",", ",")
            return jsonify('\u20B9',predict_val)
        return "Please provide a valid detail"
    return render_template('home.html')


@app.route('/location')
def location():
    response = jsonify({
        'locations': util.location()
    })
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Pridiction...")
    app.run(debug=True)