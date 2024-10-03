import requests

# Define class `MegaverseAPI` to capture the API functionalities
class MegaverseAPI:
    BASE_URL = "https://challenge.crossmint.io/api"  # Base URL for the API

    # Initialize the class with the candidate_id to be used in the API requests
    def __init__(self, candidate_id):
        self.candidate_id = candidate_id

    # Define a function to post a Polyanet to a specific (row, column) on the Megaverse grid
    def post_polyanet(self, row, column):
        url = f"{self.BASE_URL}/polyanets"
        payload = {
            "candidateId": self.candidate_id,
            "row": row,
            "column": column
        }
         # Send a POST request to create the Polyanet at the specified position
        response = requests.post(url, json=payload)
        return response.json()
    
     # Define a function to delete a Polyanet from a specific (row, column) on the Megaverse grid
    def delete_polyanet(self, row, column):
        url = f"{self.BASE_URL}/polyanets"
        payload = {
            "candidateId": self.candidate_id,
            "row": row,
            "column": column
        }

        # Send a DELETE request to remove the Polyanet at the specified position
        response = requests.delete(url, json=payload)
        return response.json()
    
     # Define a function to get the goal map from the API
    def get_goal_map(self):
        url = f"{self.BASE_URL}/map/7054d957-9b30-487d-b6cf-e7dab57080c9/goal"
        response = requests.get(url)  # Send a GET request to retrieve the goal map
        return response.json()
    
# Function to manage Polyanets based on specific positions (rows, columns) for deletion
def manage_polyanets(candidate_id):
    api = MegaverseAPI(candidate_id)
    positions_to_delete = [(6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (8, 7)]

# Iterate over the list of positions and delete the Polyanet at each specified position
    for row, column in positions_to_delete:
        api.delete_polyanet(row, column)

# Call the manage_polyanets function with the candidate ID to initiate the deletion process  
manage_polyanets("7054d957-9b30-487d-b6cf-e7dab57080c9")
