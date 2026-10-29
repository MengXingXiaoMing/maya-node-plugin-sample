# maya-node-plugin-sample

示例 Maya 节点插件，用来演示 [Maya 节点插件市场](https://github.com/MengXingXiaoMing/maya-node-plugin-market)
的收录流程。它本身只注册一个空节点，没有实际功能。

## 它演示了什么

- 插件代码放在**作者自己的公开仓库**里（不在索引仓库里）
- 入口文件里有 `NODE_INFO`，写明节点序号、节点名、版本、作者、标签
- 索引仓库里只需要一个 `plugins/0x001414BF.json` 元数据条目指向这里

## 对应的市场条目

```json
{
  "name": "示例：最小节点插件",
  "description": "只注册一个空节点，用来演示插件市场的节点格式、条目写法与自动合并流程。",
  "author": "詹康明",
  "version": "1.1.0",
  "node_id": "0x001414BF",
  "node_name": "marketSampleNode",
  "category": "utility",
  "tags": ["示例", "模板"],
  "repo": "MengXingXiaoMing/maya-node-plugin-sample",
  "subpath": "",
  "entry": "sample_node.py",
  "branch": "main",
  "run": "cmds.createNode('marketSampleNode')",
  "maya_versions": ["2022", "2023", "2024", "2025", "2026"],
  "added": "2026-10-29"
}
```

## 自己写插件时要改的地方

1. `NODE_INFO` 里的 `node_id` 换成你自己申请的节点序号（[Maya 节点序号申请](https://www.autodesk.com/sign-in?redirect_url=https%3A%2F%2Fapps.autodesk.com%2Fdevelop%2Fnodeidregistration%2F)）
2. `node`、`version`、`name` 和条目 JSON 里的 `node_name`、`version`、`name` 保持一致
3. 把条目文件提交到 [maya-node-plugin-index](https://github.com/MengXingXiaoMing/maya-node-plugin-index) 的 `plugins/<node_id>.json`
