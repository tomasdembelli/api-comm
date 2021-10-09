# api-comm
HTTP client focusing on communications with APIs.

Example usage for creating a `GET` request to `https://api.sandbox.transferwise.tech/v1/profiles`.
[Source](https://api-docs.transferwise.com/#payouts-guide-get-your-profile-id)

1. Create a client
```python
from api_comm import ApiComm

client = ApiComm(
            base_url='https://api.sandbox.transferwise.tech',
            token='my-secret-token',   # it is advised to read this from a config file or an environment variable
            token_type='Bearer',
            headers={"Content-Type": "application/json"})
```

2. Call `connect()` method on the client for a given resource path. This method will return `requests.Response()`. See [w3 resource](https://www.w3schools.com/PYTHON/ref_requests_response.asp) for more.
```python            

# connect method returns a requests.Response() object.
profiles = client.connect(
            method='get',
            path='v1/profiles')
```
3. Call `json()` method to get the response in JSON format.
```python
profiles.json()
# example output
'''
[
  {
    "id": 217896,
    "type": "personal",
    "details": {
      "firstName": "Oliver",
    ...
    }
  },
  {
    "id": 220192,
    "type": "business",
    "details": {
      "name": "ABC Logistics Ltd",
    ...
    }
  }
]
'''   
```

4. Reuse the client for creating a `POST` to `https://api.sandbox.transferwise.tech/v1/transfers`.
[Source](https://api-docs.transferwise.com/#payouts-guide-create-transfer)
```python
import json

data = {
    'targetAccount': '12345',
    'quote': '123',
    'customerTransactionId': '5678',
}

transfer = client.connect(
    method='post',
    path='transfers',
    data=json.dumps(data))  
    
transfer.status_code  # 201
transfer.json()
# example output
'''
{
    "id": 468956,
    "user": <your user id>,
    "targetAccount": <recipient account id>,
    "sourceAccount": null,
    ...
    "customerTransactionId": "bd244a95-dcf8-4c31-aac8-bf5e2f3e54c0"
}
'''

```
