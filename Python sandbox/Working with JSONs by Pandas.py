import requests
import pandas as pd
import json

if not(path.exists("C:\\Sandbox\\my-dev-repo\\Python sandbox\\Json_Pandas.json")):
    #pull json file from jsonplachholder
    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    #load data from response to a dataframe variable
    todos = json.loads(response.text)

    #Save data in json file
    with open("C:\\Sandbox\\my-dev-repo\\Python sandbox\\Json_Pandas.json", "w+") as f:
        json.dump(todos, f, indent = 4, sort_keys=True)

#load data from file to a dataframe variable
df = pd.read_json("C:\\Sandbox\\my-dev-repo\\Python sandbox\\Json_Pandas.json")

#limit the dataframe to "userId" and "completed" columns
df = df[['userId', 'completed']]

#limit the rows to those with 'completed' == True
#Count the number of rows for each userId and rename the default's column name to "count_compl_true)
#       .groupby(['userId']).agg(count_compl_true=('completed','count'))
agg_df = df[df['completed']==True].groupby(['userId']).agg(count_compl_true=('completed','count'))
'''
        count_compl_true
userId
1                     11
2                      8
3                      7
4                      6
5                     12
6                      6
7                      9
8                     11
9                      8
10                    12
'''

#get the maximum number of count_compl_true from dataframe
s_max_completed = agg_df.agg({'count_compl_true' : ['max']})
'''
     count_compl_true
max                12
'''

#get max count_compl_true as an integer
l_v_max_completed = s_max_completed.iloc[0][0]
'''
12
'''

#get userId's based on the max number of "completed"
ids_w_max = agg_df[agg_df['count_compl_true']==l_v_max_completed]
'''
        count_compl_true
userId
5                     12
10                    12

pandas.core.frame.DataFrame
'''

#change the dataframe of integers to a list of strings
#HOW TO CHANGE INT LIST TO STR LIST
#METHOD 1
str_arr = []
for i in list(ids_w_max.index):
    str_arr.append(str(i))

#METHOD 2
str_arr2 = list(map(str, ids_w_max.index))


print('Users with maximum number of completed todos are',' and '.join(str_arr))
print('Users with maximum number of completed todos are',' and '.join(str_arr2))
