import requests # type: ignore
import csv

def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder and prints their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        # Parse the JSON response into a Python list of dictionaries
        posts = response.json()
        
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    """Fetches all posts and saves id, title, and body to a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        
        # Prepare the list of dictionaries with only the required fields
        # Using a list comprehension for efficiency and readability
        processed_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        # Define the CSV file name and the header (fieldnames)
        filename = "posts.csv"
        fieldnames = ['id', 'title', 'body']

        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                # Write the header row
                writer.writeheader()
                # Write all post data
                writer.writerows(processed_data)
        except IOError as e:
            print(f"An error occurred while writing to the CSV: {e}")