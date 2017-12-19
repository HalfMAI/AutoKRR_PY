from krrRequestBase import _request_get, _request_post
from krrRequestBase import k_KRR_API_URL, krr_current_uuid, krr_current_accesstoken, krr_current_session_id

def version_get():
	api_name = "/app/version/get"
	params = {
		"platform" : "2",
		"version" : "1.0.3"
	}
	response = _request_get(api_name, params)
	print (response)

if __name__ == "__main__":
	version_get()