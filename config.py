# 阿里云 PolarDB PostgreSQL 配置
DB_HOST = "yunjisuansuan.rwlb.rds.aliyuncs.com"
DB_PORT = 5432
DB_USER = "zhaofulin"
DB_PASSWORD = "Zfl20050815!"
DB_NAME = "sports_meet_se"  # 你刚创建的数据库

# 连接串（自动拼接，不用改）
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
