from flask import Flask, request, jsonify
from flask_cors import CORS
import products_dao
import dosage_dao
import json
from sql_connection import get_sql_connection
import orders_dao

app = Flask(__name__)
CORS(app)

connection = get_sql_connection()


@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getDOSAGE', methods=['GET'])
def get_dosage():
    response = dosage_dao.get_dosages(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# @app.route('/updateProduct', methods=['POST'])
# def update_product():
#     request_payload = json.loads(request.form['data'])
#     product_id = products_dao.insert_new_product(connection, request_payload)
#     response = jsonify({
#         'product_id': product_id
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response


@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Qwklife _Pharma_Store ")
    app.run(port=5000)
