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
        self.user_name = os.getenv('user_name')
        self.user_password = os.getenv('user_password')
        self.env = os.getenv('env')
        self.api_url = os.getenv('api_url')
        self.Siddharth_email = os.getenv('Siddharth_email')
        self.Ashish_email = os.getenv('Ashish_email')
        self.Prakash_email = os.getenv('Prakash_email')
        self.Somvir_email = os.getenv('Somvir_email')
        self.Nishant_email = os.getenv('Nishant_email')
        self.H_K_email = os.getenv('H_K_email')
        self.Hitesh_email = os.getenv('Hitesh_email')
        self.Ghanshyam_email = os.getenv('Ghanshyam_email')
        self.Arun_email = os.getenv('Arun_email')
        self.Kartikay_email = os.getenv('Kartikay_email')
        self.YashKant_email = os.getenv('YashKant_email')
        self.Uttam_email = os.getenv('Uttam_email')
        self.Sunil_email = os.getenv('Sunil_email')
        self.Anil_email = os.getenv('Anil_email')
        self.Sanjay_email = os.getenv('Sanjay_email')
        self.Pradeep_email = os.getenv('Pradeep_email')
        self.Ashok_email = os.getenv('Ashok_email')
        self.Prashant_email = os.getenv('Prashant_email')
        self.Rajender_email = os.getenv('Rajender_email')
        self.Mahesh_email = os.getenv('Mahesh_email')
        self.approver_password = os.getenv('approver_password')


globalEnvs = global_env_vars()
