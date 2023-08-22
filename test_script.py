import requests
test_urls = [
    "http://20.244.56.144/numbers/primes",
    "http://abc.com/fibo"
]

microservice_url = "http://localhost:8008/numbers"

params = {'url': test_urls}
response = requests.get(microservice_url, params=params)

if response.status_code == 200:
    data = response.json()
    combined_numbers = data['numbers']

    third_url = "http://20.244.56.144/numbers/odd"
    response_third = requests.get(third_url)

    if response_third.status_code == 200:
        data_third = response_third.json()
        combined_numbers.extend(data_third['number'])

        unique_numbers = list(set(combined_numbers))
        unique_numbers.sort()

        print("Unique numbers:", unique_numbers)
    else:
        print("Request failed with status code:", response_third.status_code)
else:
    print("Request failed with status code:", response.status_code)
