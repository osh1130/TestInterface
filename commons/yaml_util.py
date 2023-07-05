import os.path
import yaml


class YamlUtil:

    #read yaml file
    def read_yaml(self):
        #os.getcwd()
        with open(os.getcwd()+'/extract.yaml' , encoding="utf-8") as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            print(value)
            return value

    #write data
    def write_yaml(self,data):
        with open(os.getcwd()+'/extract.yaml' , encoding="utf-8", mode="a") as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    def clean_yaml(self):
        with open(os.getcwd()+'/extract.yaml' , encoding="utf-8",mode="w") as f:
            f.truncate()

    def get_path(self):
        return os.path.dirname(__file__).split('commons')[0]

    def read_testcase_yaml(self, yaml_path):
        with open(YamlUtil().get_path()+yaml_path , encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

#if __name__=='__main__':
    #YamlUtil().read_yaml()
    #print(YamlUtil().get_path())