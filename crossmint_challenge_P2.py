import requests
import json
import time

# Function to retrieve the goal map
def get_map(candidate_id):
    api_url = f"https://challenge.crossmint.io/api/map/{candidate_id}/goal"

    # Make a GET request to retrieve the map and extract the 'goal' data
    return requests.get(api_url).json().get('goal')

#Function to send a POST request
def post_request(api_url, data):
    # Define headers for the request, specifying JSON format
    headers = {"Content-Type": "application/json"}
    try:
        # Send the POST request with data in JSON format
        requests.post(api_url, data=json.dumps(data), headers=headers)
    except requests.exceptions.RequestException as e:
        # Send the POST request with data in JSON format
        print(f"Error posting data: {e}")

#Function to send a DELETE request
def delete_request(api_url, data):
    headers = {"Content-Type": "application/json"}
    try:
        requests.delete(api_url, data=json.dumps(data), headers=headers)
    except requests.exceptions.RequestException as e:
        print(f"Error deleting data: {e}")

# Function to add a Polyanet at a specified row and column
def post_polyanet(candidate_id, row, col):
    post_request("https://challenge.crossmint.io/api/polyanets", {"row": row, "column": col, "candidateId": candidate_id})

# Function to add a Soloon at a specified row, column, and color
def post_soloon(candidate_id, row, col, color):
    post_request("https://challenge.crossmint.io/api/soloons", {"row": row, "column": col, "color": color, "candidateId": candidate_id})

# Function to add a Cometh at a specified row, column, and direction
def post_cometh(candidate_id, row, col, direction):
    post_request("https://challenge.crossmint.io/api/comeths", {"row": row, "column": col, "direction": direction, "candidateId": candidate_id})

# Function to delete a Polyanet at a specified row and column
def delete_polyanet(candidate_id, row, col):
    delete_request("https://challenge.crossmint.io/api/polyanets", {"row": row, "column": col, "candidateId": candidate_id})

# Function to delete a Soloon at a specified row and column
def delete_soloon(candidate_id, row, col):
    delete_request("https://challenge.crossmint.io/api/soloons", {"row": row, "column": col, "candidateId": candidate_id})

# Function to delete a Cometh at a specified row and column
def delete_cometh(candidate_id, row, col):
    delete_request("https://challenge.crossmint.io/api/comeths", {"row": row, "column": col, "candidateId": candidate_id})

 # Main function to execute the process
def main():
    candidate_id = "7054d957-9b30-487d-b6cf-e7dab57080c9"
    
    # Get the goal map
    goal_map = get_map(candidate_id)

    # Loop through each cell in the map
    for row in range(len(goal_map)):
        for col in range(len(goal_map[0])):
        
            # Get the value of the current cell in the goal map
            goal_value = goal_map[row][col]
            current_objects = []

            # If the cell should be empty ("SPACE"), delete any existing object
            if goal_value == "SPACE":
                delete_polyanet(candidate_id, row, col)
                delete_soloon(candidate_id, row, col)
                delete_cometh(candidate_id, row, col)
            else:
                # Add the correct object
                goal_value = goal_value.lower()
                if goal_value == "polyanet":
                    post_polyanet(candidate_id, row, col)
                else:
                    obj_type, obj_name = goal_value.split("_")
                    if obj_name == "soloon":
                        post_soloon(candidate_id, row, col, obj_type)
                    elif obj_name == "cometh":
                        post_cometh(candidate_id, row, col, obj_type)

            # Add a delay to avoid overloading the API
            time.sleep(1)

# Execute the main function when the script is run directly.
if __name__ == "__main__":
    main()
