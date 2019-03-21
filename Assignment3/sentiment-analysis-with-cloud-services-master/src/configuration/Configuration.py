import os
from configparser import ConfigParser


class Configuration:

    config_dir = [os.path.abspath(os.path.dirname(__file__)) + '/../../conf/', '']

    conf_filename = {
        'app': 'app.cfg',
    }

    def __init__(self):
        app_config = self._read_config(filename=self.conf_filename['app'])
        if app_config is not None:
            try:
                self.log_path = app_config.get(section='log', option='path')

                self.aws_access_key_id = app_config.get(section='amazon-cred', option='aws_access_key_id')
                self.aws_secret_access_key = app_config.get(section='amazon-cred', option='aws_secret_access_key')
                self.aws_region_name = app_config.get(section='amazon-cred', option='region_name')

                self.azure_subscription_key = app_config.get(section='azure-cred', option='subscription_key')

                self.ibm_iam_apikey = app_config.get(section='ibm-cred', option='iam_apikey')
                self.ibm_url = app_config.get(section='ibm-cred', option='url')

                self.gcp_file_path = app_config.get(section='google-cred', option='gcp_file_path')
            except Exception as e:
                print(e)
                print("Error while reading app config file")

    def _read_config(self, filename):
        config = ConfigParser()
        cfg_file = None
        try:
            for correct_dir in self.config_dir:
                cfg_file = correct_dir + filename
                if os.path.exists(cfg_file):
                    config.read_file(open(cfg_file))
                    return config
                else:
                    continue
        except Exception as e:
            print(e)
            print(cfg_file + " Not Found!")
            return None

    def get_log_path(self):
        return self.log_path

    def get_aws_access_key_id(self):
        return self.aws_access_key_id

    def get_aws_secret_access_key(self):
        return self.aws_secret_access_key

    def get_aws_region_name(self):
        return self.aws_region_name

    def get_azure_subscription_key(self):
        return self.azure_subscription_key

    def get_ibm_iam_apikey(self):
        return self.ibm_iam_apikey

    def get_ibm_url(self):
        return self.ibm_url

    def get_gcp_file_path(self):
        return self.gcp_file_path


if __name__ == "__main__":
    configuration = Configuration()
