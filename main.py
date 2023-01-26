from flask import Flask, render_template, request, redirect, url_for
from test import write_block, check_integrity

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def block():

  if request.method == 'POST':
    lender = request.form.get('lender')
    amount = request.form['amount']
    borrower = request.form['borrower']

    write_block(name=lender, amount=amount, to_whom=borrower)
    return redirect(url_for('block'))
  
  return render_template('index.html')

@app.route('/check', methods=['GET'])
def check():
  results = check_integrity()
  return render_template('index.html', results=results)

if __name__ == '__main__':
  app.run(debug=True)