from fastapi import FastAPI

from pkg.data import Member
from pkg.schema import ModifyItem, response, DeleteItem

app = FastAPI()

org = Member()


@app.get("/api/sync")
async def members():
    """获取同步信息"""
    return org.data


@app.get("/api/sync/big")
async def big_data():
    """获取同步信息"""
    return org.big_data()


@app.get("/api/sync/member/{member_no}/depart/{depart_no}")
async def stable_big(member_no: int = 1000, depart_no: int = 100):
    """获取同步信息"""
    if depart_no < 50 or depart_no > 5000:
        return response(status=400, message='False', data='部门数量值 （50， 5000]！')
    if member_no < 1 or member_no > 100000:
        return response(status=400, message='False', data='成员数量值 （1， 100000]！')
    return org.stale_big_data(member_no, depart_no)


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


@app.post('/api/delete')
async def update_org(item: DeleteItem):
    """删除组织信息"""
    org.delete_org(item.uuids, item.d_type)
    return response()


@app.post('/api/reset')
async def reset_api():
    """重置组织信息"""
    org.reset()
    return response()
