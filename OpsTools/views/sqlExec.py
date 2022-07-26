from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from OpsTools.models import dbms
from OpsTools.views.mysql_db_exec import mysqlDB
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def sqlExec(request):
    executeInfo = {"status": "true", "msg": None, "data": None}
    if request.method == "GET":
        dbInfo = dbms.objects.all().order_by("-id")
        return render(request, "dbms/sqlExec.html", {"dbInfo": dbInfo})
    elif request.method == "POST":
        req = json.load(request)
        dbname = req["db"]
        execSql = req["sql"]
        dbInfo = dbms.objects.get(name=dbname)
        dbHost = dbInfo.dbHost
        dbPort = dbInfo.dbPort
        dbUser = dbInfo.dbUser
        dbPasswd = dbInfo.dbPasswd
        dbHouse = dbInfo.dbHouse

        try:
            mysql = mysqlDB(dbHost, dbPort, dbUser, dbPasswd, dbHouse)
            db = mysql.DBconn()  # 数据库链接

            result = mysql.SQLexec(db, execSql) # 获取数据总数
            allrow = len(result["results"])

            # execSql = execSql + "LIMIT {offset},10".format(offset=)
            result = mysql.SQLexec(db, execSql)
            db.close()  # 断开数据库链接

            header = []
            for head in result["fields"]:
                header.append(head[0])
            results = []
            for result in result["results"]:
                results.append(result)

            executeInfo["data"] = {
                "header": header,
                "results": results,
                "allrow":allrow
            }
            print("格式化执行结果:", executeInfo)
        except Exception as e:
            executeInfo["status"] = "false"
            executeInfo["msg"] = str(e)

        return JsonResponse(executeInfo)
