#!/usr/bin/env python
# The decompiled C# code this file copies parts from is owned by
#   https://x.com/eggHatcherGame And is unfortunately used here
#   without permission.
import io
from .binarydotnet import BinaryReader
def decode(stream:io.BufferedIOBase) -> dict:
    br = BinaryReader(stream)
    output = {}

    output['soloChats'] = []
    for i in range(br.read_int32()):
        br.read_string()
        output['soloChats'].append(dict(
            name = br.read_string(),
            icon = br.read_string(),
            voice = br.read_string(),
            jpVoice = br.read_string(),
            content = br.read_string(),
        ))

    output['showLines'] = []
    for i in range(br.read_int32()):
        br.read_string()
        output['showLines'].append(dict(
            content = br.read_string(),
            voice = br.read_string(),
            jpVoice = br.read_string(),
        ))

    output['tutorials'] = []
    for i in range(br.read_int32()):
        output['tutorials'].append(dict(
            index = br.read_string(),
            type = br.read_string(),
            chName = br.read_string(),
            imgs = br.read_string(),
            des = [br.read_string(), br.read_string()],
        ))

    output['challengeLogs'] = []
    for i in range(br.read_int32()):
        output['challengeLogs'].append(dict(
            challengeType = br.read_string(),
            battleType = br.read_string(),
            self = br.read_string(),
            des = br.read_string(),
        ))

    output['paintEvaluations'] = []
    for i in range(br.read_int32()):
        output['paintEvaluations'].append(dict(
            type = br.read_string(),
            chara = br.read_string(),
            level = br.read_string(),
            des = br.read_string(),
        ))
    return output
