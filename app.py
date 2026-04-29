from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import traceback

app = Flask(__name__)
app.config['DEBUG'] = True

# 数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+pg8000://zhaofulin:Zf120050815!@yunjisuansuan.rwlb.rds.aliyuncs.com:5432/sports_meet_se"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ==============================================
# 最简单、最稳定、不报错的查询方式（原生SQL）
# ==============================================

# 用户接口
@app.route("/api/users")
def get_users():
    try:
        with db.engine.connect() as conn:
            res = conn.execute(text("SELECT id, username, password, role FROM users"))
            users = [dict(row) for row in res]
        return jsonify(users)
    except:
        return jsonify([])

# 项目接口
@app.route("/api/events")
def get_events():
    try:
        with db.engine.connect() as conn:
            res = conn.execute(text("SELECT id, event_name, event_type FROM events"))
            events = [dict(row) for row in res]
        return jsonify(events)
    except:
        return jsonify([])

# 场地接口
@app.route("/api/venues")
def get_venues():
    try:
        with db.engine.connect() as conn:
            res = conn.execute(text("SELECT id, venue_code, venue_name, capacity, equipment_available, status FROM venues"))
            venues = [dict(row) for row in res]
        return jsonify(venues)
    except:
        return jsonify([])

# 首页
@app.route("/")
def index():
    return "<h1>✅ 运动会服务运行成功！</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
