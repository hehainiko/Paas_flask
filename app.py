from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 数据库连接（直接用你的）
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+pg8000://zhaofulin:Zf120050815!@yunjisuansuan.rwlb.rds.aliyuncs.com:5432/sports_meet_se"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ==============================================
# 【数据库模型】全部根据你的表自动生成
# ==============================================
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), default='普通用户')

class Teams(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(100), nullable=False)
    team_name = db.Column(db.String(100), nullable=False)
    registration_number = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.TIMESTAMP)

class TeamMembers(db.Model):
    __tablename__ = 'team_members'
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer)
    member_name = db.Column(db.String(50))
    role = db.Column(db.String(10))
    phone = db.Column(db.String(20))
    student_id = db.Column(db.String(20))
    created_at = db.Column(db.TIMESTAMP)

class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), unique=True)
    event_type = db.Column(db.String(20))
    created_at = db.Column(db.TIMESTAMP)

class Registrations(db.Model):
    __tablename__ = 'registrations'
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer)
    event_id = db.Column(db.Integer)
    registration_time = db.Column(db.TIMESTAMP)
    status = db.Column(db.String(20))
    check_in_time = db.Column(db.TIMESTAMP)
    created_at = db.Column(db.TIMESTAMP)

class Scores(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    registration_id = db.Column(db.Integer)
    score_value = db.Column(db.Numeric(10,3))
    score_unit = db.Column(db.String(20))
    recorded_by = db.Column(db.String(50))
    stage = db.Column(db.String(20))
    ranking = db.Column(db.Integer)
    points = db.Column(db.Integer)
    created_at = db.Column(db.TIMESTAMP)

class Venues(db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    venue_code = db.Column(db.String(50), unique=True)
    venue_name = db.Column(db.String(100))
    capacity = db.Column(db.Integer)
    equipment_available = db.Column(db.String(200))
    status = db.Column(db.String(20))
    created_at = db.Column(db.TIMESTAMP)

# ==============================================
# 【你要的 JSON 接口】和截图一模一样！
# ==============================================

# 1. 查询所有用户
@app.route("/api/users")
def get_users():
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

# 2. 查询所有场地
@app.route("/api/venues")
def get_venues():
    data = Venues.query.all()
    result = []
    for item in data:
        result.append({
            "id": item.id,
            "venue_code": item.venue_code,
            "venue_name": item.venue_name,
            "capacity": item.capacity,
            "equipment_available": item.equipment_available,
            "status": item.status
        })
    return jsonify(result)

# 3. 查询所有项目
@app.route("/api/events")
def get_events():
    data = Events.query.all()
    result = []
    for item in data:
        result.append({
            "id": item.id,
            "event_name": item.event_name,
            "event_type": item.event_type
        })
    return jsonify(result)

# 首页
@app.route("/")
def index():
    return "<h1>✅ 运动会后端服务运行成功！</h1>"

# 启动
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
