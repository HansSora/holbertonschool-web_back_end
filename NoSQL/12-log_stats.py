from pymongo import MongoClient

if __name__ == "__main__":
    # Connect to the MongoDB server
    client = MongoClient()

    # Specify the database and collection
    db = client.logs
    collection = db.nginx

    # Count the total number of documents in the collection
    total_logs = collection.count_documents({})

    # Count the number of documents for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    # Count the number of documents where method is GET and path is /status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

    # Display the results
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check_count} status check")
