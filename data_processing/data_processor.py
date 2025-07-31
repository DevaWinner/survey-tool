import os
import csv
from pymongo import MongoClient

class UserDataProcessor:
    """
    A class to handle fetching user data from MongoDB and saving it to a CSV file.
    """
    def __init__(self, db_uri, db_name, collection_name):
        """Initializes the data processor with MongoDB connection details."""
        try:
            self.client = MongoClient(db_uri)
            self.db = self.client[db_name]
            self.collection = self.db[collection_name]
            # Test connection
            self.client.admin.command('ping')
            print("Successfully connected to MongoDB.")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            self.collection = None

    def fetch_all_users(self):
        """Fetches all documents from the user collection."""
        if self.collection is None:
            return []
        return list(self.collection.find({}, {'_id': 0}))

    def save_to_csv(self, users_data, file_path):
        """Saves a list of user data dictionaries to a CSV file."""
        if not users_data:
            print("No data to save.")
            return

        # Define all possible headers to ensure CSV consistency
        headers = ['first_name', 'last_name', 'age', 'gender', 'total_income', 'utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']
        
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headers, extrasaction='ignore')
                writer.writeheader()
                for user in users_data:
                    writer.writerow(user)
            print(f"Data successfully saved to {file_path}")
        except IOError as error:
            print(f"Error writing to file {file_path}: {error}")

if __name__ == "__main__":
    # --- Configuration ---
    MONGO_URI = "mongodb://localhost:27017/"
    DB_NAME = "survey_db"
    COLLECTION_NAME = "users"
    
    # Define output path relative to this script
    current_dir = os.path.dirname(__file__)
    CSV_PATH = os.path.join(current_dir, '..', 'analysis', 'user_data.csv')
    
    # Create the analysis directory if it doesn't exist
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)

    # --- Processing ---
    processor = UserDataProcessor(MONGO_URI, DB_NAME, COLLECTION_NAME)
    all_users = processor.fetch_all_users()
    processor.save_to_csv(all_users, CSV_PATH)
