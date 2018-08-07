#!/usr/bin/python
#coding=utf-8

import telnetlib
import time


def doTelnet(url):
    ports = {20:'ftp 默认的数据和命令传输端口[可明文亦可加密传输] ,允许匿名的上传下载,爆破,嗅探,win提权,远程执行(proftpd 1.3.5),各类后门(proftpd,vsftp 2.3.4)',
             21:'ftp 默认的数据和命令传输端口[可明文亦可加密传输] ,允许匿名的上传下载,爆破,嗅探,win提权,远程执行(proftpd 1.3.5),各类后门',
             22:'ssh[数据ssl加密传输] 可根据已搜集到的信息尝试爆破,v1版本可中间人,ssh隧道及内网代理转发,文件传输,等等…常用于linux远程管理…',
             23:'telnet[明文传输] 爆破,嗅探,一般常用于路由,交换登陆,可尝试弱口令,也许会有意想不到的收获',
             25:'smtp[简单邮件传输协议,多数linux发行版可能会默认开启此服务]	邮件伪造,vrfy/expn 查询邮件用户信息,可使用smtp-user-enum工具',
             53:'dns[域名解析]	允许区域传送,dns劫持,缓存投毒,欺骗以及各种基于dns隧道的远控',
             69:'tftp[简单文件传输协议,无认证]	尝试下载目标及其的各类重要配置文件',
             139:'[smb实现windows和linux间文件共享,明文],可尝试爆破以及smb自身的各种远程执行类漏洞利用,如,ms08-067,ms17-010,嗅探',
             445:'[smb实现windows和linux间文件共享,明文],可尝试爆破以及smb自身的各种远程执行类漏洞利用,如,ms08-067,ms17-010,嗅探',
             389:'ldap[轻量级目录访问协议]',
             512:'linux rexec	可爆破,rlogin登陆',
             513:'linux rexec	可爆破,rlogin登陆',
             514:'linux rexec	可爆破,rlogin登陆',
             873:'rsync备份服务	匿名访问,文件上传',
             1090:'RMI服务 远程命令执行',
             1099:'RMI服务 远程命令执行',
             1352:'Lotus domino邮件服务,弱口令,信息泄漏,爆破',
             1433:'mssql数据库,注入,提权,sa弱口令,爆破',
             1521:'oracle数据库	tns爆破,注入,弹shell…',
             1500:'ispmanager 主机控制面板',
             2181:'zookeeper 未授权访问',
             2375:'Docker Remote API',
             2601:'zebra路由	默认密码zerbra',
             2604:'zebra路由	默认密码zerbra',
             3128:'squid代理服务,弱口令',
             3306:'mysql数据库	注入,提权,爆破',
             3389:'windows rdp远程桌面	shift后门[需要03以下的系统],爆破,ms12-020[蓝屏exp]',
             4848:'glassfish控制台	弱口令',
             5000:'sybase/DB2数据库',
             5432:'postgresql数据库',
             5984:'CouchDB	未授权导致的任意指令执行',
             6379:'redis未授权	可尝试未授权访问,弱口令爆破',
             7001:'weblogic控制台,java反序列化,弱口令',
             7002:'weblogic控制台,java反序列化,弱口令',
             8012:'jres弱口令',
             8069:'zabbix,远程执行,sql注入',
             8080:'Apache/Tomcat/Nginx等中间件',
             11211:'Memcache服务 未授权访问'
            }

    port = ports.keys()
    value = ports.values()


    for i in range(0,port.__len__()):
        time.sleep(1)
        try:
            tn = telnetlib.Telnet(url, port[i], timeout=2)

            if (tn):
                print(str(port[i])+'：'.decode("utf-8").encode("gbk")+value[i].decode("utf-8").encode("gbk"))
            else:
                continue
        except:
            pass

if "__main__" == __name__:

    print("请输入url或者ip,如：www.baidu.com/127.0.0.1：".decode("utf-8").encode("gbk"))
    url = raw_input()
    doTelnet(url)