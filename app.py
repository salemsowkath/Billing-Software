from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    product = data.get("product")
    price = float(data.get("price"))
    quantity = int(data.get("quantity"))

    subtotal = price * quantity
    gst = subtotal * 0.18
    total = subtotal + gst

    return jsonify({
        "product": product,
        "subtotal": subtotal,
        "gst": gst,
        "total": total
    })

if __name__ == "__main__":
    app.run(debug=True)