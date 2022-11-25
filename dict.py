import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
            user="postgres",
            password="5731",
            host="localhost",
            port="5432",
            database="dict")
    return conn

def read_dict():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def add_word(word, translation):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
    conn.close()

def delete_word(ID):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
    conn.close()

def save_dict():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("COMMIT;")
    cur.close()
    conn.close()

def insert_word(word, translation):
    print (f"To insert {word} and its translation {translation}, use add instead!")


while True: ## REPL - Read Execute Program Loop
    print("Welcome! To use this dictionary, use the commands list, add, delete or quit!")
    cmd = input("Command: ")
    if cmd == "list":
        print(read_dict())
    elif cmd == "add":
        word = input("  Word: ")
        translation = input("  Translation: ")
        add_word(word, translation)
    elif cmd == "delete":
        ID = input("ID: ")
        delete_word(ID)
    elif cmd == "quit":
        save_dict()
        exit()
