
[English](https://github.com/missuo/VolcengineTranslate/blob/master/README.md)｜简体中文

## 介绍
VolcengineTranslate是一个用Flask框架编写的翻译接口。

## 准备工作
你应该去[火山引擎](https://www.volcengine.com/product/machine-translation)的官方网站，申请访问机器翻译。并创建你的`access_key`和`secret_key`。

## 使用方法
1. 修改`volc.py`中的第19和20行。
2. 安装依赖项。
```bash
pip install volcengine flask
```
3. 运行Python文件。
```bash
python volc.py
```
## 调用API
**默认API: `http://localhost:5000`**

**请求(source_lang是可选项)**
```json
{
"source_lang": "en",
"target_lang": "zh",
"text": "Hello World!"
}
```
**响应**
```json
{
"code":200,
"text": "你好世界！"
}
```
## 部署在服务器上(如Ubuntu)
```bash
sudo apt-get update
sudo apt-get install python3-pip python3 nginx
sudo pip3 install flask volcengine
python3 volc.py
```
**你可以使用`Nginx`配置你自己的反向代理，使API可以公开访问。**
## License
MIT License