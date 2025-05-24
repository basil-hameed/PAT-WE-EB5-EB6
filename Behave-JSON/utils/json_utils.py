import json

# read the json data by passing the file path
def read_json_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# write the test results into the json file
def write_test_result(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)