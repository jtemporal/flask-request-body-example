import json
import httpx


print()
print('Making request: This will fail to pass along the data')
data = {'example': 'data'}
response = httpx.post('http://localhost:5000/', data=data)
print(f'Request data: {response.content}')

print()
print('Making request: This will succeed to pass along the data')
response = httpx.post('http://127.0.0.1:5000/', data=json.dumps(data))
print(f'Resquest data:  {response.content}')
print()