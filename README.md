# payment-gateway-python

A small payment gateway: merchant accounts, orders stored in SQLite, and signed requests to a payment provider.

**Demo target for ProofPatch: intentionally contains security bugs. Never deploy this code.**

| Area | Vulnerability | OWASP |
|---|---|---|
| `gateway/config.py` | Hardcoded payment API key (CWE-798) | A07 Identification and Authentication Failures |
| `gateway/orders.py` | SQL injection in order search (CWE-89) | A03 Injection |
| `gateway/accounts.py` | Passwords hashed with MD5 (CWE-328) | A02 Cryptographic Failures |

Run the tests: `python -m pytest` (standard library only).
