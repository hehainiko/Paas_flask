from flask import Flask, jsonify
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

# 阿里云 PolarDB 正确连接
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+pg8000://zhaofulin:Zf120050815!@pc-uf6a2084m0y29c01.polardb.rds.aliyuncs.com:5432/sports_meet_se"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 自动初始化表和数据（启动就自动建好）
with app.app_context():
    try:
        # 创建 users 表
        db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS users (
              id SERIAL PRIMARY KEY,
              username VARCHAR(50) NOT NULL,
              password VARCHAR(100) NOT NULL,
              role VARCHAR(20) NOT NULL DEFAULT '普通用户'
            );
        """))

        # 创建 events 表
        db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS events (
              id SERIAL PRIMARY KEY,
              event_name VARCHAR(100) NOT NULL,
              event_type VARCHAR(20) NOT NULL
            );
        """))

        # 创建 venues 表
        db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS venues (
              id SERIAL PRIMARY KEY,
              venue_code VARCHAR(50) NOT NULL,
              venue_name VARCHAR(100) NOT NULL,
              capacity INT,
              equipment_available VARCHAR(200),
              status VARCHAR(20) DEFAULT '可用'
            );
        """))

        # 插入默认数据
        db.session.execute(text("""
            INSERT INTO users (username, password, role)
            VALUES ('admin','admin123','管理员'),('user','user123','普通用户')
            ON CONFLICT DO NOTHING;
        """))

        db.session.execute(text("""
            INSERT INTO events (event_name, event_type)
            VALUES ('男子100米','径赛'),('男子200米','径赛'),('女子100米','径赛'),('女子跳远','田赛')
            ON CONFLICT DO NOTHING;
        """))

        db.session.execute(text("""
            INSERT INTO venues (venue_code, venue_name, capacity, status)
            VALUES ('FIELD_A','田径场A区',200,'可用'),('JUMP_AREA','跳跃区',50,'可用')
            ON CONFLICT DO NOTHING;
        """))

        db.session.commit()
    except:
        pass

# ===================== 接口 =====================
@app.route("/api/users")
def get_users():
    try:
        with db.engine.connect() as conn:
            res = conn.execute(text("SELECT id, username, password, role FROM users"))
            return jsonify([dict(row) for row in res])
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/api/events")
def get_events():
    try:
        with db.engine.connect() as conn:
            res = conn.execute(text("SELECT id, event_name, event_type FROM events"))
            return jsonify([dict(row) for row in res])
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/api/venues")
def get_venues():
    try:
        with db.engine.connect() as conn:
            res = conn.execute(text("SELECT id, venue_code, venue_name, capacity, status FROM venues"))
            return jsonify([dict(row) for row in res])
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/")
def index():
    return "<h1>✅ 运动会服务运行成功！</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
