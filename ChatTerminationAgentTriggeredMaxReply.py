from config.llm_config import llm_config
from autogen import ConversableAgent

cathy = ConversableAgent(
    "cathy",
    system_message="Your name is Cathy and you are a part of a duo of comedians.",
    llm_config={**llm_config, "temperature": 0.9},
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "joe",
    system_message="Your name is Joe and you are a part of a duo of comedians.",
    llm_config={**llm_config, "temperature": 0.7},
    human_input_mode="NEVER",  # Never ask for human input.
    max_consecutive_auto_reply=1,  # Limit the number of consecutive auto-replies.
)

result = joe.initiate_chat(cathy, message="Cathy, tell me a joke.")