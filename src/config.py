"""
simple configuration to get .env variable
"""

import os
from dotenv import load_dotenv


class Config:
    def __init__(self):
        # loading .env file
        load_dotenv()
        
        # getting API key
        self.api_key = os.getenv('NEWS_API_KEY')
        
        # checking key exists
        if not self.api_key:
            raise ValueError("key not found.")
        
        # print("API key loaded.")
    
    def get_api_key(self):
        """returns the API key"""
        return self.api_key


# testing the config
if __name__ == "__main__":
    try:
        config = Config()
        print(f"API key: ...{config.get_api_key()[-4:]}")
    except Exception as e:
        print(f"error: {e}")