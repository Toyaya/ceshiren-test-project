#####docker run 
- --name名字
- -e:环境变量
- -p:端口号
- -d:后台运行
- -v /dev/shm:/dev/shm 优化内存使用
- --link hub：把hub的网络信息发给node。把hub容器的一些网络信息已环境变量的形方式注入到node容器里。

````
docker run --name=hub -p 5001:4444 -e GRID_TIMEOUT=0 -e GRID_THROW_ON_CAPABILITY_NOT_PRESENT=true -e GRID_NEW_SESSION_WAIT_TIMEOUT=-1 -e GRID_BROWSER_TIMEOUT=15000 -e GRID_TIMEOUT=30000 -e GRID_CLEAN_UP_CYCLE=30000 -d selenium/hub:3.7.1-beryllium
docker run --name=chrome -p 5902:5900 -e NODE_MAX_INSTANCES=6 -e NODE_MAX_SESSION=6 -e NODE_REGISTER_CYCLE=5000 -e DBUS_SESSION_BUS_ADDRESS=/dev/null -v /dev/shm:/dev/shm --link hub -d selenium/node-chrome-debug:3.7.1-beryllium
docker exec -it chrome bash #登录到容器里的命令，docker exec让docker容器运行一条命令，-it开启一个窗口，bash执行一个叫bash的命令
````
#####--link 换成 -e
#####docker让所有的容器共享宿主机的内核，docker运行在lunix
#####网络模式：-p （桥接模式），  --net=host（容器使用宿主机的网络模式）  ， --net=container:B A（容器A使用容器B的网络）

######容器隔离：
- 名称空间隔离（网络名称，进程名称，Mount名称，用户名称<docker不隔离>，ITC进程通讯，Time名称空间）

######解释容器桥接网络？？(https://testerhome.com/topics/9567)
######https://testerhome.com/ycwdaaaa
######https://testerhome.com/topics/16605
######dockerfile理解成制作镜像的脚本
######（面试题）一个run指令就是一层，每多一层就会多一个IO的性能开销。调试中dockerfile用多个run，开发完成后一个run
######docker build命令用于使用 Dockerfile 创建镜像
