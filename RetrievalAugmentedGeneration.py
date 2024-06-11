from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from chromadb.utils import embedding_functions
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config.llm_config import llm_config

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_openai_base_url = os.getenv("AZURE_OPENAI_BASE_URL")
azure_openai_embedding_model_deployment_name = os.getenv("AZURE_OPENAI_EMBEDDING_MODEL_DEPLOYMENT_NAME")
azure_openai_embedding_model_version = os.getenv("AZURE_OPENAI_EMBEDDING_MODEL_VERSION")

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_base=azure_openai_base_url,
                api_key=azure_openai_api_key,
                api_type="azure",
                api_version=azure_openai_embedding_model_version,
                deployment_id=azure_openai_embedding_model_deployment_name,
                model_name="text-embedding-ada-002"
            )

recur_spliter = RecursiveCharacterTextSplitter(separators=["\n", "\r", "\t"])

# Assistant agent receives message from RetrieveUserProxyAgent which includes the question and the associated context
# Assistant agent then processes the question and context to generate the answer
assistant = RetrieveAssistantAgent(
    name="assistant",
    system_message="You are a helpful assistant.",
    code_execution_config=False,
    llm_config=llm_config,
)

# RetrieveUserProxyAgent computes the embeddings of the document specified and stores in the vector database(ChromaDB)
# It computes the context by doing a search in the vector database to retrieve the most similar embeddings to the question
ragproxyagent = RetrieveUserProxyAgent(
    code_execution_config=False,
    name="ragproxyagent",
    retrieve_config={
        "task": "qa",
        "docs_path": os.getcwd() + "/docs/test.md",
        "embedding_function": openai_ef,
        "custom_text_split_function": recur_spliter.split_text,
    },
)

assistant.reset()

# Initiate chat with the assistant agent
ragproxyagent.initiate_chat(assistant, 
                            message=ragproxyagent.message_generator, 
                            problem="What is the fastest growing service by ACR in SAP SE and what is it's last 12 month ACR?"
                            )
