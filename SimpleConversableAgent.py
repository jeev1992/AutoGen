from config.llm_config import llm_config
from autogen import ConversableAgent

agent = ConversableAgent(
    "chatbot",
    llm_config=llm_config,
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
)

reply = agent.generate_reply(messages=[{"content": "Tell me a joke.", "role": "user"}])
print(reply)