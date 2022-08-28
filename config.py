from environs import Env

env = Env()
env.read_env()

token = env.str("token")
path_user_db = env.str("path_user_db")
