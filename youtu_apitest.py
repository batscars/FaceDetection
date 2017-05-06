import TencentYoutuyun

appid = '10010533'
secret_id = 'AKIDlV5EYxlaiHwdPI8f7a7X9kjkoyDPCPrF'
secret_key = 'XOMMSLMQYes3JevIe9Wiz74ThkcJ4h9R'
userid = 'zhangbin'
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT
youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)


def compare_test():
    lfw_file = open("pairs_youtu.txt")
    res_file = open("youtu1727.txt", "a+")
    error_code = open("error_code.txt", "a+")
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

        content = youtu.FaceCompare(register_image, verify_image)
        error_code.write(str(content['errormsg']) + '\n')
        if content['errorcode'] != 0:
            score = -1
        else:
            score = content['similarity']

        print(str(count))
        print(register_image)
        print(verify_image)
        print(str(score) + '\n')

        if (int(count / 300)) % 2 == 0:
            flag = 1
        else:
            flag = 0

        res_file.write(line + '\t' + str(score) + '\t' + str(flag) + '\n')
        count += 1

    lfw_file.close()
    res_file.close()
    error_code.close()

compare_test()