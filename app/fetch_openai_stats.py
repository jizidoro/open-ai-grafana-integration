import openai
from app.utils import load_config

def fetch_stats():
    config = load_config()

    # Add debug print statement
    print("Config for OpenAI:", config['openai'])

    openai.api_key = config['openai']['api_key']

    # Example: Get usage stats
    usage_stats = openai.Usage.list()
    return usage_stats