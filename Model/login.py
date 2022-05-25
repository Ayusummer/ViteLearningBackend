# 定义 login 页面需要的一些数据结构
# 借助 Pydantic 来使用标准的 Python 类型声明请求体
from plistlib import UID
import string
from pydantic import BaseModel

class User(BaseModel):
    uid: int
    password: str
