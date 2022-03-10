import random
from collections import UserDict

from pkg.mocks import ones_uuid


def members():
    return [
        {
            'userid': 'xiaobaigou',
            'name': 'xiaobaigou',
            'mobile': '',
            'department': ['21000', ],
            'email': 'xiaocai@ones.ai'
        },
        {
            'userid': 'xiaomin',
            'name': 'xiaomin',
            'mobile': '',
            'department': ['21000', ],
            'email': ''
        },
        {
            'userid': 'huahua',
            'name': '花花',
            'mobile': '',
            'department': ['21001', ],
            'email': 'huahua@ones.ai'
        },
        {
            'userid': 'dahua',
            'name': '大华',
            'mobile': '',
            'department': ['24001', ],
            'email': 'dahua@ones.ai'
        },
        {
            'userid': 'xiaotong',
            'name': '晓彤',
            'mobile': '',
            'department': ['25000', ],
            'email': 'xiaotong@ones.ai'
        },
        {
            'userid': 'wukong',
            'name': '齐天大圣',
            'mobile': '',
            'department': ['22000', ],
            'email': 'wukong@ones.ai'
        },
        {
            'userid': 'zhubajie',
            'name': '猪八戒',
            'mobile': '',
            'department': ['22000', ],
            'email': 'zhubajie@ones.ai'
        },
        {
            'userid': 'shawujing',
            'name': '沙悟净',
            'mobile': '',
            'department': ['22000', ],
            'email': 'shawujing@ones.ai'
        },
        {
            'userid': 'xiaobailong',
            'name': '小白龙',
            'mobile': '',
            'department': ['22000', ],
            'email': ''
        },
        {
            'userid': 'xiezhi',
            'name': '谢智',
            'mobile': '',
            'department': ['24100', ],
            'email': 'xiezhi+4@ones.ai'
        },
        {
            'userid': 'zhiheng',
            'name': '方志恒',
            'mobile': '',
            'department': ['24100', ],
            'email': 'enheng@ones.ai'
        },
        {
            'userid': 'liujing',
            'name': '刘晶',
            'mobile': '',
            'department': ['24100', ],
            'email': 'oho@ones.ai'
        },
        {
            'userid': 'moli',
            'name': '茉莉',
            'mobile': '',
            'department': ['24100', ],
            'email': 'momo@ones.ai'
        },
        {
            'userid': 'dejing',
            'name': '梁德金',
            'mobile': '',
            'department': ['24100', ],
            'email': 'dede@ones.ai'
        },
        {
            'userid': 'zhongli',
            'name': '林中莉',
            'mobile': '',
            'department': ['24100', ],
            'email': 'zhong@ones.ai'
        },
        {
            'userid': 'zhoujiahao',
            'name': '周佳浩',
            'mobile': '',
            'department': ['24100', ],
            'email': 'jiajia@ones.ai'
        },
        {
            'userid': 'liuxing',
            'name': '刘鑫',
            'mobile': '',
            'department': ['24100', ],
            'email': 'niuniu@ones.ai'
        },
        {
            'userid': 'yangdi',
            'name': '杨笛',
            'mobile': '',
            'department': ['24100', ],
            'email': 'didi@ones.ai'
        },
        {
            'userid': 'tangsheng',
            'name': '唐僧',
            'mobile': '',
            'department': ['22000', ],
            'email': 'tangsheng@ones.ai'
        },
        {
            'userid': 'yangyang',
            'name': '杨洋',
            'mobile': '',
            'department': ['22002', ],
            'email': 'yang@ones.ai'
        },
        {
            'userid': 'xifan',
            'name': '稀饭',
            'mobile': '',
            'department': ['25003', ],
            'email': 'xixi@ones.ai'
        },
        {
            'userid': 'yatang',
            'name': '雅堂',
            'mobile': '',
            'department': ['25003', ],
            'email': 'yaya@ones.ai'
        },
        {
            'userid': 'weiye',
            'name': '伟业',
            'mobile': '',
            'department': ['25003', ],
            'email': 'wei@ones.ai'
        },
        {
            'userid': 'huangmei',
            'name': '黄美',
            'mobile': '',
            'department': ['21004', ],
            'email': 'meiyou@ones.ai'
        },
        {
            'userid': 'weixiaobao',
            'name': '韦小宝',
            'mobile': '',
            'department': ['21006', ],
            'email': 'weixiaobao@ones.ai'
        },
        {
            'userid': 'anqila',
            'name': '安琪拉',
            'mobile': '',
            'department': ['21006', ],
            'email': 'anqila@ones.ai'
        },
        {
            'userid': 'caiwenji',
            'name': '蔡文姬',
            'mobile': '',
            'department': ['21006', ],
            'email': 'caiwenji@ones.ai'
        },
        {
            'userid': 'bilibili',
            'name': '对应LDAP的bilibili',
            'mobile': '13342543625',
            'department': ['21006', ],
            'email': 'bilibili@ones.ai'
        }
    ]


