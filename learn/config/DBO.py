import sqlite3


class conn():
    def __init__(self):
        self.conn = sqlite3.connect('G:\\yfaf\\config\\test.db')
        print("数据库链接成功!")

    def getAllInfo(self):
        c = self.conn.cursor()
        cursor = c.execute("SELECT * FROM app_update;")

        configList = []

        for row in cursor:
            config = {}
            config["id"] = row[0]
            config["version_name"] = row[1]
            config["version_code"] = row[2]
            config["description"] = row[3]
            config["download_url"] = row[4]
            config["publish_time"] = row[5]
            configList.append(config)
        return configList

if __name__ == "__main__":
    c = conn()
    configList = c.getAllInfo()
    print(configList)