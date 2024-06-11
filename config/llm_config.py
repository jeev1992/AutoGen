from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_openai_base_url = os.getenv("AZURE_OPENAI_BASE_URL")
azure_openai_llm_model_deployment_name = os.getenv("AZURE_OPENAI_LLM_MODEL_DEPLOYMENT_NAME")
azure_openai_llm_model_version = os.getenv("AZURE_OPENAI_LLM_MODEL_VERSION")

#LLM config list
config_list = [
  {
    "model": azure_openai_llm_model_deployment_name,
    "api_type": "azure",
    "api_key": azure_openai_api_key,
    "base_url": azure_openai_base_url,
    "api_version": azure_openai_llm_model_version
  }
]

llm_config = {
  "config_list": config_list,
  "seed": 42, # If the seed value is changed cached results wouldn't be used
  "temperature": 0 # 0 means no randomness, good for tasks where we don't want LLMs to be creative, example coding tasks
}