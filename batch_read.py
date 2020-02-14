import os
import subprocess as sp
import logging

image_file_list=sorted(os.listdir(os.path.dirname(os.path.abspath(__file__))+'/examples/exampleSet/photo'))

image_acceptable_width=str(30000)
batch_size=1
cond=True
RuntimeError_count=0

while cond:
  for _ in range(0,len(image_file_list),batch_size):
      input_image=image_file_list[_:_+batch_size]
      input_image=",".join(input_image)
      print(input_image)
      recog=sp.Popen(['python3','recognize_faces_image_loop_test.py','-e','encoding/encoding3.pickle','-i',input_image,'-r',image_acceptable_width],stdout=sp.PIPE)
      res = recog.communicate()
      for line in res[0].decode(encoding='utf-8').split('\n'):
        print(line)
      
      status=res[0].decode(encoding='utf-8').split('\n')[-3]
      print('recieve : ',status)
      if _==(batch_size*(len(image_file_list)/batch_size)):
        cond=False
      if status=="RuntimeError " or status=="MemoryError ":
        RuntimeError_count+=1
        if RuntimeError_count == 1:
            image_acceptable_width=str(4096)
            recog.kill()
        elif RuntimeError_count == 2:
            image_acceptable_width=str(2560)
            recog.kill()
        elif RuntimeError_count == 3:
            image_acceptable_width=str(1920)
            recog.kill()
        elif RuntimeError_count == 4:
            image_acceptable_width=str(1280)
            recog.kill()
        elif RuntimeError_count == 5:
            image_acceptable_width=str(1024)
            recog.kill()
        elif RuntimeError_count == 6:
            image_acceptable_width=str(960)
            recog.kill()
        elif RuntimeError_count == 7:
            image_acceptable_width=str(800)
            recog.kill()
        elif RuntimeError_count == 8:
            image_acceptable_width=str(640)
            recog.kill()
        elif RuntimeError_count == 9:
            image_acceptable_width=str(480)
            recog.kill()
        elif RuntimeError_count == 10:
            image_acceptable_width=str(320)
            recog.kill()
        else :
            logging.error('please change your device, or check your code\n')
            recog.kill()
            cond=False
        logging.error(f'{status} happened, now image_acceptable_width is {image_acceptable_width}\n')
        break
        