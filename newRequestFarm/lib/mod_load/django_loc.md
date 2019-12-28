

django 的请求体参数会封装程QueryDict对象
1、请求 的取值方式GET对应的是请求形式 dict.get('键'， '默认值')<<GET.get()>>, dict.getList()<<GET.getList()>>获取多个值
2、 postMan的使用

3、请求体，表单类获取： request.POST  ==> get(), getList()

4、如果是非表单格式的请求体（json，或其他格式）使用request.body,返回bytes类型
eg: json_bytes = request.body
json_dict = json.loads(json_bytes.decode('utf-8')
json_dict.get()

5、请求头 request.META

6、响应体（Response, JsonResponse)
 response = HttpResponse(s, content_type="appliction/json", status=200)
 构造响应头
 response['itcase'] = 'heima'
 return response

7 Cookie的设置： HttpResponse.setcookie()

8 Session django默认开启Session
  广义session机制 -》会话， 用于多次记录http请求关系
  狭义 -> 保持会话，验证会话
  存在后端，可以放在数据库中，本地缓存（内存或全局变量）文件



 9 类的装饰器的增加方法
  (1) 在URL中添加装饰器
  （2) 在类中添加装饰器
  (3) python中的多继承， 如果继承的是同一父类，则先找同级目录下的子类

  10 中间件： 中间件用的是全局，所有的视图函数
