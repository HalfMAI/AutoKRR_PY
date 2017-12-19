import configparser

K_KRR_SETTING_FILE = "KRR_Setting.ini"

def config_load_accesstoken():
	return _config_load()['ACCOUNT_INFO']['acc_access_token']
	
def config_load_uuid():
	return _config_load()['ACCOUNT_INFO']['acc_uuid']
	
def config_load_proxy_ip():
	return _config_load()['PROXY_SETTING']['proxy']
def config_load_proxy_onoff():
	return _config_load()['PROXY_SETTING']['is_proxy_on']
	
def config_save_accesstoken(access_token):	
	config = _config_load()
	config['ACCOUNT_INFO']['acc_access_token'] = access_token	
	_config_save_all(config)
	
def _config_save_all(config):
	with open(K_KRR_SETTING_FILE, 'w') as configfile:
		config.write(configfile)

def _config_load():
	config = configparser.ConfigParser()
	config.read(K_KRR_SETTING_FILE)
	return config