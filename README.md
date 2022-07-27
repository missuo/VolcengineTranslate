
English｜[简体中文](https://github.com/missuo/VolcengineTranslate/blob/master/README_CN.md)

## Description
VolcengineTranslate is a simple API written in Flask that allows you to translate.

## Preparation
You should go to the official website of [Volcano Engine](https://www.volcengine.com/product/machine-translation) and apply for access to machine translation. And create your `access_key` and `secret_key`.

## Usage
1. Modify Line 19 and 20 in `volc.py`.
2. Install Dependencies.
    ```bash
    pip install volcengine flask
    ```
3. Run Python File.
    ```bash
    python volc.py
    ```

## Call API
**Defult Host: `http://localhost:5000`** 

**Request(source_lang is Optional)**
```json
{
   "source_lang":"en",
   "target_lang":"zh",
   "text":"Hello World!"
}
```
**Response**
```json
{
   "code":200,
   "text":"你好世界!"
}
```

## Deployment On the Server(e.g. Ubuntu)
```bash
sudo apt-get update
sudo apt-get install python3-pip python3 nginx
sudo pip3 install flask volcengine
python3 volc.py
```
**You can configure your own reverse proxy using `Nginx` to make the API publicly accessible.**

## License
MIT License



