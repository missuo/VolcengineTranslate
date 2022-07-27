'''
Author: Vincent Young
Date: 2022-07-28 01:52:04
LastEditors: Vincent Young
LastEditTime: 2022-07-28 02:45:52
FilePath: /VolcengineTranslate/volc.py
Telegram: https://t.me/missuo

Copyright © 2022 by Vincent, All Rights Reserved. 
'''
# -*- coding: UTF-8 -*-
import json
from volcengine.ApiInfo import ApiInfo
from volcengine.Credentials import Credentials
from volcengine.ServiceInfo import ServiceInfo
from volcengine.base.Service import Service
from flask import Flask, request

access_key = "Modify this to your access key"
secret_key = "Modify this to your secret key"


app = Flask(__name__)

@app.route('/',methods=['POST'])
def translate():
	data = request.get_json()
	if('text' not in data.keys()):
		error = {
			'code': '404',
			'message':'text not found',
			'github': 'https://github.com/missuo/volc-translate'
		}
		return error
	else:
		text = data['text']
	if('source_lang' in data.keys()):
		source_lang = data['source_lang'].lower()
	else: 
		source_lang = ''
	if('target_lang' in data.keys()):
		target_lang = data['target_lang'].lower()
	else:
		target_lang = 'en'
	k_access_key = access_key
	k_secret_key = secret_key
	k_service_info = \
	ServiceInfo('open.volcengineapi.com',
		{'Content-Type': 'application/json'},
		Credentials(k_access_key, k_secret_key, 'translate', 'cn-north-1'),
		5,
		5)
	k_query = {
		'Action': 'TranslateText',
		'Version': '2020-06-01'
	}
	k_api_info = {
		'translate': ApiInfo('POST', '/', k_query, {}, {})
	}
	service = Service(k_service_info, k_api_info)
	body = {
		'SourceLanguage': source_lang,
		'TargetLanguage': target_lang,
		'TextList': [text],
	}
	res = service.json('translate', {}, json.dumps(body))
	res = json.loads(res)
	if(res['TranslationList'][0]['Translation'] != ''):
		result = {
			'code': 200,
		}
		result['data'] = res['TranslationList'][0]['Translation']
	else:
		result = res
	return result

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=False)