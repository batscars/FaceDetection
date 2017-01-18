import urllib
import urllib.request
import urllib.parse
import json


def compare(image1, image2):
    url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
    data = {
        'api_key': 'GqD1BoiXToRdJHMR2zPRVOM0_v3PYmFd',
        'api_secret': '95OTXBAOGIHd14PLRZDgZEN2gU9Wvsx9',
        'image_url1': image1,
        'image_url2': image2
    }
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data=data)

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


def compare_test():
    lfw_file = open("pairs_face.txt")
    res_file = open("res_face.txt", "a+")
    for i in range(0, 4989):
        lfw_file.readline()
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

        content = compare(register_image, verify_image)
        content = str(content)
        content = content.strip('b\'')
        content = json.loads(content)

        if (int(count / 300)) % 2 == 0:
            flag = 1
        else:
            flag = 0

        if 'confidence' in content.keys():
            score = content['confidence']
        else:
            score = '-1'
        res_file.write(line + '\t' + str(score) + '\t' + str(flag) + '\n')

        count += 1

    lfw_file.close()
    res_file.close()
compare_test()
