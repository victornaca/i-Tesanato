import requests
import os
import json
from datetime import datetime

def fetch_reviews():
    api_url = "http://127.0.0.1:5000/api/reviews"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            reviews_data = response.json()
            return reviews_data
        else:
            print("Error: Unable to fetch reviews. Status code:", response.status_code)
            return None
    except Exception as e:
        print("Error: An exception occurred while fetching reviews:", e)
        return None

def process_reviews(reviews_data):
    if reviews_data:
        destination_dir = "datalake/landing/api-sentiment-analyze/new/"
        
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
            
        current_datetime = datetime.now()
        datetime_str = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        
        json_file_path = os.path.join(destination_dir, f"reviews_{datetime_str}.json")
        
        with open(json_file_path, "w") as json_file:
            json.dump(reviews_data, json_file, indent=4)
        
        print("All reviews saved as JSON:", json_file_path)
    else:
        print("No reviews data received.")