import requests
import time
import pprint
import Connect_database
import create_fig
import get_from_web


if __name__ == '__main__':

    datanodes = get_from_web.nation_stat('A0302')
    # pprint.pprint(datanodes)

    # total = []
    # first = []
    # second = []
    # third = []
    d = ['year','born','die','increase']
    for i in range(len(d)):
        cmd = d[i]+' = []'
        exec(cmd)

    for num,ele in enumerate(datanodes):
        for i in range(len(d)-1):
            if num//20 == i:
                cmd = d[i+1]+".append(ele['data']['data'])"
                # print(cmd)
                eval(cmd)
            else:
                # print('overflow')
                pass

    # exit()
    # 连接数据库预信息
    f = open('ps.txt','r')
    ps = f.readline()
    tablename = 'Population_change'
    yearspan = 20
    db = Connect_database.Cnect_Database("127.0.0.1", "root", "population", 'utf8')
    # 连接,登记
    db.connect(ps)
    db.register(eval(str(d).replace("'",'').replace('year','[]')),d,tablename,yearspan)
    # 连接,查询
    db.connect(ps)
    result = db.retrieval('*',tablename)
    # pprint.pprint(result)

    create_fig.drawHW2(d,result)

