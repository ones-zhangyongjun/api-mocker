from fastapi import FastAPI

from pkg.data import Member
from pkg.schema import ModifyItem, response

app = FastAPI()

org = Member()


@app.get("/api/sync")
async def members():
    """获取同步信息"""
    return org.data


@app.post('/api/add')
async def add_org(item: ModifyItem):
    """添加组织信息"""
    org.add_members(item.data, item.d_type)
    return response()


@app.post('/api/update')
async def update_org(item: ModifyItem):
    """更新组织信息"""
    org.update_members(item.data, item.d_type)
    return response()


@app.post('/api/update')
async def update_org(item: ModifyItem):
    """删除组织信息"""
    org.delete_org(item.data, item.d_type)
    return response()


@app.post('/api/reset')
async def reset_api():
    """重置组织信息"""
    org.reset()
    return response()
