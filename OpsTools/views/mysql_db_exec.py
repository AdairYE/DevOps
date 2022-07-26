import pymysql

class mysqlDB:
  """
  链接mysql数据库执行sql
  """

  def __init__(self, host, port, user, passwd, db):
    self.host = host
    self.port = port
    self.user = user
    self.passwd = passwd
    self.db = db

  def DBconn(self):
    if not isinstance(self.port,int):
      self.port = int(self.port)
    try:
      db = pymysql.connect(
        host=self.host,
        port=self.port,
        user=self.user,
        passwd=self.passwd,
        db=self.db,
        charset='utf8',
        connect_timeout=180
      )
      print("链接数据库:%s:%s@%s" %(self.host,self.port,self.db))
      return db
    except Exception as e:
      print("数据库链接失败:", e)
      raise Exception(
        "数据库链接失败:", e
      )

  def SQLexec(self, db,sql):
    try:
      print("sql:",sql)
      cursor = db.cursor()
      cursor.execute(sql)
      results = cursor.fetchall()  # sql 执行数据
      fields = cursor.description  # 获取字段名

      return {
        "results":results,
        "fields":fields
      }
    except Exception as e:
      raise Exception(
        "sql执行失败:", e
      )

