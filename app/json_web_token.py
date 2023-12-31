from django.conf import settings
from dataclasses import dataclass

import jwt


@dataclass
class JsonWebToken:
    """Perform JSON Web Token (JWT) validation using PyJWT"""

    jwt_access_token: str
    auth0_issuer_url: str = f"https://{settings.AUTH0_DOMAIN}/"
    auth0_audience: str = settings.AUTH0_AUDIENCE
    algorithm: str = "RS256"
    jwks_uri: str = f"https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json"

    def validate(self):
        try:
            jwks_client = jwt.PyJWKClient(self.jwks_uri)
            jwt_signing_key = jwks_client.get_signing_key_from_jwt(
                self.jwt_access_token
            ).key
            payload = jwt.decode(
                self.jwt_access_token,
                jwt_signing_key,
                algorithms=self.algorithm,
                audience=self.auth0_audience,
                issuer=self.auth0_issuer_url,
            )

        # TODO: fix error handling
        except jwt.exceptions.PyJWKClientError:
            print("UnableCredentialsException")
            return "UnableCredentialsException"
        except jwt.exceptions.InvalidTokenError:
            print("BadCredentialsException")
            return "BadCredentialsException"
        return payload
