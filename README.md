RPyC - Transparent, Symmetric Distributed Computing

安装
```
$ pip install rpyc
```


参考：

github项目地址：[https://github.com/tomerfiliba/rpyc](https://github.com/tomerfiliba/rpyc)

基于对称协议的服务解耦：[Decoupled Services](http://rpyc.readthedocs.org/en/latest/docs/services.html#services)


分布式模型：

1、单生产者-多消费者网络模型
```
                 server
              [IP_S:PORT_S]
              /           \
             /             \
    client_01               client_02
[IP_C_01:PORT_C_01]     [IP_C_02:PORT_C_02]
```

2、单生产者-多消费者（水平扩展）网络模型
```
      server_01               server_02
        /   \                   /   \
client_01   client_02   client_03   client_04
```

3、多生产者-多消费者网络模型
```
server_01   server_02
    |     \/    |
    |     /\    |
client_01   client_02
```
