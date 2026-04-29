from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import traceback

app = Flask(__name__)
# 开启调试模式，能看到具体错误
app.config['DEBUG'] = True

# 数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+pg8000://zhaofulin:Zf120050815!@yunjisuansuan.rwlb.rds.aliyuncs.com:5432/sports_meet_se"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ==============================================
# 【数据库模型】适配你的表
# ==============================================
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), default='普通用户')

class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), unique=True)
    event_type = db.Column(db.String(20))

class Venues(db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    venue_code = db.Column(db.String(50), unique=True)
    venue_name = db.Column(db.String(100))
    capacity = db.Column(db.Integer)
    equipment_available = db.Column(db.String(200))
    status = db.Column(db.String(20))

# ==============================================
# 【带错误处理的接口】
# ==============================================
@app.route("/api/users")
def get_users():
    try:
        data = Users.query.all()
        result = []
        for item in data:
            result.append({
                "id": item.id,
                "username": item.username,
                "password": item.password,
                "role": item.role
            })
        return jsonify(result)
    except Exception as e:
        # 打印错误详情
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500

@app.route("/api/events")
def get_events():
    try:
        data = Events.query.all()
        result = []
        for item in data:
            result.append({
                "id": item.id,
                "event_name": item.event_name,
                "event_type": item.event_type
            })
        return jsonify(result)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500

@app.route("/api/venues")
def get_venues():
    try:
        data = Venues.query.all()
        result = []
        for item in data:
            result.append({
                "id": item.id,
                "venue_code": item.venue_code,
                "venue_name": item.venue_name,
                "capacity": item.capacity,
                # 处理 NULL 值，避免报错
                "equipment_available": item.equipment_available if item.equipment_available else "",
                "status": item.status
            })
        return jsonify(result)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500

# 首页
@app.route("/")
def index():
    return "<h1>✅ 运动会后端服务运行成功！</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
