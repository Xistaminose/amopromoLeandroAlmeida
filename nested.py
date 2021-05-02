import json
import pandas as pd

with open('./source-data.json') as access_json:
    read_content = json.load(access_json)

dataframe = pd.DataFrame(read_content)
print(dataframe)

# question_access = read_content['results']

# for question_data in question_access:
#     print(question_data['replies'])