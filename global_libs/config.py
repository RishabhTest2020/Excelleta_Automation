import logging
import os
from dotenv import load_dotenv


class global_env_vars:
    def __init__(self):
        self.get_env()
        self.env_vars()

    def get_env(self, env='bony'):
        try:
            env = os.environ['ENV']
        except KeyError:
            env = env
        except Exception as e:
            print(e)
        env_file_path = os.getcwd() + '/envFiles/' + env + '.env'
        load_dotenv(env_file_path)

    def env_vars(self):
        self.main_url = os.getenv('main_url')
        self.user_email = os.getenv('user_email')
        self.user_password = os.getenv('user_password')
        self.env = os.getenv('env')
        self.api_url = os.getenv('api_url')
        self.Siddharth_email = os.getenv('Siddharth_email')
        self.Ashish_email = os.getenv('Ashish_email')
        self.Prakash_email = os.getenv('Prakash_email')
        self.Somvir_email = os.getenv('Somvir_email')
        self.Nishant_email = os.getenv('Nishant_email')
        self.approver_password = os.getenv('approver_password')


globalEnvs = global_env_vars()
