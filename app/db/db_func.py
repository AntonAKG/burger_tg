import psycopg2

class DBConnect:
    def __init__(self):
        self.conn = psycopg2.connect(
            database='burger',
            user='postgres',
            password='1801',
            host='localhost',
            port='5432'
        )

        self.cursor = self.conn.cursor()

        self.conn.autocommit = True

    def show_products_data(self):
        self.cursor.execute("""SELECT * from products""")

    def insert_category(self, add_category_name: str) -> None:
        self.cursor.execute("""INSERT INTO category (category_name) VALUES  (%s)""", (add_category_name,))

    def show_category_data(self, show_category_name: str) -> list:
        self.cursor.execute("""SELECT category_name FROM category WHERE category_name = %s""", (show_category_name,))
        result = self.cursor.fetchall()
        return result

    def get_products_by_category(self, get_category_name: str) -> list:
        self.cursor.execute("""
            SELECT p.product_name, p.description, p.price
            FROM products p
            JOIN category c ON p.category_id = c.category_id
            WHERE c.category_name = %s
        """, (get_category_name,))
        result = self.cursor.fetchall()
        return result

    def new_user(self, email: str, first_name: str, last_name: str, phone_number: str):
        self.cursor.execute("""INSERT INTO users (email, first_name, last_name, phone_number) VALUES (%s, %s, %s, %s)""", (email, first_name, last_name, phone_number))

    def insert_data_product(self, product_name:str, description:str, price:float, category_id:int):
        ...

    # def is_au

db = DBConnect()
# db.insert_category('coffee')

category_name = 'coffee'  # Назва категорії
print(type(db.show_category_data(category_name)))

products = db.get_products_by_category(category_name)
for product in products:
    print(product)