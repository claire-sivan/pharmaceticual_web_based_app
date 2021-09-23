def get_dosages(connection):
    cursor = connection.cursor()
    query = ("SELECT * from dosage")
    cursor.execute(query)

    response = []
    for (dosage_id, dosage_name) in cursor:
        response.append({
            'dosage_id': dosage_id,
            'dosage_name': dosage_name
        })
    return response


if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    print(get_dosages(connection))

