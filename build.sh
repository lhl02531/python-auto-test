echo "运行容器python执行自动化"  #输出日志
#-w=$WORKSPACE：指定workspace
#--volumes-from=jenkins_save01：将jenkins容器中的workspace映射到python容器中，此时jenkins中git拉下来的代码就会被映射进去
sudo docker run --rm -w=$WORKSPACE --volumes-from=jenkins lv_python_test:v1
echo "python执行自动化执行成功"


#作者：haili
#链接：http://testingpai.com/article/1644570535388
#来源：测试派
#协议：CC BY-SA 4.0 https://creativecommons.org/licenses/by-sa/4.0/