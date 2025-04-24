import redis
import json
from datetime import datetime

# Connect to Redis running on localhost
r = redis.Redis(host='localhost', port=6379, db=0)


def store_conversation(user_id, summary, raw):
    """
    Stores a conversation turn in Redis for the given user.
    Keeps only the latest 10 turns.
    """
    conversation = {
        "summary": summary,
        "raw": raw,
        "timestamp": datetime.utcnow().isoformat()
    }

    key = f"recent:{user_id}"
    json_data = json.dumps(conversation)

    r.lpush(key, json_data)     # Push new item to the front
    r.ltrim(key, 0, 9)          # Keep only the 10 most recent items


def get_recent_conversations(user_id, limit=5):
    """
    Returns the most recent N conversations for the given user.
    """
    key = f"recent:{user_id}"
    messages = r.lrange(key, 0, limit - 1)

    results = []
    for msg in messages:
        parsed = json.loads(msg)
        results.append(parsed)

    return results
