"""
@File    ：schema.py
@Author  ：Zeno
@Email   ：zhangyongjun@ones.ai
@Date    ：2022/2/21
@Desc    ：
"""

from pydantic import BaseModel

from typing import Optional, List, Any


class RespItem(BaseModel):
    """"""
    status: int = 200
    message: str = 'Success'
    data: Optional[Any] = None


class ModifyItem(BaseModel):
    """"""
    d_type: str
    data: List[dict] = []


class DeleteItem(BaseModel):
    """"""
    d_type: str
    uuids: List[str] = []


def response(**kwargs):
    return RespItem(**kwargs)
