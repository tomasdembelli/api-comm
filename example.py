from api_comm import ApiComm

base_url = 'https://api.sandbox.transferwise.tech'
read_token = '246s7d15-3af3-2dc2-8584-8a52df3f6f83'


# Create a read-only client.
read_client = ApiComm(
            base_url=base_url,
            token=read_token,
            token_type='Bearer',
            headers={"Content-Type": "application/json"})

# connect method returns a requests.Response() object.
# With json method, response can be converted to a JSON object.
profiles = read_client.connect(
            method='get',
            path='v1/profiles').json()

print(profiles)            

'''
[
  {
    "id": 217896,
    "type": "personal",
    "details": {
      "firstName": "Oliver",
      "lastName": "Wilson",
      "dateOfBirth": "1977-07-01",
      "phoneNumber": "+3725064992",
      "avatar": "https://lh6.googleusercontent.com/-XzeFZ2PJE1A/AAAAAAAI/AAAAAAAAAAA/RvuvhXFsqs0/photo.jpg",
      "occupation": null,
      "primaryAddress": 236532
    }
  },
  {
    "id": 220192,
    "type": "business",
    "details": {
      "name": "ABC Logistics Ltd",
      "registrationNumber": "12144939",
      "acn": null,
      "abn": null,
      "arbn": null,
      "companyType": "LIMITED",
      "companyRole": "OWNER",
      "descriptionOfBusiness": "Information and communication",
      "primaryAddress": 240402,
      "webpage": "https://abc-logistics.com"
    }
  }
]
'''          
