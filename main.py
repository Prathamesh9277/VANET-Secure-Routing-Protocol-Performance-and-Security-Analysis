# main.py

from vehicle import Vehicle
from crypto_utils import CryptoManager
from network import Network

def main():
    vehicles = [Vehicle(i) for i in range(5)]
    crypto = CryptoManager()
    crypto.init_keys([v.id for v in vehicles])

    network = Network(vehicles, crypto, attacker_enabled=True)

    src = vehicles[0]
    dst = vehicles[1]
    req_id = 1

    deliveries = network.broadcast_rreq(src, dst.id, req_id)
    for recv, msg in deliveries:
        ok = network.verify_and_record(msg, src.id)
        if ok and recv.id == dst.id:
            path = msg['path'] + [dst.id]
            rreps = network.unicast_rrep(dst, src.id, req_id, path)
            for recv2, msg2 in rreps:
                network.verify_and_record(msg2, dst.id)

    network.report_metrics()

if __name__ == "__main__":
    main()
