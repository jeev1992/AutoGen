from autogen import ConversableAgent
from config.llm_config import llm_config
from autogen import GroupChat
from autogen import GroupChatManager

# The Developer Agent gives an estimate of the time it will take to develop a feature.
developer_agent = ConversableAgent(
    name="Developer_Agent",
    system_message="You are a software developer who needs to provide the technical feasibility for a feature.",
    llm_config=llm_config,
    human_input_mode="NEVER",
    description="Return the technical feasibility for a feature."
)

# The Tester Agent gives an estimate of the time it will take to test a feature.
tester_agent = ConversableAgent(
    name="Tester_Agent",
    system_message="You are a software tester who needs to proivde an estimate of the time it will take to test a feature.",
    llm_config=llm_config,
    human_input_mode="NEVER",
    description="Return the number of hours it will take to test a feature."
)

# The ProductManager Agent gives an estimate of the time it will take to plan a feature.
productManager_agent = ConversableAgent(
    name="ProductManager_Agent",
    system_message="You are a product manager who needs to provide an estimate of the time it will take to plan a feature.",
    llm_config=llm_config,
    human_input_mode="NEVER",
    description="Return the number of hours it will take to plan a feature."
)

engineerinManager_agent = ConversableAgent(
    name="EngineerinManager_Agent",
    system_message="You are an engineering manager who needs to give an estimate of the time it will take to deliver a feature.",
    llm_config=llm_config,
    human_input_mode="NEVER",
    description="Return the number of hours it will take to deliver a feature."
)

group_chat = GroupChat(
    agents=[developer_agent, tester_agent, productManager_agent, engineerinManager_agent],
    messages=[],
    max_round=3,
    speaker_selection_method="round_robin",
)

#Create a group manager.
group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config,
)

chat_result = engineerinManager_agent.initiate_chat(
    group_chat_manager,
    message="I want to develop a Parking Management System.",
    summary_method="reflection_with_llm",
)