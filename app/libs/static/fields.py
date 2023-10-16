RESPONSE_MAP = {"status": {200: "HTTP/1.1 200 OK", 404: "HTTP/1.1 404 Not Found",201: "HTTP/1.1 201 Created"}}

HTTP_HEADER_MAP = {"req_line": 0, "Host": 1, "User-Agent": 2, "body":-1}

EOF = "\r\n\r\n"
DELIM = "\r\n"
