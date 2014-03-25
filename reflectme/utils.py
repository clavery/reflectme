
def parse_headers(headers):
    raw_headers = headers.splitlines()
    raw_headers = [h.split(':') for h in raw_headers]
    return {h[0].strip() : h[1].strip() for h in raw_headers}

