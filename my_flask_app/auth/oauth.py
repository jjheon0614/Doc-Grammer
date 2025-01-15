""" Filename: oauth.py - Directory: my_flask_app/auth 

This module configures OAuth for a Flask application using Authlib. It initializes
the OAuth object with the application context and registers the Google OAuth client
with necessary details such as client ID, client secret, and various URLs required
for the OAuth flow.

"""
from authlib.integrations.flask_client import OAuth

oauth = OAuth()


def configure_oauth(app):
    """
    Configures OAuth for the Flask application using Authlib.

    This function initializes the OAuth object with the application context and
    registers the Google OAuth client with necessary details such as client ID,
    client secret, and various URLs required for the OAuth flow.

    Args:
        app (Flask): The Flask application instance to configure with OAuth.
    """
    oauth.init_app(app)
    oauth.register(
        name="google",
        client_id="your-google-oauth-client-id",
        client_secret="your-google-oauth-client-secret",
        access_token_url="https://oauth2.googleapis.com/token",
        authorize_url="https://accounts.google.com/o/oauth2/auth",
        api_base_url="https://www.googleapis.com/oauth2/v1/",
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        client_kwargs={"scope": "openid email profile"},
    )