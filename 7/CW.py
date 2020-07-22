# import os
#
# print(os.sep)
# print(os.path.dirname(__file__))
#
#
# import json
#
# with open('questions.json', 'r') as file:
#     data = json.load(file)
#
#     for q in data['questions']:
#         q['answer'] = input(q['q'])
#
# with open('questions.json', 'w') as file:
#     json.dump(data, file, indent=4)


# import csv

# data_list = [[1,2], 'kjsndkjcv', [3,4]]
# with open('test.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerows(data_list)

# import yaml
#
# with open('test.yaml') as file:
#     data = yaml.safe_load(file)
#     print(type(data['integer'][0]))
# pip install PyYAML

