import json
import requests


string = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

string_json = json.dumps(string, indent= 4) # THIS IS STRING
#print("string_json:", string_json, "||| type:", type(string_json))

loads_json = json.loads(string_json) # THIS IS JSON 
#print("load_json:", loads_json, "||| type:", type(loads_json))

with open("C:\\Sandbox\\my-dev-repo\\Python sandbox\\dumps_json.json", "w+") as f:
    json.dump(string_json, f)



with open("C:\\Sandbox\\my-dev-repo\\Python sandbox\\loads_json.json", "w+") as f:
    json.dump(loads_json, f)



response = requests.get("https://jsonplaceholder.typicode.com/todos")

todos = json.loads(response.text)

with open("C:\\Sandbox\\my-dev-repo\\Python sandbox\\todos.json", "w+") as f:
    json.dump(todos, f, indent=4, sort_keys=True)



with open("C:\\Sandbox\\my-dev-repo\\Python sandbox\\todos.json", "r") as f:
    newJsonLoad = json.load(f)

userIdCompl = {}

for obj in newJsonLoad:
    if obj["completed"]:
        try:
            #increment count of completed if user exists
            userIdCompl[obj["userId"]] += 1
        except KeyError:
            userIdCompl[obj["userId"]] = 1



sortedUsers = dict(sorted(userIdCompl.items()
                         ,key=lambda item: item[1]
                         ,reverse=True)
                   )

#maxCompleted = values(sortedUsers[0]) 
sortedUsersDict = dict(sortedUsers)

#Find max number of completed tasks
maxCompleted = max(sortedUsers.values())

#Find userId(s) with max number of completed tasks
maxComplUserId = dict(filter(lambda a: a[1]==maxCompleted, sortedUsers.items())).keys()


maxCompUserIdList = list(maxComplUserId)
string_ints = [str(i) for i in maxCompUserIdList]

textToPrint = " and ".join(string_ints)


print(textToPrint)



#stworzyc dict
#policzyc ile completed = true ma kazdy userId
#posortowac po ilości "completed"



#print(type(newJsonLoad[0]))

#print(type(newJsonLoad))









def todos():
    todos = json.loads(response.text)
    todos_by_user = {}

    # Increment complete TODOs count for each user.
    for todo in todos:
        if todo["completed"]:
            try:
                # Increment the existing user's count.
                todos_by_user[todo["userId"]] += 1
            except KeyError:
                # This user has not been seen. Set their count to 1.
                todos_by_user[todo["userId"]] = 1

    print("1", todos_by_user)

    # Create a sorted list of (userId, num_complete) pairs.
    top_users = sorted(todos_by_user.items(), 
                    key=lambda x: x[1], reverse=True)

    print("top_users:", top_users)

    # Get the maximum number of complete TODOs.
    max_complete = top_users[0][1]

    # Create a list of all users who have completed
    # the maximum number of TODOs.
    users = []
    for user, num_complete in top_users:
        if num_complete < max_complete:
            break
        users.append(str(user))

    max_users = " and ".join(users)


    print(max_users)


#todos()
'''
with open("test_file_json2.json","r") as f:
    data2 = json.load(f)

data3 = json.dumps(data)

data4 = json.loads(data3)


json_string = json.dumps(data, indent=4)

json_string["president"]["name"] = "test"

print(data4)
'''