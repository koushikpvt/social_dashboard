import requests

def get_user_data(access_token):
    api_url = "https://graph.threads.net/v1.0/me?fields=id,name"
    headers = {'Authorization': f'Bearer {access_token}'}
    
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching user data:", e)
        return None