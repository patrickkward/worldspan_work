import requests
import sys
import re
import json

# token:
# 4IUYNhfpNMPcgC36oJuf

token = "4IUYNhfpNMPcgC36oJuf"
header = {"Authorization": 'Bearer {}'.format(token)}

response = requests.get("https://the-one-api.herokuapp.com/v1/movie", headers=header)

if response:
    print("Response Successful! " + str(response.status_code))
    retrieved_val = response.text
else:
    print("Response Failure! " + str(response.status_code))
    sys.exit(response.status_code)

retrieved_val = retrieved_val.split(",\"academyAwardWins\"")
award_amount = 0
temp_film = ""
film = ""

for i in range(0, len(retrieved_val) - 1):
    temp_award_amount = ""
    for j in reversed(retrieved_val[i]):
        if j == ':':
            temp_award_amount = int(temp_award_amount)
            if temp_award_amount > award_amount:
                award_amount = temp_award_amount
                try:
                    film = re.search('name\":(.+?),\"', retrieved_val[i]).group(1)
                except AttributeError:
                    print("An error has occurred")
            break
        else:
            temp_award_amount = j + temp_award_amount

print(film, "with ", award_amount, " nominations!")
