from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
# 从 Model/login.py 中导入 User
from Model.login import User
# 

app = FastAPI()

# 定义

@app.get("/login")
def read_root(user: User):
    """检验用户名和密码是否和 ViteLearningBackend.db 的 admin 表中的数据匹配
    匹配则返回 true, 否则返回 false
    """
    """用 user.uid 查询 admin 表中的 uid 字段并检查 user.password 是否和 admin 表中的 password 字段匹配
    若匹配则返回 true, 否则返回 false
    """
    




@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
