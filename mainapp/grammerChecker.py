import requests
import json

def getRequest(text):
    response = requests.post('http://164.125.7.61/speller/results', data={'text1': text})
    print("*************",response.text,"*********")
    if "기술적 한계로 찾지 못한 맞춤법 오류나 문법 오류가 있을 수 있습니다." in response.text or not "data = [" in response.text:
        return []
    data = response.text.split('data = [', 1)[-1].rsplit('];', 1)[0]
    data = list(map(lambda v: {'orgStr':v['orgStr'], 'candWord':v['candWord'].split('|')[0], 'start':v['start'], 'end':v['end'], 'help':v['help']} , json.loads(data)['errInfo']))
    return data

def compareWithOrg(orgText, errData):
    isErr = []
    orgTextList = []
    candTextList = []
    index = 0

    for d in errData:
        if d['start'] != 0:
            candTextList.append(orgText[index:d['start']])
            orgTextList.append(orgText[index:d['start']])
            isErr.append(False)
        candTextList.append(d['candWord'])
        orgTextList.append(d['orgStr'])
        isErr.append(True)
        index = d['end']+1
    if index <= len(orgText):
        candTextList.append(orgText[index:])
        orgTextList.append(orgText[index:])
        isErr.append(False)

    return {
        'isErr': isErr,
        'orgTextList': orgTextList,
        'candTextList': candTextList
    }

def checkGrammer(orgText):
    errData = sorted(getRequest(orgText), key=lambda a: a["start"])
    data = compareWithOrg(orgText, errData)
    print("*************",data,"*********")
    return data