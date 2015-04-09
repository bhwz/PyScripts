from os import listdir, getcwd
from subprocess import call

for flcFile in listdir(getcwd()):
    if flcFile.endswith(".flac"):
        print(flcFile)
        flcName = flcFile[:-4]
        ffmpegArgs = " -i \"{0}\" -acodec alac \"{1}\".m4a".format(flcFile, flcName)
        call("ffmpeg" + ffmpegArgs, shell=True)
        continue
    else:
        continue
