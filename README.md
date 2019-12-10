# Micro-blogReview    
微博评论/爬虫/数据分析/python/数据挖掘    
爬取指定的微博的评论，并进行情感分析    
## 运行说明    
* 首先在[微博开发者平台](https://open.weibo.com)注册登录，并申请，[申请流程点这里](https://www.douban.com/note/449162780/)。
* 获取到开发者接口的App Key及App Secret(无需开发者认证及高级接口申请)
* 在应用接口管理页面的<code>应用信息>高级信息>OAuth2.0 授权设置</code>中的<code>授权回调页</code>填写<code>http://api.weibo.com/oauth2/default.html</code>
* 获取<code>accessoken</code>:    
将得到的App Key及App Secret值填入本程序<code>./weiboApi/weiboApi.py</code>中对应的值，运行后将自动打开浏览器的<code>微博OAuth2.0</code>页面，在url中，包含一个<code>code=*****</code>，复制code值，回到本程序，将code的值填入程序运行后的输入栏，运行后输出<code>accesstoken</code>
* 根据开发者文档的评论接口页面的接口说明，使用获得的accesstoken及相关微博文章的ID构造API链接，访问，并复制cookie,将<code>./start.py</code>中链接及cookie替换。
* 运行<code>./start.py</code>，数据会自动格式化并保存至<code>./outPut/评论.csv</code>
## 更新日志    
### 2019年12月5日    
* 创建项目
* 分析微博手机端H5页面，得到地址爬取评论
* 太难了，地址得手动获取，每页50条，且反扒机制TQL！    
## 2019年12月6日
* 申请了微博API
* 添加了通过AppKey及AppSecret获取access_token的程序（./weiboAPI）:[olwolf/sinaweibopy3](https://github.com/olwolf/sinaweibopy3)
* 根据开发者文档构建获取评论的链接    
<code>https://api.weibo.com/2/comments/show.json?access_token=[your_access_token]&id=[微博的ID]&count=[1~200]200&page=1</code>

hehe