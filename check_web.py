import requests
import sys
def check_web_message(url, expected_text):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        if expected_text in response.text:
            print("Expected message found on the web page.")
            return True
        else:
            print("Expected message NOT found.")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Failed to reach the URL: {e}")
        return False
if __name__ == "__main__":
    url = "http://47.129.248.45:8081"
    expected = "Apache Tomcat" 
    result = check_web_message(url, expected)
    sys.exit(0 if result else 1)
