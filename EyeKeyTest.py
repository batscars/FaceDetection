# coding=utf-8
import requests
import json
import time


def get_face_id(image_path):
    data = {
        'app_id': 'app_id',
        'app_key': 'app_key',
        'url': image_path
    }
    try:
        res = requests.post('http://api.eyekey.com/face/Check/checking', data=data)
    except Exception:
        res = requests.post('http://api.eyekey.com/face/Check/checking', data=data)

    result = res.text
    try:
        result = json.loads(result)
        if 'face' in result.keys():
            result = result['face']
            result = result[0]
            if 'face_id' in result.keys():
                return result['face_id']
            else:
                return -1
        else:
            return -1
    except Exception:
        return -1


def compare(image1, image2):
    face1 = get_face_id(image1)
    face2 = get_face_id(image2)
    print(face1)
    print(face2)
    if face1 == -1 or face2 == -1:
        return -1
    data = {
        'app_id': 'app_id',
        'app_key': 'app_key',
        'face_id1': face1,
        'face_id2': face2
    }
    try:
        res = requests.get('http://api.eyekey.com/face/Match/match_compare', params=data)
    except Exception:
        res = requests.get('http://api.eyekey.com/face/Match/match_compare', params=data)

    result = res.text
    result = json.loads(result)
    if 'similarity' in result.keys():
        return result['similarity']
    else:
        return -1


def compare_test():
    lfw_file = open("pairs_eyekey.txt")
    res_file = open("eye0959.txt", "a+")
    count = 0
    while 1:
        image_path = "http://vis-www.cs.umass.edu/lfw/images/"
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

        score = compare(register_image, verify_image)
        if (int(count / 300)) % 2 == 0:
            flag = 1
        else:
            flag = 0
        res_file.write(line + '\t' + str(score) + '\t' + str(flag) + '\n')

        if count % 1000:
            time.sleep(3)
        print(str(count)+'\n')
        count += 1

    lfw_file.close()
    res_file.close()

compare_test()
