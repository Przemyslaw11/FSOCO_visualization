import glob 
import json
import os
from pathlib import Path
from json import dumps 
from tqdm import tqdm

classIdMapper = {9993505:0,
                 9993514:1, 
                 9993506:2, 
                 9993507:3,
                 9993508:4,
                 9993509:5,
                 9993510:6,
                 9993511:7,
                 9993512:8,
                 9993513:9}
cones = []
for annPath in tqdm(Path("./").rglob("./*/*.json")):
    with open(annPath, "r", encoding="utf8") as ann:
        annData = json.loads(ann.read())
        imgHeight = annData["size"]["height"]
        imgWidth = annData["size"]["width"]
        for obj in annData["objects"]:
            classId = str(classIdMapper[int(obj["classId"])])
            points = obj["points"]["exterior"]
            p1 = points[1]
            p0 = points[0] 
            objWidth = p1[0] - p0[0]
            objHeight = p1[1] - p0[1]

            objCenterXNorm = (p0[0] + (objWidth/2) )/imgWidth
            objCenterYNorm = (p0[1] + (objHeight/2) )/imgHeight
            objWidthNorm = objWidth / imgWidth
            objHeightNorm = objHeight / imgHeight
            
            cones.append({
                "classId": obj["classId"],
                "classTitle": obj["classTitle"],
                "pixWidth": objWidth,
                "pixHeight": objHeight,
                "normWidth": objWidthNorm,
                "normHeight": objHeightNorm,
                "normCenterX": objCenterXNorm,
                "normCenterY": objCenterYNorm,
                "imgAreaCovered": (objWidth*objHeight)/(imgHeight*imgWidth)
            })

with open("parsed.json", "w") as f:
    f.write(dumps(cones))