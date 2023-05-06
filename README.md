# PrometheusFastApiInstrumentator
FastApi的普罗米修斯中间件
prometheus-client~=0.12.0
+ 增加对返回数据包 {"code":200,"data":"success"} code的值监控

### 使用方式：
- 在FastApi的app启动时挂载
```
@app.on_event('startup')
async def startup():
    # 初始化
    # 监控插件，接入普罗米修斯
    instrumentator = Instrumentator()
    instrumentator.instrument(app).expose(app)
```
