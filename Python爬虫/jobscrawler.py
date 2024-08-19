# 需要的包自己导入
class JobCrawler:
# 初版完成对网页信息的基本解析为后期数据插入数据库做准备（后续可继续优化）
    def parser_bs(self, url, city):
        # # 【2】获取URL文本内容
        data = webrequests.get_data(url)
        soup = BeautifulSoup(data, 'html.parser')
        job_lists = soup.find_all('div', attrs={'class': 'c-job-list'})
        for item in job_lists:
            job = jobobj.Job()
            try:
                # 工作
                job.jobname = item.find('h3').text
                # TODO 补充解析的各种信息添加到job对象中



                # 城市
                job.city = city
                # 采集时间
                job.collecttime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # 测试下解析出的结果，后续可以删除此句
                print(job.to_json())
            except Exception as e:
                print(e)

        return data


# 加载配置文件
    def __load_conf(self):
        citys = []
        jobs = []
        return citys, jobs

 # 通过城市、岗位、页数定位网页 入口方法
    def start(self):

        citys, jobs = self.__load_conf()

        for city in citys:
            for job in jobs:
                for  index in range(1,3):
                    url = f'https://www.jobui.com/jobs?jobKw={job}&cityKw={city}&n={index}'
                    print(f"开始爬取{city}岗位为{job}的第{index}页数据")
                    print(url)
                    result = self.parser_bs(url, city)
                    print('网页内容如下：',result)
                    time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    jobcrawler = JobCrawler()