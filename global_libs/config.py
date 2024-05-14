import os
from dotenv import load_dotenv


global global_env_vars

def set_global_variable(name, value):
    globals()[name] = value


def get_env(env='stage'):
    try:
        env = os.environ['ENV']
    except KeyError:
        env = env
    env_file_path = os.getcwd() + '/envFiles/' + env + '.env'
    load_dotenv(env_file_path)


def global_env_variables():
    get_env()
    var1 = os.getenv('main_url')
    vars_dict = {'main_url': var1}
    return vars_dict
    
global_env_vars = global_env_variables()