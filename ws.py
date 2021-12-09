import asyncio
import json
from websockets import connect

entityId = "4c2cc200-58fb-11ec-8f43-1d800e6c37b6"
jwt_token = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJzYW1vbmNoZXYwMDFAZ21haWwuY29tIiwic2NvcGVzIjpbIlRFTkFOVF9BRE1JTiJdLCJ1" \
            "c2VySWQiOiJkYzM5ODdmMC0zMmI1LTExZWMtYmI0NC04ZjQzODIxMGQ4YjciLCJmaXJzdE5hbWUiOiLQktCw0LvQtdC90YLQuNC9Ii" \
            "wibGFzdE5hbWUiOiLQodCw0LzQvtC90YfQtdCyIiwiZW5hYmxlZCI6dHJ1ZSwicHJpdmFjeVBvbGljeUFjY2VwdGVkIjp0cnVlLCJpc" \
            "1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiZDk1ZDQzMDAtMzJiNS0xMWVjLWJiNDQtOGY0MzgyMTBkOGI3IiwiY3VzdG9tZXJJZCI6" \
            "IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCIsImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNjM4OTg1OTM3L" \
            "CJleHAiOjE2NDA3ODU5Mzd9.QKMC_cGU9o7qq19uqDYBnL9nmEDmBVz4BEN8bgZV4-21NrvAePcy9kzEtv5tYPd-13vELthZanx7Uir4yZgP3Q"


async def handler(websocket):
    while True:
        message = await websocket.recv()
        print(message)


async def hello(uri):
    async with connect(uri) as websocket:
        obj = {
            "tsSubCmds": [
                {
                    "entityType": "DEVICE",
                    "entityId": entityId,
                    "scope": "LATEST_TELEMETRY",
                    "cmdId": 10
                }
            ],
            "historyCmds": [],
            "attrSubCmds": []
        }
        await websocket.send(json.dumps(obj))
        await handler(websocket)


asyncio.run(hello(f"wss://demo-thingsboard.io/api/ws/plugins/telemetry?token={jwt_token}"))
