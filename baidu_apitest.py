# coding=utf-8
import base64
import urllib
import urllib.request
import urllib.parse
import time
import json


def image_to_base64(image_path):
    image_data = open(image_path, "rb")
    temp = image_data.read()
    base64_data = base64.b64encode(temp)
    image_data.close()
    data_string = str(base64_data)
    data_string = data_string.strip('\'b')
    print(data_string)
    return data_string


def register(username, image=[]):
    url = 'http://apis.baidu.com/idl_baidu/faceverifyservice/face_register'
    reg = r'{"params": [{"username": "%s", "cmdid": "1000", "appid": "bcd24781cd71c7fe421d066e4427cef9", "clientip": "192.168.2.156","type": "st_groupverify", "groupid": "0", "versionnum": "1.0.0.1", "images": ["%s"]}], "jsonrpc": "2.0","method": "Register"}'%(username, image[0])

    byte_data = reg.encode(encoding="utf-8")
    req = urllib.request.Request(url, data=byte_data)
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    req.add_header("apikey", "bcd24781cd71c7fe421d066e4427cef9")

    try:
        resp = urllib.request.urlopen(req)
        content = resp.read()
        if content:
            print(content)
    except Exception:
        resp = urllib.request.urlopen(req)
        content = resp.read()
        if content:
            print(content)


def verify(username, image=[]):
    url = 'http://apis.baidu.com/idl_baidu/faceverifyservice/face_verify'
    reg = r'{"params": [{"username": "%s", "cmdid": "1000", "appid": "bcd24781cd71c7fe421d066e4427cef9", "clientip": "192.168.2.156","type": "st_groupverify", "groupid": "0", "versionnum": "1.0.0.1", "images": ["%s"]}], "jsonrpc": "2.0","method": "Verify"}'%(username, image[0])

    byte_data = reg.encode(encoding="utf-8")
    req = urllib.request.Request(url, data=byte_data)
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    req.add_header("apikey", "bcd24781cd71c7fe421d066e4427cef9")
    try:
        resp = urllib.request.urlopen(req)
        content = resp.read()
        if content:
            print(content)
        return content
    except Exception:
        resp = urllib.request.urlopen(req)
        content = resp.read()
        if content:
            print(content)
        return content


def recognize(image=[]):
    url = 'http://apis.baidu.com/idl_baidu/faceverifyservice/face_recognition'
    reg = r'{"params": [{"cmdid": "2002", "appid": "bcd24781cd71c7fe421d066e4427cef9", "clientip": "192.168.2.156","type": "st_groupverify", "groupid": "0", "versionnum": "1.0.0.1", "images": ["%s"]}], "jsonrpc": "2.0","method": "Verify"}' % (image[0])

    byte_data = reg.encode(encoding="utf-8")
    req = urllib.request.Request(url, data=byte_data)
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    req.add_header("apikey", "bcd24781cd71c7fe421d066e4427cef9")

    resp = urllib.request.urlopen(req)
    content = resp.read()
    if content:
        print(content)


def compare(image1, image2):
    url = 'http://apis.baidu.com/idl_baidu/faceverifyservice/face_compare'
    reg = r'{"params": [{"cmdid": "1000", "appid": "bcd24781cd71c7fe421d066e4427cef9", "clientip": "192.168.2.156","type": "st_groupverify", "groupid": "12345", "versionnum": "1.0.0.1", "usernames": {"name1": "name1", "name2": "name2"}, "images": {"name1": "%s", "name2": "%s"}, "cates": {"name1":"7", "name2":"7"}}], "jsonrpc": "2.0","method": "Compare"}' % (image1, image2)
    byte_data = reg.encode(encoding="utf-8")
    req = urllib.request.Request(url, data=byte_data)
    req.add_header("apikey", "bcd24781cd71c7fe421d066e4427cef9")
    try:
        resp = urllib.request.urlopen(req)
        content = resp.read()
        if content:
            print(content)
        return content
    except Exception:
        resp = urllib.request.urlopen(req)
        content = resp.read()
        if content:
            print(content)
        return content


