##### har2case mulu/xxx.har 默认生出pytest python格式
##### har2case mulu/xxx.har -2j 生出json格式
##### har2case mulu/xxx.har -2y 生出yaml格式

#####.with_jmespath("body.data.list.0.id","id")   参数化关联：把提取出来的值 命名为id。 后续通过$id来引用。和.extract().with_jmespath
```
step(
  RunRequest("用例名称")
  .post("url")
  .with_headers(
    **{
    header
    }
  )
  .with_json({json})
  .extract() #从相应里面提取东西
  .validate()#校验
    
)
```

