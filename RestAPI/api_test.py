import requests
import time 

# URL for REST API to test
URL = "http://54.88.89.80:9091/couponapi/coupons"

def main():
    for i in range(1, 101): # Make 100 requests
        start = time.time()
        try:
            response = requests.get(URL, timeout=5) # GET request
            elapsed = time.time() - start
            print(f"Request {i}: {response.status_code} in {elapsed:.3f}s")
        except requests.exceptions.RequestException as e:
            elapsed = time.time() - start
            print(f"Request {i}: FAILED after {elapsed:.3f}s - {e}")


if __name__ == "__main__":
    main()
