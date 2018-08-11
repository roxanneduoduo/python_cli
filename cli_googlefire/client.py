import fire
import redis


if __name__ == '__main__':
    fire.Fire(redis.StrictRedis)

"""
>  python client.py flushdb
True
>  python client.py set codehole superhero
True
>  python client.py get codehole
superhero
>  python client.py exists codehole
True
>  python client.py keys "*"
codehole
>  python client.py delete codehole
1
# 指定地址
> python client.py set codehole superhero --host=127.0.0.1 --port=6379
True

"""
