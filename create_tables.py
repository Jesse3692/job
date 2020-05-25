from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer, String, Float


# 创建数据库连接
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/job51?charset=utf8")
# 操作数据库，创建一个session
Session = sessionmaker(bind=engine)
# 声明一个基类
Base = declarative_base()

class Job51(Base):
    # 表名称
    __tablename__ = 'job_data'
    # id 设置为主键和自增
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 岗位名称
    position_name = Column(String(length=50), nullable=False)
    # 公司名称
    company_name = Column(String(length=50), nullable=False)
    # 所在城市
    city = Column(String(length=10), nullable=False)
    # 工作年限要求
    work_year = Column(String(length=20), nullable=False)
    # 学历
    education = Column(String(length=20), nullable=False)
    # 工作地点
    address = Column(String(length=50), nullable=False)
    # 薪资
    salary = Column(String(length=20), nullable=False)
    # 抓取日期
    crawl_date = Column(String(length=20), nullable=False)

if __name__ == "__main__":
    # 创建数据表
    Job51.metadata.create_all(engine)
