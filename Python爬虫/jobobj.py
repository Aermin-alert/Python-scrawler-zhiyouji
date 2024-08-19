class Job:
    def __init__(self):
        # 定义Job类中的成员属性
        # 岗位名
        self.jobname = ''
        # 经验
        self.exp = ''
        # 学历
        self.degree = ''
        # 薪资
        self.salary = 10000
        # 公司名
        self.company = ''
        # 访问浏览量，即点击量
        self.hit = 1000
        # 城市
        self.city = '北京'
        # 更新时间
        self.publishtime = ''
        # 数据获取时间，即采集时间
        self.collecttime = ''

    def to_json(self):
        return self.__dict__