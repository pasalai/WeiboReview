# Micro-blogReview    
## 2019年12月5日    
* 创建项目
* 分析微博手机端H5页面，得到地址爬取评论
* 太难了，地址得手动获取，每页50条，且反扒机制TQL！    
## 2019年12月6日
* 申请了微博API
* 添加了通过AppKey及AppSecret获取access_token的程序（./weiboAPI）:[olwolf/sinaweibopy3](https://github.com/olwolf/sinaweibopy3)
* 根据开发者文档构建获取评论的链接    
<code>https://api.weibo.com/2/comments/show.json?access_token=[your_access_token]&id=[微博的ID]&count=[1~200]200&page=1</code>
