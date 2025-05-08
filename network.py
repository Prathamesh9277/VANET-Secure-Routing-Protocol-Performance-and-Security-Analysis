# network.py

import copy

class Network:
    def __init__(self, vehicles, crypto_manager, attacker_enabled=False):
        self.vehicles = vehicles
        self.crypto = crypto_manager
        self.attacker_enabled = attacker_enabled
        self.metrics = {
            'total': 0,
            'valid': 0,
            'invalid': 0,
            'failures': {}
        }

    def broadcast_rreq(self, src, dest_id, req_id):
        msg = {
            'type': 'RREQ',
            'source': src.id,
            'dest': str(dest_id),
            'id': str(req_id),
            'path': [src.id]
        }

        self.crypto.add_hash(msg)
        self.crypto.sign_message(msg, src.id)

        deliveries = []
        for recv in self.vehicles:
            if recv.id != src.id:
                new_msg = copy.deepcopy(msg)

                # Simulate tampering
                if self.attacker_enabled and recv.id == "2":
                    new_msg['path'].append("Evil")  # Modify content

                deliveries.append((recv, new_msg))

        return deliveries

    def unicast_rrep(self, dst, src_id, req_id, path):
        msg = {
            'type': 'RREP',
            'source': dst.id,
            'dest': str(src_id),
            'id': str(req_id),
            'path': path
        }

        self.crypto.add_hash(msg)
        self.crypto.sign_message(msg, dst.id)

        return [(self.get_vehicle_by_id(src_id), msg)]

    def get_vehicle_by_id(self, vid):
        for v in self.vehicles:
            if v.id == str(vid):
                return v
        return None

    def verify_and_record(self, msg, sender_id):
        self.metrics['total'] += 1
        ok, reason = self.crypto.verify_message(msg, sender_id)
        if ok:
            self.metrics['valid'] += 1
        else:
            self.metrics['invalid'] += 1
            self.metrics['failures'][reason] = self.metrics['failures'].get(reason, 0) + 1
        return ok

    def report_metrics(self):
        print("Total messages processed:", self.metrics['total'])
        print("  Valid:  ", self.metrics['valid'])
        print("  Invalid:", self.metrics['invalid'])
        for reason, count in self.metrics['failures'].items():
            print(f"    {reason} failures: {count}")
