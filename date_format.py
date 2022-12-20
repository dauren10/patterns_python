import datetime


def date1():
    dt = datetime.datetime.strptime(
        "2022-12-08T16:57:27.143+06:00", "%Y-%m-%dT%H:%M:%S.%f%z"
    ).timestamp()
    return (
        datetime.datetime.utcfromtimestamp(int(dt)) + datetime.timedelta(hours=6)
    ).strftime("%Y-%m-%dT%H:%M:%S")


print(date1())


def date2():
    data = {}
    data["timestamp"] = "2022-12-08T16:57:27+06:00"
    dt = data["timestamp"]
    return datetime.datetime.fromisoformat(dt).strftime("%Y-%m-%dT%H:%M:%S")


print(date2())
