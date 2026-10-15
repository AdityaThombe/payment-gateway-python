"""Gateway configuration."""

PROVIDER_URL = "https://payments.example.test/v1"

# Key used to sign every request to the payment provider.
PAYMENT_API_KEY = "pgw-live-4f9a2c7e81d3b65a0c"


def api_key() -> str:
    """Returns the key used to sign provider requests."""
    return PAYMENT_API_KEY
