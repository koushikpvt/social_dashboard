import requests

def fetch_user_info(access_token):
    url = "https://graph.threads.net/v1.0/me"
    params = {"fields": "id,name"}
    headers = {"Authorization": f"Bearer {access_token}"}
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

# Example usage:
access_token = "your-access-token"
user_info = fetch_user_info(access_token)
print(user_info)
