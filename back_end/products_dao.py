from sql_connection import get_sql_connection


def get_all_products(connection):
    cursor = connection.cursor()

    query = ("SELECT products.product_id, products.name, products.stock,products.price,dosage.dosage_name FROM "
             "products "
             "inner join dosage ON  products.dosage_id=dosage.dosage_id")

    cursor.execute(query)

    response = []

    for (product_id, name, stock, price, dosage_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'stock': stock,
                'price': price,
                'dosage_name': dosage_name
            })

    return response


# def update_product(connection,product):
#     cursor = connection.cursor()
#     query = ("""UPDATE products "
#              SET name = % s,
#              SET stock = % s,
#              SET price = % s
#              SET dosage_id = % s,
#              WHERE product_id = % s"""
#      # data = (name, stock, price, dosage_id)
#     data = (product['product_name'], product['stock'], product['price'], product['dosage_id'])

                 # update book title
    cursor.execute(query, data)
    # accept the changes
    connection.commit()




def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "( name, stock, price, dosage_id)"
             "VALUES (%s,%s,%s,%s)")
    data = (product['product_name'], product['stock'], product['price'], product['dosage_id'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()


if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 7))
