"""
Checking mechanism for preventing duplicate conversions

hash original .mts file and track 
- filepath (directory + file name + file extension)
- resulting file's hash

Before converting a file:
1. Check the hash of current mts file from the database
2. If it exists, check filepath
    2a. If saving directory matches a filepath in database
    2b. Check if filepath exists
        - if it does: compare hash with resulting file's hash in db
            - if equal: SKIP CONVERSION (TODO: additional flag for skipping or not skipping conversion)
            - else: go to 3 (resolve naming, MAYBE overwrite)
        - else: go to 3
3. convert file and save directory, filename, and extension
"""

import sqlite3
import hashlib

conn = sqlite3.connect(":memory:")

with conn:
    conn.execute(
        """\
        CREATE TABLE IF NOT EXISTS cache (
            id INTEGER PRIMARY KEY,
            mts_hash BLOB NOT NULL UNIQUE
        );
    """
    )

    conn.executemany(
        "INSERT INTO cache(mts_hash) VALUES (?)",
        [
            [hashlib.md5("asd".encode()).digest()],
            [hashlib.md5("as".encode()).digest()],
            [hashlib.md5("a".encode()).digest()],
        ],
    )

    res = conn.execute("SELECT * FROM cache")
    for i in res.fetchall():
        print(i)
