import streamlit as st
import mysql.connector

# Define the SQL queries
queries = [
    "SELECT * FROM Customer;",
    "SELECT * FROM Seller;",
    "SELECT * FROM InStock;",
    "SELECT * FROM not_in_stock;",
    "SELECT * FROM items;",
    "INSERT INTO Customer (customer_name, phone_number) VALUES ('John Doe', '+1234567890');",
    "INSERT INTO InStock (item_id, quantity) VALUES (1, -10);",
    "INSERT INTO InStock (item_id, quantity) VALUES (500, 1);",
    "UPDATE InStock SET quantity = 0 WHERE item_id = 1;",
    "SELECT s.seller_name, i.category, SUM(b.quantity*b.price) AS sales FROM Seller s  JOIN Seller_Inventory si ON s.seller_id = si.seller_id JOIN Items i ON si.item_id = i.item_id JOIN Bill b ON si.seller_id = b.seller_id AND si.item_id = b.item_id GROUP BY s.seller_id, i.category;",
    "SELECT i.item_name, SUM(b.quantity*b.price) AS sales FROM Items i JOIN Bill b ON i.item_id = b.item_id  WHERE i.category = 'Books' GROUP BY i.item_id;",
    "SELECT i.category, SUM(b.quantity*b.price) AS sales FROM Items i JOIN Bill b ON i.item_id = b.item_id GROUP BY i.category WITH ROLLUP;",
    "SELECT i.category, i.item_name, SUM(b.quantity * b.price) AS total_sales FROM Bill b JOIN Items i ON b.item_id = i.item_id GROUP BY i.category, i.item_name WITH ROLLUP;"
]


# Define a function to create a database connection
def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pokemon18@",
        database="Amazon_clone",
        autocommit = True
    )
    return connection


# Define a function to execute the SQL queries and display the results
def execute_query(query):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(query)
    results = cur.fetchall()
    st.write(results)
    cur.close()
    conn.close()


# Create the Streamlit app
def main():
    st.title("Amazon_clone Database")

    # Display a dropdown menu to select a SQL query
    selected_query = st.selectbox("Select a query", queries)

    # Execute the selected SQL query when the user clicks the "Run Query" button
    if st.button("Run Query"):
        execute_query(selected_query)


if __name__ == "__main__":
    main()
