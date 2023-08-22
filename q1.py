from flask import Flask, request
import urllib.request, urllib.parse, json
app = Flask(__name__)

@app.route('/numbers')
def query_example():
    query = request.args.getlist('url')
    merged_numbers= []
    for url in query:
        if url == 'http://20.244.56.144/numbers/primes' or url == 'http://20.244.56.144/numbers/fibo' or url == 'http://20.244.56.144/numbers/rand' or url == 'http://20.244.56.144/numbers/odd':
            merged_numbers.extend(getUrlResponseData(url))

    unique_numbers = list(set(merged_numbers))
    return f'Unique numbers: {unique_numbers}'

def getUrlResponseData(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return dict["numbers"]

if __name__ == '__main__':
    app.run(debug=True, port=8000)
