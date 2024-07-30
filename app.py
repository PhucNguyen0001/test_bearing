import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)
df = pd.read_csv('bi-cau.csv')

def format_number(val):
    if isinstance(val, float) and val.is_integer():
        return str(int(val))
    else:
        return str(val)

def search(d_bore=None, d_outside=None, b=None):
    if not d_bore and not d_outside and not b:
        return None
    records = df
    if d_bore:
        records = records[records['d bore'] == float(d_bore)]

    if d_outside:
        records = records[records['D outside'] == float(d_outside)]

    if b:
        records = records[records['B'] == float(b)]

    return records.to_dict(orient='records')



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search1():
    d_bore = request.args.get('d bore', None)
    d_outside = request.args.get('D outside', None)
    b = request.args.get('B', None)

    result = search(d_bore, d_outside, b)

    for record in result:
        for key, value in record.items():
            record[key] = format_number(value)


    return render_template('search.html', result=result)



if __name__ == '__main__':
    # print(search(d_outside=3))
    app.run()
