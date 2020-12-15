import random

valid_video_formats = [
    ".3g2", ".3gp", ".3gpp",
    ".asf", ".avi",
    ".dat", ".divx", ".dv",
    ".f4v", ".flv",
    ".gif",
    ".m2ts", ".m4v", ".mkv", ".mod",
    ".mov", ".mp4", ".mpe", ".mpeg",
    ".mpeg4", ".mpg", ".mts",
    ".nsv",
    ".ogm", ".ogv",
    ".qt",
    ".tod", ".ts",
    ".vob",
    ".wmv",
]

for i in range(100):
    fn = "videos/video_"+str(i)+valid_video_formats[random.randint(0, len(valid_video_formats)-1)]
    f = open(fn, "w+")
    f.write("video "+str(i))
    f.close()
