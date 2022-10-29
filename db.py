import psycopg2

try:
    connection= psycopg2.connect(
        host='127.0.0.1',
        user='postgres',
        password='',
        database=''
    )

    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE category(
            id serial PRIMARY KEY,
            name varchar(50) NOT NULL,
            description text NOT NULL);'''
        )
        connection.commit()

    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE discounts(
            id serial PRIMARY KEY,
            name varchar(50) NOT NULL,
            percent int NOT NULL);'''
        )
        connection.commit()

    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE product(
            id serial PRIMARY KEY,
            category_id int,
            discounts_id int,
            name varchar(50) NOT NULL,
            price float8 NOT NULL,
            CONSTRAINT FK_product_category FOREIGN KEY(category_id)
                REFERENCES category(id)
                ON DELETE CASCADE,
            CONSTRAINT FK_product_discounts FOREIGN KEY(discounts_id)
                REFERENCES discounts(id)
                ON DELETE CASCADE
                );'''
        )
        connection.commit()

    with connection.cursor() as cursor:
        insert_category="""
        INSERT INTO category(id,name,description)
        VALUES
        (1,'Pivko','For Beginner'),
        (2,'Vodka','For Sport-Masters')"""
        cursor.execute(insert_category)
        connection.commit()
    with connection.cursor() as cursor:
        insert_discount="""
        INSERT INTO discounts (id,name,percent)
        VALUES
        (1,'Pivnoi_day',30),
        (2,'Alko_day',20)"""
        cursor.execute(insert_discount)
        connection.commit()
    with connection.cursor() as cursor:
        insert_product="""
        INSERT INTO product (id,category_id,discounts_id,name,price)
        VALUES
        (1,1,1,'BALTIKA9',3.50),
        (2,2,2,'CBAYAK',9),
        (3,1,1,'ALIVARIYA10',3.0),
        (4,2,2,'LUX',7)"""
        cursor.execute(insert_product)
        connection.commit()
    low_price=float(input('Set a low price:'))
    high_price=float(input('Set a high price:'))
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT *
            FROM product
            RIGHT JOIN discounts ON product.discounts_id=discounts.id
            RIGHT JOIN category ON product.category_id=category.id"""
        )
        records=cursor.fetchall()
        for record in records:
            if record[4] >low_price and record[4] < high_price:
                print(record)
                print('---------------------------------------------')

except Exception as _ex:
    print('[INFO] Error while working with PostgreSQL',_ex)
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection closed')



