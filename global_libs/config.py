import os
from dotenv import load_dotenv


class global_env_vars:
    def __init__(self):
        # self.var2=None
        # self.var1= None
        self.get_env()
        self.env_vars()

    def get_env(self, env='stage'):
        try:
            env = os.environ['ENV']
        except KeyError:
            env = env
        except Exception as e:
            print(e)
        env_file_path = os.getcwd() + '/envFiles/' + env + '.env'
        # import pdb; p+db.set_trace()
        load_dotenv(env_file_path)

    def env_vars(self):
        self.main_url = os.getenv('main_url')
        self.user_email = os.getenv('user_email')
        self.user_password = os.getenv('user_password')
        self.env = os.getenv('env')


globalEnvs = global_env_vars()
