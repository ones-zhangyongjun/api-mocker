## Mock Api


| Api | 名字 | 类型       | 参数                                                                       | 说明                                                                        |
| --- |---|----------|--------------------------------------------------------------------------|---------------------------------------------------------------------------|
|api/sync| get | 同步       | -                                                                        ||
|api/add| post | 添加mock数据 | {"d_type":"members","data": [{"userid":"2323","name":"new_user_name"}]}  | `d_type` : members, departments。members与 `userid` 关联, departments 与`id` 关联 |
|api/update| post | 更新mock数据 | {"d_type":"members","data": [{"userid":"2323","name":"updated_user_name"}]} | 同上                                                                        |
|api/reset| post | 重置为默认数据  | - ||
|api/delete| post | 删除mock数据 | `{"d_type":"members", "uuids":["2323", "2324"]}`| uuids 的值：members-- `userid`, departments --`id`                      |
