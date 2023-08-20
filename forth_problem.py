import requests

url = 'https://ipinfo.io/ips'
response = requests.get(url)

if response.status_code == 200:
    ip_list = response.text.split('\n')
else:
    print("Failed to fetch the IP list.")

target_ip = input("Type the IP address ,pls: ")


if target_ip in ip_list:
    print(f'{target_ip} is in the list.')
else:
    print(f'{target_ip} is not in the list.')
