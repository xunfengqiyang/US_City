import os
import sys
import json


def getlocation():
    path = './static/nielsentopo.json'
    content = open(path).read()
    dict = eval(content)
    geometries = dict["objects"]["nielsen_dma"]["geometries"]

    data = {}
    export_str = 'var geoCoordMap = {\n'
    for e in geometries:
        properties = e["properties"]
        longitude = properties["longitude"]
        latitude = properties["latitude"]
        city = properties["dma1"]
        coordinate = '[' + str(longitude) + ',' + str(latitude) + ']'
        data[city] = coordinate;
        export_str = export_str + '\t' + "\"" + city + "\":" + coordinate + "," + '\n'

    export_str = export_str + "}"
    f = open('./export/city.js', 'w')
    f.write(export_str)
    f.close()

    f = open('./export/city.json', 'w')
    f.write(json.dumps(data , ensure_ascii=False , indent=4))
    f.close()


if __name__ == "__main__":
    getlocation()