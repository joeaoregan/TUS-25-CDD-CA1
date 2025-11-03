import requests
import time 

# URL for REST API to test
# IPv4_ADDR = "13.218.220.21"
# IPv4_ADDR = "ec2-98-80-7-17.compute-1.amazonaws.com"
# IPv4_ADDR = "ec2-18-208-251-209.compute-1.amazonaws.com"
# IPv4_ADDR = "ec2-3-91-76-75.compute-1.amazonaws.com"
# IPv4_ADDR = "ec2-54-163-16-200.compute-1.amazonaws.com" # Fibonnaci v2
# IPv4_ADDR = "ec2-13-221-17-181.compute-1.amazonaws.com" # Factorial v2
IPv4_ADDR = "ec2-54-237-139-69.compute-1.amazonaws.com" # Book
PORT = "9091"
URL = f"http://{IPv4_ADDR}:{PORT}/couponapi/coupons"

def main():
    for i in range(1, 1001): # Make 1000 requests
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
      