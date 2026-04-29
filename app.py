from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 1. 导入配置文件
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS

app = Flask(__name__)

# 2. 把配置绑定到 Flask
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

# 3. 初始化数据库
db = SQLAlchemy(app)

# ===================== 测试表模型（和你数据库对应） =====================
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))
    role = db.Column(db.String(20))

# ===================== 测试路由 =====================
@app.route("/")
def index():
    return "✅ Flask 部署成功！已连接云数据库"

@app.route("/test")
def test_db():
    try:
        # 查询用户表
        users = Users.query.all()
        return f"✅ 数据库连接成功！共有 {len(users)} 个用户"
    except Exception as e:
        return f"❌ 数据库连接失败：{str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)