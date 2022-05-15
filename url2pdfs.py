#fc-list :lang=zh 
# _*_ coding: UTF-8 _*_
# https://www.cnblogs.com/xiaowenshu/p/9916719.html
# https://blog.csdn.net/qq_36490364/java/article/details/83035033
# https://zhuanlan.zhihu.com/p/94608155

import requests
import time,os
import pdfkit

def url_2_pdf():
    header={
    'uer-aGent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    'Referer':'http://10.70.61.87:9090/dologin.action',
    'Host':'10.70.61.87:9090'
    }


    postdata={
    'os_username':"",
    'os_password':"",
    'login': '登录'
    }
    session = requests.Session()
    #登录
    def Getcookiesandlogin():
        posturl = 'http://10.70.61.87:9090/dologin.action'
        session.get('10.70.61.87:9090',headers=header)#通过这次来获取cookie
        postdata['os_cookie'] = session.cookies.get_dict()['Cookie']  # 把cookie加入表单参数中
        session.post(posturl, data=postdata,headers=header)


    urllist = [
    "http://10.70.61.87:9090/pages/viewpage.action?pageId=41647534",
    "http://10.70.61.87:9090/pages/viewpage.action?pageId=45303909"
               ] # 一篇博客的url

    nameslist=["人工智能研究所主页",
    "产品研发"]
    for url,name in zip(urllist,nameslist):
        confg = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
        # 这里指定一下wkhtmltopdf的路径，这就是我为啥在前面让记住这个路径
        pdfkit.from_url(url, name+'.pdf', configuration=confg)
        time.sleep(2)
        # from_url这个函数是从url里面获取内容
        # 这有3个参数，第一个是url，第二个是文件名，第三个就是khtmltopdf的路径

        # pdfkit.from_file('my.html', 'jmeter_下载文件2.pdf',configuration=confg)
        # from_file这个函数是从文件里面获取内容
        # 这有3个参数，第一个是一个html文件，第二个是文生成的pdf的名字，第三个就是khtmltopdf的路径

        html = '''
        <div>
        <h1>title</h1>
        <p>content</p>
        </div>
        '''  # 这个html是我从一个页面上拷下来的一段，也可以

        # pdfkit.from_string(html, 'jmeter_下载文件3.pdf',configuration=confg)
        # from_file这个函数是从一个字符串里面获取内容
        # 这有3个参数，第一个是一个字符串，第二个是文生成的pdf的名字，第三个就是khtmltopdf的路径



def html_file2pdf(html, to_file):
    # 将wkhtmltopdf.exe程序绝对路径传入config对象
    path_wkthmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    # 生成pdf文件，to_file为文件路径
    pdfkit.from_file(html, to_file, configuration=config)



if __name__ == '__main__':
    # 获取目标文件夹的路径
    path = './txt/'
    # 获取当前文件夹中的文件名称列表
    filenames = os.listdir(path)
    # 先遍历文件名
    count = 0
    for filename in filenames:
        count+=1
        try:
            filepath = path +filename
            # 遍历单个文件，读取行数
            # url_2_pdf()
            html_file2pdf(filepath, filepath.split()[0]+'.pdf')
        except Exception as e:
            print(e)
        if count%50==0:
            print(count,": ",filepath,"\n")
    print('完成')
