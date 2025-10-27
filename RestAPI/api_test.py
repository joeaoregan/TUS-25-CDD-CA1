import requests
import time 

# URL for REST API to test
IPv4_ADDR = "13.218.220.21"
PORT = "9091"
URL = f"http://{IPv4_ADDR}:{PORT}/couponapi/coupons"

def main():
    for i in range(1, 2501): # Make 100 requests
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
      
