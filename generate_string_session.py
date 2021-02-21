from pyrogram import Client

API_KEY = int(input("Enter API KEY: 2719286"))
API_HASH = input("Enter API HASH: f87299ffb97c021891d44dd0063882da")
with Client(':memory:', api_id=API_KEY, api_hash=API_HASH) as app:
    print(app.export_session_string())