def register_verify():
    lfw_file = open("pairs_test.txt")
    res_file = open("res001.txt", "a+")
    count = 1
    while 1:
        image_path = "E:\\zhangbin\\Data\\lfw\\lfw\\lfw\\"
        line = lfw_file.readline()
        if not line:
            break
        line = line.strip('\n')
        images = line.split('\t')
        if len(images) > 3:
            register_image = image_path + images[0] + "\\" + images[0] + "_"
            if len(images[1]) < 2:
                register_image = register_image + "000" + images[1] + ".jpg"
            elif len(images[1]) < 3:
                register_image = register_image + "00" + images[1] + ".jpg"
            elif len(images[1]) < 4:
                register_image = register_image + "0" + images[1] + ".jpg"
            else:
                register_image = register_image + images[1] + ".jpg"

            verify_image = image_path + images[2] + "\\" + images[2] + "_"
            if len(images[3]) < 2:
                verify_image = verify_image + "000" + images[3] + ".jpg"
            elif len(images[3]) < 3:
                verify_image = verify_image + "00" + images[3] + ".jpg"
            elif len(images[3]) < 4:
                verify_image = verify_image + "0" + images[3] + ".jpg"
            else:
                verify_image = verify_image + images[3] + ".jpg"
        else:
            register_image = image_path + images[0] + "\\" + images[0] + "_"
            if len(images[1]) < 2:
                register_image = register_image + "000" + images[1] + ".jpg"
            elif len(images[1]) < 3:
                register_image = register_image + "00" + images[1] + ".jpg"
            elif len(images[1]) < 4:
                register_image = register_image + "0" + images[1] + ".jpg"
            else:
                register_image = register_image + images[1] + ".jpg"

            verify_image = image_path + images[0] + "\\" + images[0] + "_"
            if len(images[2]) < 2:
                verify_image = verify_image + "000" + images[2] + ".jpg"
            elif len(images[2]) < 3:
                verify_image = verify_image + "00" + images[2] + ".jpg"
            elif len(images[2]) < 4:
                verify_image = verify_image + "0" + images[2] + ".jpg"
            else:
                verify_image = verify_image + images[2] + ".jpg"

        if count % 300 == 0:
            time.sleep(1.2)

        print(register_image)
        print(verify_image)

        username = "reg_ver_t4_" + str(count)
        register(username, image_to_base64(register_image))

        content = verify(username, image_to_base64(verify_image))
        str_content = str(content)
        str_score = str_content.split(",")[3]
        score = str_score.split(":")[1]
        digit_score = score.strip('\"')
        res_file.write(digit_score+'\n')
        count += 1

    lfw_file.close()
    res_file.close()


def verify_one_by_one():
    url_reg = 'http://apis.baidu.com/idl_baidu/faceverifyservice/face_register'
    url_ver = 'http://apis.baidu.com/idl_baidu/faceverifyservice/face_verify'
    reg = r'{"params": [{"username": "verify_test01_00","cmdid": "1000","appid": "bcd24781cd71c7fe421d066e4427cef9","clientip": "192.168.2.156","type": "st_groupverify","groupid": "0","versionnum": "1.0.0.1","images": ["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"]}],"jsonrpc": "2.0","method": "Register"}'
    ver = r'{"params": [{"username": "verify_test01_00","cmdid": "1000","appid": "bcd24781cd71c7fe421d066e4427cef9","clientip": "192.168.2.156","type": "st_groupverify","groupid": "0","versionnum": "1.0.0.1","images": ["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"]}],"jsonrpc": "2.0","method": "Verify"}'

    byte_data_reg = reg.encode(encoding="utf-8")
    req_reg = urllib.request.Request(url_reg, data=byte_data_reg)
    req_reg.add_header("Content-Type", "application/x-www-form-urlencoded")
    req_reg.add_header("apikey", "bcd24781cd71c7fe421d066e4427cef9")
    resp_reg = urllib.request.urlopen(req_reg)
    content_reg = resp_reg.read()
    if content_reg:
        print(content_reg)

    byte_data_ver = ver.encode(encoding="utf-8")
    req_ver = urllib.request.Request(url_ver, data=byte_data_ver)
    req_ver.add_header("Content-Type", "application/x-www-form-urlencoded")
    req_ver.add_header("apikey", "bcd24781cd71c7fe421d066e4427cef9")
    resp_ver = urllib.request.urlopen(req_ver)
    content_ver = resp_ver.read()
    if content_ver:
        print(content_ver)


