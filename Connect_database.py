import MySQLdb
import pprint

class Cnect_Database(object):
    def __init__(self,ip,user,db,charset):
        self.ip = ip
        self.user = user
        self.db = db
        self.charset = charset

    def connect(self,ps):
        # 连接数据库,获取游标
        self.dadabase = MySQLdb.connect(self.ip,self.user, ps, self.db, charset=self.charset )
        self.cursor = self.dadabase.cursor()
        # 获取数据库版本信息,打印
        self.cursor.execute("SELECT VERSION()")
        data = self.cursor.fetchone()
        print("Database version : %s " % data)

    def register(self,data,namelist,tablename,yearspan):
        # 如果数据表已经存在,删除表。
        self.cursor.execute("DROP TABLE IF EXISTS "+tablename)

        # 建表前准备
        creatlist = namelist.copy()
        for i,ele in enumerate(creatlist):
            if ele == 'year':
                creatlist[i] = ele+' YEAR NOT NULL'
            else:
                creatlist[i] = ele + ' FLOAT'
            # print(ele)
        # 创建数据表SQL语句
        sql = "CREATE TABLE "+tablename+" "+str(tuple(creatlist)).replace("'",'')
        print(sql)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.dadabase.commit()
        except:
            # Rollback in case there is any error
            self.dadabase.rollback()

        # 插入的预处理
        vallist = namelist.copy()
        for i,ele in enumerate(vallist):
            # print(ele)
            if ele == 'year':
                vallist[i] = '2018-index'
            else:
                vallist[i] = 'data['+str(i)+'][index]'
        # 2018-index,eval('total')[index],man[index],woman[index],city[index],  countryside[index]
        # SQL 插入语句
        # print(vallist)
        for index in list(range(0,yearspan)):
            sql = "INSERT INTO "+tablename+str(tuple(namelist)).replace("'",'')+" VALUES {}".format(str(tuple(map(eval,vallist))))
            print(sql)
            try:
            # 执行sql语句
                self.cursor.execute(sql)
                # 提交到数据库执行
                self.dadabase.commit()
                # print('s')
            except:
                # Rollback in case there is any error
                self.dadabase.rollback()

        self.dadabase.close()

    def retrieval(self,itemlist,tablename):
        if itemlist == '*':
            sql = "select * from "+tablename
        else:
            sql = "select "+str(itemlist).replace("'",'').strip('[]')+" from "+tablename
        print(sql)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # pprint.pprint(result)
        self.dadabase.close()
        return result

    