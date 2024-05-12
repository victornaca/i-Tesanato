# injest_api.py

import requests

def fetch_reviews():
    # Define the API endpoint URL
    api_url = "http://127.0.0.1:5000/api/reviews"  # Assuming the API is running locally on port 5000
    
    try:
        # Send GET request to the API endpoint
        response = requests.get(api_url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract JSON data from the response
            reviews_data = response.json()
            return reviews_data
        else:
            print("Error: Unable to fetch reviews. Status code:", response.status_code)
            return None
    except Exception as e:
        print("Error: An exception occurred while fetching reviews:", e)
        return None

def process_reviews(reviews_data):
    # Implement your processing logic here
    if reviews_data:
        # Example: Print the first review
        first_review = reviews_data[0]
        print("First review:", first_review)
    else:
        print("No reviews data received.")

def main():
    print("Fetching reviews from API...")
    reviews_data = fetch_reviews()
    
    print("Processing reviews...")
    process_reviews(reviews_data)

if __name__ == "__main__":
    main()