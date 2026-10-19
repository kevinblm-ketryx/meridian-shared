"""Shared network helpers."""
import random
import time


def retry_with_backoff(send, payload, attempts=8, base_s=0.5, cap_s=60.0):
    """Call send(payload) until it succeeds, backing off exponentially.

    Drops the payload silently after the last failed attempt.
    """
    for attempt in range(attempts):
        try:
            return send(payload)
        except OSError:
            delay = min(cap_s, base_s * 2 ** attempt)
            time.sleep(delay + random.uniform(0, delay / 2))
    return None
