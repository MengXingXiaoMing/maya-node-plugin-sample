# -*- coding: utf-8 -*-
"""示例节点：演示 Maya 节点插件市场条目的最小写法。

这个文件只注册一个空节点，没有任何实际功能，用来示范：
- NODE_INFO 里写什么（市场卡片和在线条目都读它）；
- 节点怎么注册（registerNode / MTypeId）；
- 条目里的 node_id / node / version 必须和这里完全一致，否则自动校验会拒绝。
"""

NODE_INFO = {
    "name": "示例：最小节点插件",
    "description": "只注册一个空节点，用来演示插件市场的节点格式、条目写法与自动合并流程。",
    "author": "詹康明",
    "version": "1.0.0",
    "node": "marketSampleNode",
    "node_id": "0x00A10B01",
    "run": "cmds.createNode('marketSampleNode')",
    "tags": ["示例", "模板"],
    "github": "https://github.com/MengXingXiaoMing/maya-node-plugin-sample",
}

import maya.api.OpenMaya as om


def maya_useNewAPI():
    pass


NODE_ID = om.MTypeId(int(NODE_INFO["node_id"], 16))


class SampleNode(om.MPxNode):
    TYPE_NAME = NODE_INFO["node"]

    def __init__(self):
        om.MPxNode.__init__(self)


def nodeCreator():
    return SampleNode()


def initialize():
    pass


def initializePlugin(plugin):
    om.MFnPlugin(plugin, NODE_INFO["author"], NODE_INFO["version"]).registerNode(
        SampleNode.TYPE_NAME, NODE_ID, nodeCreator, initialize)


def uninitializePlugin(plugin):
    om.MFnPlugin(plugin).deregisterNode(NODE_ID)
