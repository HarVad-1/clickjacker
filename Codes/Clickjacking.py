import requests

def check_clickjacking_protection(url):
    try:
        response = requests.get(url)
        headers = response.headers
        
        x_frame_options = headers.get('X-Frame-Options', None)
        csp = headers.get('Content-Security-Policy', None)

        if x_frame_options:
            print(f"X-Frame-Options: {x_frame_options}")
            if x_frame_options.upper() in ['DENY', 'SAMEORIGIN']:
                print("X-Frame-Options header is properly set to prevent clickjacking.")
            else:
                print("X-Frame-Options header is set but might not be effective for clickjacking protection.")
        else:
            print("X-Frame-Options header is missing.")

        if csp:
            print(f"Content-Security-Policy: {csp}")
            if 'frame-ancestors' in csp:
                print("Content-Security-Policy header with frame-ancestors directive is set to prevent clickjacking.")
            else:
                print("Content-Security-Policy header is set but does not contain frame-ancestors directive for clickjacking protection.")
        else:
            print("Content-Security-Policy header is missing.")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the URL to check for clickjacking protection: ")
    check_clickjacking_protection(url)

