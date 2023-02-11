import time

class logs_time:
    def aw_log(self, dest="", name="", v="", ip=""):
        f = open(dest, "a", encoding="utf-8")
        date_time = time.strftime("%a %b %d %H:%M:%S", time.localtime())

        content = f"""DATA:[{date_time}] NAME:[{name}] V:[{v}] ip:[{ip}]"""

        f.write(content + "\n")
        f.close()


