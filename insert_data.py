from collections import Counter
from sqlalchemy import func
from create_tables import Job51
from create_tables import Session
import time

class HandleJob51Data:
    def __init__(self):
        # 实例化session信息
        self.session = Session()
        # 当前时间
        self.date = time.strftime("%Y-%m-%d", time.localtime())


    # 数据的存储方法
    def insert_item(self, item):
        # 当前时间
        date = self.date
        """
        CREATE TABLE `job_data` ( 
            `id` int(11) NOT NULL AUTO_INCREMENT, 
            `position_name` varchar(50) NOT NULL, 
            `company_name` varchar(50) NOT NULL, 
            `city` varchar(10) NOT NULL, 
            `work_year` varchar(20) NOT NULL, 
            `education` varchar(20) NOT NULL, 
            `address` varchar(50) NOT NULL, 
            `salary` varchar(20) NOT NULL, 
            `crawl_date` varchar(20) NOT NULL, PRIMARY KEY (`id`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8	
        :return:
        """
        # 存储的数据结构
        data = Job51(
            # 岗位名称
            position_name = item['position_name'],
            # 公司名称
            company_name = item['company_name'],
            # 所在城市
            city = item['city'],
            # 工作年限
            work_year = item['work_year'],
            # 学历
            education = item['education'],
            # 工作地址
            address = item['address'],
            # 薪资
            salary = item['salary'],
            # 抓取日期
            crawl_date = date
        )

        # 去除重复数据
        query_result = self.session.query(Job51).filter(
            Job51.crawl_date == date,
            Job51.position_name == item['position_name']
        ).first()

        if query_result:
            pass
        else:
            # 插入数据
            self.session.add(data)
            # 提交数据到数据库
            self.session.commit()

if __name__ == "__main__":
    # 测试数据
    item = {
        "position_name": "数据分析师",
        "company_name": "佰聆数据股份有限公司",
        "city":"西安",
        "work_year":"3-5年",
        "education":"本科",
        "address": "西安市长安区航天中路669号(国网陕西省电力公司电力科学研究院)",
        "salary":"10K-20K",
        "crawl_date":"2019-11-21"
    }
    HandleJob51Data().insert_item(item)
