from json import loads
with open("parsed.json", "r") as f:
    cones = loads(f.read())
    with open("reparsed.csv", "w") as fNew:
        fNew.write("classId,classTitle,pixWidth,pixHeight,normWidth,normHeight,normCenterX,normCenterY\n")
        for cone in cones:
            fNew.write(",".join(map(lambda el: str(el), [cone["classId"],
                                                        cone["classTitle"],
                                                        cone["pixWidth"],
                                                        cone["pixHeight"],
                                                        cone["normWidth"],
                                                        cone["normHeight"],
                                                        cone["normCenterX"],
                                                        cone["normCenterY"]])) + "\n")