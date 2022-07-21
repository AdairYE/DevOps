from django.urls import path
from OpsTools import views

urlpatterns = [
    # 数据库管理
    path('dbms/index/',views.index,name="dbms_index"),
    path('dbms/sqlExec/',views.sqlExec,name="dbms_sqlExec"),

]