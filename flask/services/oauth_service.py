import requests
from oauthlib.oauth2 import WebApplicationClient

# Google OAuth configuration
# recipefinder oauth 
#yes, this is bad security to store the google 
# oauth keys in the code, but this is a demo project
GOOGLE_CLIENT_ID = "42003689246-4t2lkspfbuaf8kccb99srqrlvlpn807u.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

# OAuth2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)

def get_google_provider_cfg():
    """Fetch Google provider configuration."""
    return requests.get(GOOGLE_DISCOVERY_URL).json()

def fetch_token(code, request_url):
    """Exchange authorization code for access token."""
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request_url,
        redirect_url=request_url.split('?')[0],
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )
    return client.parse_request_body_response(token_response.text)

def fetch_user_info(token):
    """Fetch user information from the token."""
    google_provider_cfg = get_google_provider_cfg()
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    return userinfo_response.json()
