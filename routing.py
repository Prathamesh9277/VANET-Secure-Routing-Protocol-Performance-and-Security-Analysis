# routing.py

def create_rreq(source_id, dest_id, req_id, path):
    return {
        'type': 'RREQ',
        'source': str(source_id),
        'dest': str(dest_id),
        'id': str(req_id),
        'path': path
    }

def create_rrep(dest_id, source_id, req_id, path):
    return {
        'type': 'RREP',
        'source': str(dest_id),
        'dest': str(source_id),
        'id': str(req_id),
        'path': path
    }