def compare_test():
    lfw_file = open("pairs_baidu.txt")
    res_file = open("res_baidu.txt", "a+")
    for i in range(0, 4931):
        lfw_file.readline()
    count = 0
    while 1:
        image_path = "E:\\zhangbin\\Data\\lfw\\lfw\\lfw\\"
        line = lfw_file.readline()
        if not line:
            break
        line = line.strip('\n')
        images = line.split('\t')
        if len(images) > 3:
            register_image = image_path + images[0] + "\\" + images[0] + "_"
            if len(images[1]) < 2:
                register_image = register_image + "000" + images[1] + ".jpg"
            elif len(images[1]) < 3:
                register_image = register_image + "00" + images[1] + ".jpg"
            elif len(images[1]) < 4:
                register_image = register_image + "0" + images[1] + ".jpg"
            else:
                register_image = register_image + images[1] + ".jpg"

            verify_image = image_path + images[2] + "\\" + images[2] + "_"
            if len(images[3]) < 2:
                verify_image = verify_image + "000" + images[3] + ".jpg"
            elif len(images[3]) < 3:
                verify_image = verify_image + "00" + images[3] + ".jpg"
            elif len(images[3]) < 4:
                verify_image = verify_image + "0" + images[3] + ".jpg"
            else:
                verify_image = verify_image + images[3] + ".jpg"
        else:
            register_image = image_path + images[0] + "\\" + images[0] + "_"
            if len(images[1]) < 2:
                register_image = register_image + "000" + images[1] + ".jpg"
            elif len(images[1]) < 3:
                register_image = register_image + "00" + images[1] + ".jpg"
            elif len(images[1]) < 4:
                register_image = register_image + "0" + images[1] + ".jpg"
            else:
                register_image = register_image + images[1] + ".jpg"

            verify_image = image_path + images[0] + "\\" + images[0] + "_"
            if len(images[2]) < 2:
                verify_image = verify_image + "000" + images[2] + ".jpg"
            elif len(images[2]) < 3:
                verify_image = verify_image + "00" + images[2] + ".jpg"
            elif len(images[2]) < 4:
                verify_image = verify_image + "0" + images[2] + ".jpg"
            else:
                verify_image = verify_image + images[2] + ".jpg"

        content = compare(image_to_base64(register_image), image_to_base64(verify_image))
        content = str(content)
        content = content.strip('b\'')
        content = json.loads(content)

        if (int(count/300)) % 2 == 0:
            flag = 1
        else:
            flag = 0

        if content['result']['_ret']['reslist']:
            score = content['result']['_ret']['reslist']['name2|name1']
        else:
            score = "-1"

        res_file.write(line + '\t' + score + '\t' + str(flag) + '\n')
        count += 1

    lfw_file.close()
    res_file.close()


def compare_one_by_one():
    url = 'http://apis.baidu.com/idl_baidu/faceverifyservice/face_compare'
    reg = r'{"params": [{"cmdid": "1000", "appid": "bcd24781cd71c7fe421d066e4427cef9", "clientip": "192.168.2.156","type": "st_groupverify", "groupid": "12345", "versionnum": "1.0.0.1", "usernames": {"name1": "name1", "name2": "name2"}, "images": {"name1": "", "name2": ""}, "cates": {"name1":"7", "name2":"7"}}], "jsonrpc": "2.0","method": "Compare"}'
    byte_data = reg.encode(encoding="utf-8")
    req = urllib.request.Request(url, data=byte_data)
    req.add_header("apikey", "bcd24781cd71c7fe421d066e4427cef9")
    resp = urllib.request.urlopen(req)
    content = resp.read()
    if content:
        print(content)


def compare_one_by_one_():
    url = 'http://apis.baidu.com/idl_baidu/faceverifyservice/face_compare'
    data = {}
    data[''] = {"params": [{"cmdid": "1000", "appid": "bcd24781cd71c7fe421d066e4427cef9", "clientip": "192.168.2.156","type": "st_groupverify", "groupid": "12345", "versionnum": "1.0.0.1", "usernames": {"name1": "name1", "name2": "name2"}, "images": {"name1": "fdsfsd", "name2": "f3fwewef"}, "cates": {"name1":"7", "name2":"7"}}], "jsonrpc": "2.0","method": "Compare"}

    decoded_data = urllib.parse.urlencode(data)
    #decoded_data = decoded_data.encode('utf-8')
    decoded_data = str.encode(decoded_data)
    print(decoded_data)
    req = urllib.request.Request(url, data=decoded_data)

    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    req.add_header("apikey", "bcd24781cd71c7fe421d066e4427cef9")
    resp = urllib.request.urlopen(req)
    content = resp.read()
    if content:
        print(content)

compare_test()


