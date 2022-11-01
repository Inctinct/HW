import psycopg2

try:
    connection= psycopg2.connect(
        host='127.0.0.1',
        user='postgres',
        password='252515Mdd',
        database='testdb1'
    )
    ex=1
    while ex == 1:
        choice=int(input('1.Создать базу данных\n2.Добавить в базу продукт\n3.Добавить категорию\n4.Добавить скидку\n5.Выборка по цене'))
        if choice == 1:
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
        if choice == 2:
            category=int(input('Введите id категории товара: '))
            discounts=int(input('Введите id скидки: '))
            name_product=input('Введите название товара: ')
            price=float(input('Введите цену товара'))
            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT MAX(id) FROM product"""
                )
                max_id_product=cursor.fetchone()
                max_id_product=max_id_product[0]+1
            with connection.cursor() as cursor:
                insert_product = f"""
                INSERT INTO product (id,category_id,discounts_id,name,price)
                VALUES
                ({max_id_product},{category},{discounts},'{name_product}',{price})"""
                cursor.execute(insert_product)
                connection.commit()
        if choice == 3:
            name_category=input('Введите название категории: ')
            description=input('Введите описание: ')
            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT MAX(id) FROM category"""
                )
                max_id_category=cursor.fetchone()
                max_id_category=max_id_category[0]+1
            with connection.cursor() as cursor:
                insert_category=f"""
                INSERT INTO category (id,name,description)
                VALUES
                ({max_id_category},{name_category},{description})"""
                cursor.execute(insert_category)
                connection.commit()
        if choice == 4:
            name_discounts=input('Введите название скидки: ')
            percent=int(input('Введите размер скидки: '))
            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT MAX(id) FROM discounts"""
                )
                max_id_discounts=cursor.fetchone()
                max_id_discounts=max_id_discounts[0]+1
            with connection.cursor() as cursor:
                insert_discount=f"""
                INSERT INTO discounts (id,name,percent)
                VALUES
                ({max_id_discounts},{name_discounts},{percent})"""
                cursor.execute(insert_discount)
                connection.commit()
        if choice == 5:
            low_price = float(input('Set a low price:'))
            high_price = float(input('Set a high price:'))
            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT *
                    FROM product
                    RIGHT JOIN discounts ON product.discounts_id=discounts.id
                    RIGHT JOIN category ON product.category_id=category.id"""
                )
                records = cursor.fetchall()
                for record in records:
                    if record[4] > low_price and record[4] < high_price:
                        print(record)
                        print('---------------------------------------------')
        ex=int(input('1.Продолжить\n2.Выход'))
except Exception as _ex:
    print('[INFO] Error while working with PostgreSQL',_ex)
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection closed')
