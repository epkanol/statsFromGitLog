
import re

def process(lines):
    commitid = None
    author = None
    date = None
    id = None
    committype = ""

    result = []
    for line in lines:
        parts = line.split()
        if parts is None or len(parts) == 0:
            continue
        head = parts[0]
        if head == "commit":
            if commitid:
                result.append([commitid, author, date, id, committype])
                commitid = None
                author = None
                date = None
                id = None
                committype = ""
            commitid = parts[1]
        if head == "Author:":
            author = parts[1]
        if head == "Date:":
            date = parts[1]
        if re.match("#[0-9]+", head):
            id = head
        if re.search("/src/main/java/", head):
            committype = "code"
        if re.search("/tests/", head) and re.search("tc_", head, re.IGNORECASE):
            committype = "integration test"
    if id:
        result.append([commitid, author, date, id, committype])
    return result
