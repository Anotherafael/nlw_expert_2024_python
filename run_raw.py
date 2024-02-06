from barcode import Code128
from barcode.writer import ImageWriter
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/create-tag", methods=["POST"])
def create_tag():
    body = request.json
    product_code = body.get("product_code")

    tag = Code128(product_code, writer=ImageWriter())
    path_from_tag = f"{tag}"
    tag.save("tag.png")

    return jsonify({"tag_path": path_from_tag})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
