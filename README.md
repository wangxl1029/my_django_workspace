# my_django_workspace
My workspace as a django web site.

version | app 
--------|-----
 v0.3.x | image uploader
 v0.2.x | polls
 v0.1.x | predictive navigation

## deployment

- django 2.1
- python 3.6

## Release

### v0.3.1

+ MTV tutorial: 上传图片的示例，不完全参照。
    - <https://blog.csdn.net/qq_27437781/article/details/80852978>
    - revision: e73bb79612fd4b09a5524510098217c557ac5b4d
+ Discovery:
    - 你会发现同一个文件名上传是没有问题的，Django会为发生了文件名重复的文件生成不同的后缀。
+ 简书Md5的样例：几乎完全参照。
    - <https://www.jianshu.com/p/41a2976418d9>
    - <https://blog.csdn.net/bird73/article/details/79875284>
    - revision: fb3f08789e3e1c1f9c9c2e5d8582b63a0f572b09
+ Models.ImageField: width and height fields example
    - <https://www.cnblogs.com/linkenpark/p/5596365.html>
    - <https://blog.csdn.net/love629891/article/details/79408014>
+ 图片url映射到本地路径：
    - <https://docs.djangoproject.com/zh-hans/2.1/ref/urls/#static>
+ 更改md5码为unique字段：
    - revision: 165e9fcd26eb3922e36480f2dc9a6d7681d1f3b5
+ 指定image field的filesystem storage.
    - revision: 504941e7b18557d73893409fcbfe3e29960ef8c3

### v0.3.0

Image uploader initial version.

### v0.2.2

define administration page. 

- [x] Poll app run OK.
- [x] P-nav app run OK.

### v0.2.1

Poll app 添加测试代码。

- [x] Poll app run OK.
- [x] P-nav app run OK.

### v0.2.0

Poll app的第一阶段版本。

- [x] Poll app run OK.
- [x] P-nav app run OK.

### v0.1.0

P-nav app的第一阶段版本。

check list:

- [x] Poll app run OK.
- [x] P-nav app run OK.

时区设置参考：<https://www.cnblogs.com/brad1994/p/6761110.html>
