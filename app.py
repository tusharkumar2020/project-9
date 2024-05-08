# Import libraries
from flask import Flask,request,render_template,redirect,url_for
# Instantiate Flask functionality
app = Flask(__name__)
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]
# Read operation
@app.route("/")
def get_transactions():
    return render_template("transactions.html",transactions=transactions)

# Create operation
@app.route("/add",methods=["GET", "POST"])
def add_transaction():
    if request.method == 'POST':
        # Create a new transaction object using form field values
        transaction = {
              'id': len(transactions) + 1,
              'date': request.form['date'],
              'amount': float(request.form['amount'])
             }

        #Append the new transaction to the list
        transactions.append(transaction)

        #Redirect to the transactions list
        return redirect(url_for("get_transactions"))

    # Render the form template to display the add transaction form
    return render_template("form.html")


# Update operation
@app.route("/edit/<int:transaction_id>",methods=["GET","POST"])
def edit_transaction(transaction_id):
    
    if request.method == 'POST':
        #Extract the updated values from the form fields
        date = request.form['date']
        amount = float(request.form['amount'])

        #Find the transaction matching ID & update its values
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break
        
        #Redirect to the transactions list page
        return redirect(url_for("get_transactions"))
    
    #Find the transactions with the matching ID and render the edit form
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template("edit.html", transaction=transaction)


# Delete operation
@app.route('/delete/<int:transaction_id>',methods=['DELETE'])
def delete_transaction(transaction_id):
    #Find transaction with matching ID
    for transaction in transactions:
        if transaction['ID'] == transaction_id:
            transactions.remove(transaction)
            break
    
    #Redirect to the transaction list page
    return redirect(url_for("get_transactions"))

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)