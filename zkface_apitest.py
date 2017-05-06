# coding=utf-8
import requests
import json


def get_face_id(image):
    url = 'http://zkfaceonline.com:8003/face/v0/faceApimatch?detect&db&matchDB=face_matdb_zb'
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': 'LTpLwhpmXA/VhosvNE6RvrPIdwBO6fIqwu+koDS9hBmRO1F+Y1S1mnFuHSTRlkPKBKyCpD',
    }
    data = open(image, "rb").read()
    try:
        res = requests.post(url, headers=headers, data=data)
    except Exception:
        res = requests.post(url, headers=headers, data=data)

    result = res.text.strip('this key has no database[]')
    try:
        result = json.loads(result)
        if len(result) == 1:
            res_dict = result[0]
            if "faceid" in res_dict.keys():
                print(res_dict['faceid'])
                return res_dict['faceid']
            else:
                return '-1'
        else:
            return '-1'
    except Exception:
        return '-1'


def face_compare(image1, image2):
    face1 = get_face_id(image1)
    face2 = get_face_id(image2)
    url = 'http://zkfaceonline.com:8003/face/v0/faceApimatch?match&db&matchDB=face_matdb_zb&faceset1=' + face1 + '&faceset2=' + face2

    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': 'LTpLwhpmXA/VhosvNE6RvrPIdwBO6fIqwu+koDS9hBmRO1F+Y1S1mnFuHSTRlkPKBKyCpD',
    }
    try:
        res = requests.post(url, headers=headers)
    except Exception:
        res = requests.post(url, headers=headers)

    result = res.text.strip('this key has no database[]')
    print(res.text)
    try:
        result = json.loads(result)
        if len(result) == 1:
            res_dict = result[0]
            if 'similarity' in res_dict.keys():
                print(res_dict['similarity'])
                return res_dict['similarity']
            else:
                return -1
        else:
            return -1
    except Exception:
        return -1


def face_compare_test():
    lfw_file = open("pairs_zk.txt")
    res_file = open("res_zk.txt", "a+")
    count = 0
    while 1:
        image_path = "E:/zhangbin/Data/lfw/lfw/lfw/"
        line = lfw_file.readline()
        if not line:
            break
        line = line.strip('\n')
        images = line.split('\t')
        if len(images) > 3:
            register_image = image_path + images[0] + "/" + images[0] + "_"
            if len(images[1]) < 2:
                register_image = register_image + "000" + images[1] + ".jpg"
            elif len(images[1]) < 3:
                register_image = register_image + "00" + images[1] + ".jpg"
            elif len(images[1]) < 4:
                register_image = register_image + "0" + images[1] + ".jpg"
            else:
                register_image = register_image + images[1] + ".jpg"

            verify_image = image_path + images[2] + "/" + images[2] + "_"
            if len(images[3]) < 2:
                verify_image = verify_image + "000" + images[3] + ".jpg"
            elif len(images[3]) < 3:
                verify_image = verify_image + "00" + images[3] + ".jpg"
            elif len(images[3]) < 4:
                verify_image = verify_image + "0" + images[3] + ".jpg"
            else:
                verify_image = verify_image + images[3] + ".jpg"
        else:
            register_image = image_path + images[0] + "/" + images[0] + "_"
            if len(images[1]) < 2:
                register_image = register_image + "000" + images[1] + ".jpg"
            elif len(images[1]) < 3:
                register_image = register_image + "00" + images[1] + ".jpg"
            elif len(images[1]) < 4:
                register_image = register_image + "0" + images[1] + ".jpg"
            else:
                register_image = register_image + images[1] + ".jpg"

            verify_image = image_path + images[0] + "/" + images[0] + "_"
            if len(images[2]) < 2:
                verify_image = verify_image + "000" + images[2] + ".jpg"
            elif len(images[2]) < 3:
                verify_image = verify_image + "00" + images[2] + ".jpg"
            elif len(images[2]) < 4:
                verify_image = verify_image + "0" + images[2] + ".jpg"
            else:
                verify_image = verify_image + images[2] + ".jpg"

        print('\n' + str(count))
        print(register_image)
        print(verify_image)
        score = face_compare(verify_image, register_image)

        if (int(count / 300)) % 2 == 0:
            flag = 1
        else:
            flag = 0

        res_file.write(line + '\t' + str(score) + '\t' + str(flag) + '\n')
        count += 1

    lfw_file.close()
    res_file.close()

face_compare_test()
# detection(open("E:/zhangbin/Data/lfw/lfw/lfw/AJ_Cook/AJ_Cook_0001.jpg", "rb").read())
# create_db()

# curl_test()
# get_face_id("E:/zhangbin/Data/lfw/lfw/lfw/AJ_Cook/AJ_Cook_0001.jpg")
# face_compare("E:/zhangbin/Data/lfw/lfw/lfw/AJ_Cook/AJ_Cook_0001.jpg", "E:/zhangbin/Data/lfw/lfw/lfw/AJ_Cook/AJ_Cook_0001.jpg")
