import requests
import json
resp = requests.get('http://localhost:8000/showdata/').json()
print(type(resp))
print(resp)
# for i in resp:
#     print(i['show']['ID'])
#     print(i['show']['Title'])
#     print(i['show']['Contributors'])
#     print(i['show']['ISWC'])
#     print(i['show']['Source'])
#     print(i['show']['Song'])
