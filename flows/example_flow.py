from prefect import flow, task
import time
import requests

@task
def wait():
    time.sleep(5)
    return "Waited for 5 seconds"

@flow(name = "Example Flow")
def example_flow():
    print("Starting the example flow...")
    
    # Call the wait task
    result = wait()
    
    print(result)
    
    # Example of making an HTTP request
    response = requests.get("https://api.github.com")
    print(f"GitHub API response status code: {response.status_code}")
    
    return "Flow completed successfully"

if __name__ == "__main__":
    example_flow()