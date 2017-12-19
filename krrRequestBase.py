import requests
import hashlib

from configReader import config_load_accesstoken, config_load_uuid, config_load_proxy_ip, config_load_proxy_onoff


k_KRR_API_URL = "https://krr-prd.star-api.com"

k_KRR_KEY = "85af4a94ce7a280f69844743212a8b" + "867206ab28946e1e30e6c1a10196609a11"	# for search engine
k_APP_VER = "1.0.3"
k_STAR_VER = "3"
k_UNITY_VER = "5.5.4f1"


krr_current_uuid = config_load_uuid()
krr_current_accesstoken = config_load_accesstoken()
krr_current_session_id = None

tmp_proxy_onoff = config_load_proxy_onoff()


def common_header(api_name=None, post_data=None):
	requesthash = ""
	requesthash = requesthash + ((krr_current_session_id + " ") if krr_current_session_id!=None else "")
	requesthash = requesthash + api_name + " "
	requesthash = requesthash + ((post_data + " ") if post_data!=None else "")
	requesthash = requesthash + k_KRR_KEY	
	requesthash = requesthash.encode('utf-8')
	requesthash = hashlib.sha256(requesthash).hexdigest()
	ret_headers = {
		'Unity-User-Agent': "app/0.0.0; Android OS 5.1.1 / API-22 LMY48Z/eng..20171207.185924; samsung SM-G925F",
		'X-STAR-REQUESTHASH': requesthash,
		'X-STAR-SESSION-ID': krr_current_session_id,
		'X-Unity-Version': k_UNITY_VER,
		'X-STAR-AB': k_STAR_VER,
		'Content-Type': "application/json",
		'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G925F Build/LMY48Z)",
		'Accept-Encoding': "gzip, deflate"
	}	
	return ret_headers
	
def _request_get(api_name, params):
	tmp_result_url = k_KRR_API_URL + "/api" + api_name
	tmp_headers = common_header(api_name)
	
	if config_load_proxy_onoff():
		tmp_http_proxy  = config_load_proxy_ip()
		tmp_https_proxy = config_load_proxy_ip()
		tmp_proxyDict = {"http":tmp_http_proxy, "https": tmp_https_proxy}
		response = requests.request("GET", tmp_result_url, headers=tmp_headers, params=params, proxies=tmp_proxyDict)		
	else:
		response = requests.request("GET", tmp_result_url, headers=tmp_headers, params=params)	
	return response.text

def _request_post(api_name, paramsDict):	
	tmp_result_url = k_KRR_API_URL + "/api" + api_name
	
	try:
		payload = json.dumps(paramsDict)
	except TypeError as e:
		print(e)
		return None
	
	tmp_headers = common_header(api_name, payload)
	
	if config_load_proxy_onoff():
		tmp_http_proxy  = config_load_proxy_ip()
		tmp_https_proxy = config_load_proxy_ip()
		tmp_proxyDict = {"http"  : tmp_http_proxy, "https" : tmp_https_proxy}
		response = requests.request("POST", tmp_result_url, data=payload, headers=headers, proxies=tmp_proxyDict)
	else:
		response = requests.request("POST", tmp_result_url, data=payload, headers=headers)
	return response.text