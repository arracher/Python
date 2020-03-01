import os,shutil,re
def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path+' 创建成功')
        return True
    else:
        print(path+' 目录已存在')
        return False

fpath=input("请输入xshell工具的session创建路径(文件夹不存在则自动创建):\n")
mkdir(fpath)
iplist=open("C:\\Users\\DieDieKun\\Desktop\\ip.txt",'r+',encoding='UTF-8',errors='ignore')
for ip in iplist:
    ip_host_list=ip.strip()
#p=re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    p = re.compile(r"(.*)\s(([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3}))")
    ip_host = p.match(ip_host_list).group().split()
    if p.match(ip_host_list):
        print(fpath+"\\"+ip_host_list+".xsh 生成成功")
        shutil.copy(fpath+"\\default1",fpath+"\\"+ip_host_list+".xsh")
        f1 = open(fpath+"\\"+ip_host_list+".xsh",'r+',errors='ignore')
        infos = f1.readlines()
        f1.seek(0,0)
        for line in infos:
            line_new = line.replace("xxx.xxx.xxx.xxx",ip_host[1])
            f1.write(line_new)
        f1.close()
    else:
        print(ip+"此行为空行或不是IP,已自动过滤")
iplist.close()
input("\nsession已生成完成,请按Enter键退出")