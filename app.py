# Import libraries
from flask import Flask, redirect, request, render_template, url_for

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation: List all transactions
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)
    
# Create operation
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == 'POST':

        transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
        }

        transactions.append(transaction)

        return redirect(url_for("get_transactions"))

    return render_template("form.html")

# Update operation
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == 'POST':

        date = request.form['date']
        amount = float(request.form['amount'])

        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break

            return redirect(url_for("get_transactions"))

        for transaction in transactions:
            if transaction['id'] == transaction_id:
                return render_template("edit.html", transaction=transaction)

# Delete operation
# Delete operation: Delete a transaction
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):

    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break

    return redirect(url_for("get_transactions"))

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)  


@app.route("/search", methods=["GET", "POST"])
def search_transactions():
    if request.method == 'POST':
        min_val = float(request.form['min_amount'])
        max_val = float(request.form['max amount'])

        filtered_transactions = [transaction for transaction in transaction if min_val <= transaction['amount'] <= max_val]

        return render_template('transactions.html', transactions=filtered_transactions)

    return render_template('search.html')

@app.route('/balance')
def total_balance():
    balance = sum(transaction['amount'] for transaction in transactions)
    return f'Total Balance: {str(balance)}'

@app.route('/')
def get_transactions():
    return render_template('transactions.html', transactions=transactions, total_balance=total_balance())

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
   
