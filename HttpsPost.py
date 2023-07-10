import concurrent.futures
import requests
import time

# Get input from the user
url = input("Enter the URL: ")
num_requests = int(input("Enter the number of requests: "))
num_threads = int(input("Enter the number of threads: "))

# Define the data to send (if applicable)
data = {'key': 'value'}  # Modify as per your requirements

# Define the function to send a POST request and print the response along with time spent
def send_request(data):
    start_time = time.time()
    response = requests.post(url, data=data)
    end_time = time.time()
    # Process the response
    print(response.text)
    print(f"Time spent: {end_time - start_time} seconds")

# Record the start time of the program
program_start_time = time.time()

# Create a ThreadPoolExecutor with the specified number of threads
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Submit the requests to the executor
    futures = [executor.submit(send_request, data) for _ in range(num_requests)]

    # Wait for all the requests to complete
    concurrent.futures.wait(futures)

# Record the end time of the program
program_end_time = time.time()

# Calculate and print the total time spent for the program
total_time = program_end_time - program_start_time
print(f"Total time spent: {total_time} seconds")
