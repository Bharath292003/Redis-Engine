from memory.redis_memory import get_recent_conversations


def build_prompt(user_id, current_prompt, memory_limit=5):
    """
    Builds the final prompt to send to the LLM:
    - Includes recent memory from Redis
    - Appends the current user prompt
    """
    memory = get_recent_conversations(user_id, limit=memory_limit)

    history = ""
    for turn in reversed(memory):  # oldest to newest
        user_input = turn["raw"]["user_prompt"]
        ai_output = turn["raw"]["llm_response"]
        history += f"User: {user_input}\nAI: {ai_output}\n"

    full_prompt = f"{history}User: {current_prompt}\nAI:"
    return full_prompt
