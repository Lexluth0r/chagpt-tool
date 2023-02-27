# 使用[acheong08](https://github.com/acheong08/ChatGPT)的非官方ChatGPT接口，实现简单API接口



## 配置并运行

1.
```sh
cp config.json_bk config.json
```
2. 配置config文件，推荐使用 access_token 方式认证（注意access_token 会过期）。

- 获取 [access_token](https://chat.openai.com/api/auth/session) 

3. 构建镜像
```sh
docker build -t chatgpt-tool .
```
4. 启动项目

```sh
docker-compose up
```
5. 通过接口访问

```curl

curl --location '127.0.0.1:9999/api/chat' \
--header 'Content-Type: application/json' \
--data '{
    "question":"who am i"
}'
```

