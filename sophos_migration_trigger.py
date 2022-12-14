import requests
import json

endpoints_list = ['']

sending_tenant_id = ''

migration_job_id = ''

migration_job_token = ''

auth_token = ''

url = '[INCOMPLETE]endpoint/v1/migrations/'

url_with_job = url + migration_job_id

payload_before_dump = {'token': migration_job_token, 'endpoints': endpoints_list}

payload = json.dumps(payload_before_dump)

trigger_headers = {'Authorization': f'Bearer {auth_token}', 'X-Tenant-ID': sending_tenant_id}

x = requests.put(url_with_job, data = payload, headers = trigger_headers)

print(x.text)
print(x.status_code)
