# crypto_utils.py

import hashlib
import json
from cryptography.hazmat.primitives.asymmetric import ed25519

class CryptoManager:
    def __init__(self):
        self.private_keys = {}
        self.public_keys = {}

    def init_keys(self, ids):
        for vid in ids:
            priv = ed25519.Ed25519PrivateKey.generate()
            pub = priv.public_key()
            self.private_keys[str(vid)] = priv
            self.public_keys[str(vid)] = pub

    def add_hash(self, msg):
        core = {k: msg[k] for k in msg if k not in ('hash', 'signature')}
        msg['hash'] = hashlib.sha256(json.dumps(core, sort_keys=True).encode()).hexdigest()

    def sign_message(self, msg, sender_id):
        priv = self.private_keys[str(sender_id)]
        core = {k: msg[k] for k in msg if k != 'signature'}
        payload = json.dumps(core, sort_keys=True).encode()
        sig = priv.sign(payload)
        msg['signature'] = sig.hex()

    def verify_message(self, msg, sender_id):
        sid = str(sender_id)
        core = {k: msg[k] for k in msg if k not in ('hash', 'signature')}
        calc_hash = hashlib.sha256(json.dumps(core, sort_keys=True).encode()).hexdigest()

        if calc_hash != msg.get('hash'):
            return False, 'hash'

        pub = self.public_keys.get(sid)
        if not pub:
            return False, 'no_pubkey'

        sig = bytes.fromhex(msg.get('signature', ''))
        try:
            pub.verify(sig, json.dumps(core, sort_keys=True).encode())
            return True, None
        except Exception:
            return False, 'sig'
