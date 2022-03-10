import datetime
import os
import random
import shutil
import time
import uuid
from typing import Generator, Any

from PIL import Image, ImageDraw, ImageFont
from faker import Faker

fakes = Faker('zh_CN')


def now_time(sep='-', date=False):
    """
    返回当前系统时间
    以括号中（2010/01/01 15:21:55）展示
    """
    fmt_ = '%Y{sep_}%m{sep_}%d %H:%M:%S'.format(sep_=sep)
    s = time.strftime(fmt_, time.localtime(time.time()))
    if date:
        s = datetime.datetime.strptime(s, f'%Y{sep}%m{sep}%d %H:%M:%S')

    return s


def microsecond() -> int:
    """微秒"""
    return int(round(time.time() * 1000000))


def now_timestamp() -> int:
    """
    返回当前系统时间

    """
    return int(time.time())


def day_timestamp(week=2) -> int:
    """
    返回指定天/week当前系统时间
    """
    n = datetime.datetime.now() + datetime.timedelta(weeks=week)

    return int(n.timestamp())


def one_second_before(sep='-', hour=-8, sec=-3) -> str:
    """
    一秒前

    :param sep: 日期格式分割符号
    :param hour: 默认8小时前
    :param sec: 默认1秒
    :return:
    """
    n = datetime.datetime.now() + datetime.timedelta(hours=hour, seconds=sec)

    return n.strftime(f'%Y{sep}%m{sep}%d %H:%M:%S')


def now_min(sep='/') -> Generator[str, Any, None]:
    """当前时间 整分钟时间值"""
    n = now_time(sep)
    seconds = 60
    minutes = (n[:-2] + f'{format(s, "02d")}' for s in range(seconds))

    mis = (datetime.datetime.strptime(m, f'%Y{sep}%m{sep}%d %H:%M:%S') for m in minutes)

    return mis


def round_minutes(internal=30, sep='/'):
    """
    当前时间前后 1/2 internal 的 时间
    :param internal: 默认 30分钟
    :param sep: 日期分割符
    :return:
    """
    now_date = datetime.datetime.strptime(now_time(sep), f'%Y{sep}%m{sep}%d %H:%M:%S')
    begin = now_date + datetime.timedelta(minutes=-internal / 2)

    date_slice = (begin + datetime.timedelta(minutes=s + 1) for s in range(internal))

    return date_slice


def round_seconds(internal=30, sep='/'):
    """
    当前时间前后 1/2 internal 的 时间
    :param internal: 默认 30分钟
    :param sep: 日期分割符
    :return:
    """
    now_date = datetime.datetime.strptime(now_time(sep), f'%Y{sep}%m{sep}%d %H:%M:%S')
    begin = now_date + datetime.timedelta(minutes=-internal / 2)

    date_slice = (begin + datetime.timedelta(minutes=s + 1) for s in range(internal))

    return date_slice


def date_today():
    """当前时间(年月日)"""
    date = datetime.date.today()
    return date


def test_nrm():
    for d in round_minutes():
        print(d, type(d))


def phone_number():
    """随机手机号"""
    return fakes.phone_number()


def name():
    """随机姓名"""
    return fakes.name()


def num():
    """生成随机三位数"""
    return fakes.numerify()


def id_card():
    """随机身份证号"""
    return fakes.ssn()


def address():
    """随机地址"""
    return fakes.address()


def email():
    """随机email"""
    return fakes.email()


def date_string():
    """随机日期"""
    return str(fakes.date_time())


def random_text(length=60):
    """随机字符串"""
    return fakes.text(length)


def ipv4():
    """随机IPV4地址"""
    return fakes.ipv4()


def serial_no():
    """随机序列号"""
    return uuid.uuid4().hex


def ones_uuid(prefix=''):
    """ONES-8位UUID"""
    return random_string(prefix=prefix)


def random_string(length=8, prefix: str = ''):
    char = ''.join([chr(i) for i in range(97, 123)])
    seed = '0123456789' + char.upper() + char

    m = random.sample(seed, length)

    return prefix + ''.join(m)


def index_copy_keys(data):
    """
    查找需要替换的key
    :param data:
    :return:
    """
    keys = []

    def index_key(message):
        for k, v in message.items():
            if isinstance(v, str):
                if v.startswith('@copy-'):
                    keys.append((k, v[6:]))
            if isinstance(v, dict):
                index_key(v)
            if isinstance(v, list):
                for m in v:
                    if isinstance(m, dict):
                        index_key(m)
                    else:
                        return

    index_key(data)

    return set(keys)


def index_values(data, keys):
    """
    查找要替换的value
    :param data:
    :param keys:
    :return: 替换后的新数据
    """
    values = []

    def index_value(message, key):
        for k, v in message.items():
            if isinstance(v, str):
                if k == key[1]:
                    # data[key[0]] = v # 替换掉标记为copy的值
                    values.append((key[0], k, v))
            if isinstance(v, dict):
                index_value(v, key)
            if isinstance(v, list):
                for m in v:
                    if isinstance(m, dict):
                        index_value(m, key)
                    else:
                        return

    for k in keys:
        index_value(data, k)

    return values


def _replace_copy(data, values):
    def rep(message, value):
        for k, v in message.items():
            if isinstance(v, str):
                if v == '@copy-' + value[1]:
                    message[k] = value[2]
            if isinstance(v, dict):
                rep(v, value)
            if isinstance(v, list):
                for m in v:
                    if isinstance(m, dict):
                        rep(m, value)
                    else:
                        return

    for val in values:
        rep(data, val)
    return data


def convert_boolean_object(s):
    return s.replace('null', 'None').replace('false', 'False').replace('true', 'True')


def remove_images(path):
    """清空图片"""
    if os.path.exists(path):
        shutil.rmtree(path)


def create_new_image(path, img_name):
    """
    生成图片

    :param path:
    :param img_name:
    :return:
    """
    img = Image.new('RGB', (1980, 1980), (20, 20, 20, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('simkai.ttf', size=92)

    # 输出文字:
    timed = '@Testing at: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    draw.text((360, 600), img_name, font=font, fill=(255, 255, 255, 128))
    draw.text((360, 760), timed, font=font, fill=(255, 255, 255, 128))
    if not os.path.exists(path):
        os.makedirs(path)
    img.save(os.path.join(path, img_name) + '.png', 'png')


if '__main__' == __name__:
    date_today()
