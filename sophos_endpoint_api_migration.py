import requests
import json
client_id = input("Client ID:")
client_secret = input("Client secret:")
payload = f'grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}&scope=token'
uri = 'https://id.sophos.com/api/v2/oauth2/token'
unauthorized_header = {'Content-Type':'application/x-www-form-urlencoded'}

x = requests.post(uri, data = payload, headers = unauthorized_header)

access_dictionary = eval(x.text)
auth_token = access_dictionary['access_token']
authorized_header = {'Authorization':f'Bearer {auth_token}'}

y = requests.get('https://api.central.sophos.com/whoami/v1', headers = authorized_header)

tenant_dictionary = eval(y.text)
tenant_id = tenant_dictionary['id']
tenant_region = tenant_dictionary['apiHosts']['dataRegion']

print("Tenant ID:", tenant_id, "Region:", tenant_region, "Auth Token:", auth_token)

request_endpoints_header = {'Authorization':f'Bearer {auth_token}','X-Tenant-ID':tenant_id}

endpoint_url = f'{tenant_region}/endpoint/v1/endpoints'

z = requests.get(endpoint_url, headers = request_endpoints_header)

print(z.text)
print(z.status_code)
