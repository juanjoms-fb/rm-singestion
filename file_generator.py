import random
import constants


for i in range(100):
    fn = "videos/video_"+str(i)+constants.VALID_VIDEO_FORMATS[random.randint(0, len(constants.VALID_VIDEO_FORMATS)-1)]
    f = open(fn, "w+")
    f.write("video "+str(i))
    f.close()
