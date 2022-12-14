import requests
migrationJobId = ''

sending_tenant_id = ''

auth_token = ''

url = f'https://[INCOMPLETE]/endpoint/v1/migrations/{migrationJobId}/endpoints'

checking_headers = {'Authorization': f'Bearer {auth_token}', 'X-Tenant-ID': sending_tenant_id}

z = requests.get(url, headers = checking_headers)

print(z.text)
print(z.status_code)

json_object = z.text

json_to_dictionary = eval(json_object)

increment = 0

for x in json_to_dictionary['items']:
    increment +=1
    print(x, increment)