def department():
    return [
        {
            'id': '21000',
            'name': '研发组部',
            'parentid': '0',
            'order': 1
        },
        {
            'id': '21001',
            'name': '质量保证部',
            'parentid': '0',
            'order': 2
        },
        {
            'id': '21002',
            'name': '产品部',
            'parentid': '0',
            'order': 3
        },
        {
            'id': '21003',
            'name': '性能优化部',
            'parentid': '0',
            'order': 4
        },
        {
            'id': '21004',
            'name': '财务部',
            'parentid': '0',
            'order': 5
        },
        {
            'id': '21005',
            'name': '人事部',
            'parentid': '0',
            'order': 6
        },
        {
            'id': '21006',
            'name': '后勤部',
            'parentid': '0',
            'order': 7
        },
        {
            'id': '22000',
            'name': '前端',
            'parentid': '21000',
            'order': 1
        },
        {
            'id': '22001',
            'name': '后端',
            'parentid': '21000',
            'order': 2
        },
        {
            'id': '22002',
            'name': 'UI',
            'parentid': '21000',
            'order': 3
        },
        {
            'id': '23000',
            'name': '压力测试',
            'parentid': '21001',
            'order': 1
        },
        {
            'id': '23001',
            'name': '接口测试',
            'parentid': '21001',
            'order': 2
        },
        {
            'id': '23002',
            'name': '功能测试',
            'parentid': '21001',
            'order': 3
        },
        {
            'id': '24000',
            'name': '产品',
            'parentid': '21002',
            'order': 1
        },
        {
            'id': '24001',
            'name': 'PM',
            'parentid': '21002',
            'order': 2
        },
        {
            'id': '24002',
            'name': 'PO',
            'parentid': '21002',
            'order': 3
        },
        {
            'id': '24003',
            'name': '基础组',
            'parentid': '21002',
            'order': 4
        },
        {
            'id': '24100',
            'name': '基础一组',
            'parentid': '24003',
            'order': 1
        },
        {
            'id': '24101',
            'name': '基础二组',
            'parentid': '24003',
            'order': 1
        },
        {
            'id': '24102',
            'name': '基础三组',
            'parentid': '24003',
            'order': 1
        },
        {
            'id': '24103',
            'name': '基础四组',
            'parentid': '24003',
            'order': 1
        },
        {
            'id': '24104',
            'name': '基础五组',
            'parentid': '24003',
            'order': 1
        },
        {
            'id': '25000',
            'name': '优化前端',
            'parentid': '21003',
            'order': 1
        },
        {
            'id': '25001',
            'name': '优化后端',
            'parentid': '21003',
            'order': 2
        },
        {
            'id': '25002',
            'name': '优化测试',
            'parentid': '21003',
            'order': 3
        },
        {
            'id': '25003',
            'name': '优化技术',
            'parentid': '21003',
            'order': 4
        },
        {
            'id': '26000',
            'name': '财务',
            'parentid': '21004',
            'order': 1
        },
        {
            'id': '27000',
            'name': '人事',
            'parentid': '21005',
            'order': 1
        },
        {
            'id': '27001',
            'name': '前台',
            'parentid': '21005',
            'order': 2
        }
    ]


class Member(UserDict):
    """"""

    def __init__(self):
        super(Member, self).__init__()
        self.data = self._new_data()

    @classmethod
    def _new_data(cls):
        return {
            'members': members(),
            'departments': department()
        }

    def add_members(self, data: list, d_type: str = 'members'):
        """
        """

        curr = self.data.get(d_type)
        curr_key = {'members': 'userid', 'departments': 'id'}
        match_key = curr_key.get(d_type)

        exist = [c[match_key] for c in curr]
        tobe_add = [d for d in data if d[match_key] not in exist]

        curr += tobe_add

    def update_members(self, data: list, d_type: str = 'members'):
        """
        """

        curr = self.data.get(d_type)
        curr_key = {'members': 'userid', 'departments': 'id'}
        match_key = curr_key.get(d_type)
        for d in data:
            for m in curr:
                if d[match_key] == m[match_key]:
                    m |= d

    def delete_org(self, uuids: list, d_type: str = 'members'):
        """"""
        curr = self.data.get(d_type)
        print(f'uuids {uuids}')
        curr_key = {'members': 'userid', 'departments': 'id'}
        match_key = curr_key.get(d_type)

        new_data = []

        for m in curr:
            if m[match_key] not in uuids:
                print(m[match_key])
                new_data.append(m)

        self.data[d_type] = new_data

    def reset(self):
        """"""
        self.data = self._new_data()

    @classmethod
    def big_data(cls):
        """"""
        b = {
            'members': [single_member() for _ in range(100000)],
            'departments': [single_depart(d, d + 1) for d in range(5000)]
        }

        return b


def single_member():
    name = f'{ones_uuid().lower()}'
    m = {
        'userid': name,
        'name': name,
        'mobile': '',
        'department': [f'{random.randint(0, 5000)}', ],
        'email': f'{name}@ones.ai'
    }

    return m


def single_depart(index, order):
    d = {
        'id': f'{index}',
        'name': f'{ones_uuid()}',
        'parentid': '0',
        'order': order
    }

    return d
