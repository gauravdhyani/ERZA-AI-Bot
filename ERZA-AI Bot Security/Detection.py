from tkinter import W
import discord
from discord.ext import commands
from os import path
import time

import numpy as np
import argparse
import cv2 
import sys
client = commands.Bot(command_prefix="+",help_command=None,intents=discord.Intents.all())
client .remove_command('help')
@client.event
async def on_ready():
    print('Logged in ')
@client.command(pass_content=True)    
async def Security(message):
 
  await message.channel.send(":rotating_light: Surveillance Activated :rotating_light:")
  member=message.author.id
  member2=message.author
  if member==504564888576983050 :
   parser = argparse.ArgumentParser(
    description='Script to run MobileNet-SSD object detection network ')
   parser.add_argument("--video", help="path to video file. If empty, camera's stream will be used")
   parser.add_argument("--prototxt", default=r".\ERZA-AI Bot Security\MobileNetSSD_deploy.prototxt",
                                  help='Path to text network file: '
                                       'MobileNetSSD_deploy.prototxt for Caffe model or '
                                       )
   parser.add_argument("--weights", default=r".\ERZA-AI Bot Security\MobileNetSSD_deploy.caffemodel",
                                 help='Path to weights: '
                                      'MobileNetSSD_deploy.caffemodel for Caffe model or '
                                      )
   parser.add_argument("--thr", default=0.6, type=float, help="confidence threshold to filter out weak detections")
   args = parser.parse_args()


# Labels of Network.
   classNames = { 0: 'background',
    1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
    5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
    10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse',
    14: 'motorbike', 15: 'person', 16: 'pottedplant',
    17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor' }

# Open video file or capture device. 
   if args.video:
    cap = cv2.VideoCapture(args.video)
   else:
    cap = cv2.VideoCapture(0)

  #Load the Caffe model 
   net = cv2.dnn.readNetFromCaffe(args.prototxt, args.weights)

   while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame_resized = cv2.resize(frame,(300,300)) # resize frame for prediction

    # MobileNet requires fixed dimensions for input image(s)
    # so we have to ensure that it is resized to 300x300 pixels.
    # set a scale factor to image because network the objects has differents size. 
    # We perform a mean subtraction (127.5, 127.5, 127.5) to normalize the input;
    # after executing this command our "blob" now has the shape:
    # (1, 3, 300, 300)
    blob = cv2.dnn.blobFromImage(frame_resized, 0.007843, (300, 300), (127.5, 127.5, 127.5), False)
    #Set to network the input blob 
    net.setInput(blob)
    #Prediction of network
    detections = net.forward()

    #Size of frame resize (300x300)
    cols = frame_resized.shape[1] 
    rows = frame_resized.shape[0]

    #For get the class and location of object detected, 
    # There is a fix index for class, location and confidence
    # value in @detections array .
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2] #Confidence of prediction 
        if confidence > args.thr: # Filter prediction 
            class_id = int(detections[0, 0, i, 1]) # Class label

            # Object location 
            xLeftBottom = int(detections[0, 0, i, 3] * cols) 
            yLeftBottom = int(detections[0, 0, i, 4] * rows)
            xRightTop   = int(detections[0, 0, i, 5] * cols)
            yRightTop   = int(detections[0, 0, i, 6] * rows)
            
            # Factor for scale to original size of frame
            heightFactor = frame.shape[0]/300.0  
            widthFactor = frame.shape[1]/300.0 
            # Scale object detection to frame
            xLeftBottom = int(widthFactor * xLeftBottom) 
            yLeftBottom = int(heightFactor * yLeftBottom)
            xRightTop   = int(widthFactor * xRightTop)
            yRightTop   = int(heightFactor * yRightTop)
            # Draw location of object  
            cv2.rectangle(frame, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop),
                          (0, 255, 0))

            # Draw label and confidence of prediction in frame resized
            if class_id in classNames:
                label = classNames[class_id] + ": " + str(confidence)
                label2 = classNames[class_id]
                
                labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
                
                yLeftBottom = max(yLeftBottom, labelSize[1])
                cv2.rectangle(frame, (xLeftBottom, yLeftBottom - labelSize[1]),
                                     (xLeftBottom + labelSize[0], yLeftBottom + baseLine),
                                     (255, 255, 255), cv2.FILLED)
                cv2.putText(frame, label, (xLeftBottom, yLeftBottom),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
                        
                if label2=='bicycle'or label2=='bus'or label2=='car'or label2=='motorbike'or label2=='person':
                    cv2.imwrite(".\ERZA-AI Bot Security\Threat.png",frame)
                    final=label2.strip("'}{")
                    Color= 0xFF6500
                    embed=discord.Embed(title='__**Erza Surveillance**__',description='__**Powered by Vanguard**__',color=Color)
                    embed.set_thumbnail(url=f'https://cdn.discordapp.com/attachments/933791569398628442/944551379073105961/1200px-VanguardInfo.jpg')
                    embed.add_field(name=f'**Security Alert**', value=f'Vanguard detected a {final}.')
                    file = discord.File(r".\ERZA-AI Bot Security\Threat.png", filename="Threat.png")
                    embed.set_image(url="attachment://Threat.png")
                    time.sleep(5)
                    await message.send(file=file,embed=embed)   
                 
    
    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
    cv2.imshow("frame", frame)
    if cv2.waitKey(5) >= 0:   
        break 
  else:
    await message.channel.send(f'{member2.mention}Not authorized')     
 
  
@client.command(pass_content=True)    
async def Stop(message):
    sys.exit({message})
client.run('Enter your token here')