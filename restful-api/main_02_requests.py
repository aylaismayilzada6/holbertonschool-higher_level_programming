from task_02_requests import fetch_and_print_posts, fetch_and_save_posts

if __name__ == "__main__":
    print("Fetch and Print Titles ")
    fetch_and_print_posts()
    
    print("\nFetch and Save to CSV ")
    fetch_and_save_posts()
    print("Check your folder for posts.csv!")
