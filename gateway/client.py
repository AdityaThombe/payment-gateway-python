"""Signed requests to the payment provider (built, not sent)."""
import hashlib
import hmac
import json

from . import config


def signed_charge(order_id: int, amount_cents: int, currency: str = "EUR") -> dict:
    """Builds a charge request with an HMAC signature over its body."""
    body = json.dumps({"order": order_id, "amount": amount_cents, "currency": currency}, sort_keys=True)
    signature = hmac.new(config.api_key().encode(), body.encode(), hashlib.sha256).hexdigest()
    return {"url": f"{config.PROVIDER_URL}/charges", "body": body, "signature": signature}
