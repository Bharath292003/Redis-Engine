from memory.redis_memory import store_conversation, get_recent_conversations, r
from llm.openai_client import generate_summary, generate_response
from utils.prompt_builder import build_prompt

# r.delete("recent:user123")

user_id = "user123"
print("🧠 Welcome to your AI assistant! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in {"exit", "quit"}:
        print("👋 Ending chat. See you next time!")
        break

    # Step 1: Build the memory-aware prompt
    full_prompt = build_prompt(user_id, user_input)

    # Step 2: Get LLaMA's response
    llm_reply = generate_response(full_prompt)

    # Step 3: Generate summary of this user-AI turn
    summary = generate_summary(user_input, llm_reply)

    # Step 4: Store conversation turn in Redis
    raw_data = {
        "user_prompt": user_input,
        "llm_response": llm_reply
    }
    store_conversation(user_id, summary, raw_data)

    # Step 5: Show the reply
    print(f"\n🤖 AI: {llm_reply}\n")
