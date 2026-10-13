# learn-10x：10 倍速学习 Skill

**让 AI 带你真正学会：先规划，再练习，用作答和成果检查理解。**

把六种学习方法变成可执行的学习流程。适配 Claude Code、Codex 和支持 Agent Skills 的工具；既能只用一个 `SKILL.md`，也能把整个仓库作为插件使用。

## 六种方法

| 方法 | 帮你做什么 |
| --- | --- |
| 学习阶梯 | 从入门到进阶，标明先修关系和阶段验收 |
| 20 小时核心筛选 | 按实际预算筛重点，安排练习、产物与复盘 |
| AI 实时考官 | 每次一题，回答后纠错，再检查能否独立应用 |
| 一页速查表 | 把已学内容压缩成可回看的复习提纲 |
| 前置资源过滤 | 选少量适配资料，说明选择依据与核验状态 |
| 费曼学习循环 | 简单解释、自己复述、补漏洞、换情境应用 |

完整流程：**成果目标 → 学习地图 → 核心与资源 → 练习 → 自测 / 复述 → 速查与复习**。也可以只调用其中一个方法。

默认 20 小时分成 10 个两小时单元，每单元最后 15 分钟复盘；规划、筛资料与自测也计入预算。时间更少，就缩小目标。“10 倍”是名称与灵感表达，本项目没有验证固定提速倍数，也不承诺 20 小时精通任何领域。

## 单文件使用

创建 `learn-10x` 文件夹，把根目录的 [SKILL.md](SKILL.md) 放进去即可。核心使用不需要脚本、API key 或额外依赖。

| 工具 | 个人使用 | 仅当前项目 |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/learn-10x/SKILL.md` | `<项目>/.claude/skills/learn-10x/SKILL.md` |
| Codex | `~/.agents/skills/learn-10x/SKILL.md` | `<项目>/.agents/skills/learn-10x/SKILL.md` |

Windows 的 `~` 表示用户目录，例如 `%USERPROFILE%\.agents\skills\learn-10x\`。选一个位置安装；Codex 未显示新技能时重启。

Claude Code：

```text
/learn-10x 我想学习摄影，每周有3小时，目标是拍出曝光稳定的人像。
```

Codex：

```text
使用 $learn-10x。我从零学习 Python，想用20小时学会整理 Excel 文件。
先给我学习路线和单元安排，再带我完成当前单元。
```

还可以说：“考考我 HTTP 缓存，每次一题”“检查我的概念复述”“先暂停，给我学习检查点”。普通聊天也可以粘贴 [六套完整提示词](references/methods.md)。

想保留可选提示词与 Codex 界面信息，可以把 `skills/learn-10x/` 整个目录复制到上表中的技能目录。完整使用示例见 [20 小时 Python / Excel 学习案例](examples/python-excel.md)。

<details>
<summary>整个仓库作为插件使用（Claude Code / Codex）</summary>

可以先通过本地目录测试，也可以从 GitHub 市场安装。插件安装会在所选工具中注册市场并启用技能，请自行选择一种方式，避免重复安装。

### Claude Code

在仓库根目录本地预览：

```sh
claude --plugin-dir .
```

通过仓库内的市场安装：

```text
/plugin marketplace add ArthurCodings/learn-10x
/plugin install learn-10x@learn-10x
/learn-10x:learn-10x 我想学习 Python，先帮我规划学习路线。
```

插件通过 `.claude-plugin/plugin.json` 直接读取根目录 `SKILL.md`，插件调用名是 `/learn-10x:learn-10x`。单文件安装的调用名仍是 `/learn-10x`。

### Codex

在仓库根目录，通过本地市场安装：

```sh
codex plugin marketplace add .
codex plugin add learn-10x@learn-10x
```

通过 GitHub 市场安装：

```sh
codex plugin marketplace add ArthurCodings/learn-10x --ref main
codex plugin add learn-10x@learn-10x
```

在会话中使用 `$learn-10x`，或通过 `/skills` 选择。Codex 封装使用仍受支持的 `.codex-plugin/plugin.json` 兼容格式，从 `skills/learn-10x/` 读取技能；市场入口为 `.agents/plugins/marketplace.json`。

其他市场也可以收录这个仓库：Claude 按其市场格式添加 GitHub 来源，Codex 按其市场格式添加仓库来源。不需要复制一套新的技能内容；提交到官方市场仍需遵循该市场的审核要求。

清单与安装方式依据 [Claude 插件规范](https://code.claude.com/docs/en/plugins-reference)、[Claude 市场规范](https://code.claude.com/docs/en/plugins/marketplace-reference)、[Codex 插件规范](https://developers.openai.com/plugins/build/plugins) 和 [Codex 技能文档](https://learn.chatgpt.com/docs/build-skills)，于 2026-10-13 核对。

</details>

<details>
<summary>目录与维护方式</summary>

```text
learn-10x/
├── README.md
├── SKILL.md                       # 技能维护源；可以单独使用
├── references/methods.md           # 可选：六套完整提示词
├── examples/python-excel.md        # 可选：贯穿学习案例
├── agents/openai.yaml              # 可选：Codex 界面信息
├── .claude-plugin/
│   ├── plugin.json                 # Claude 插件
│   └── marketplace.json            # Claude 市场
├── .codex-plugin/plugin.json        # Codex 插件
├── .agents/plugins/marketplace.json # Codex 市场
├── scripts/sync_skill.py            # 维护时生成 / 检查插件副本
└── skills/learn-10x/                # 自动生成；供插件和完整技能安装
    ├── SKILL.md
    ├── references/methods.md
    └── agents/openai.yaml
```

只编辑根目录 `SKILL.md`、`references/` 和 `agents/`。然后用 Python 3.9 或以上同步插件副本：

```sh
python scripts/sync_skill.py
python scripts/sync_skill.py --check
```

`--check` 只检查一致性，不改文件。脚本不会提交、安装或注册插件。技能运行不需要执行它；提交到市场时要保留已经生成的 `skills/learn-10x/`。

不增加 `CLAUDE.md`、`AGENTS.md`、MCP 服务或 hooks：当前功能都由技能指令完成，插件清单负责发现这些指令。

</details>

## 灵感

六个方法来自用户提供、标注为 WaytoAGI《如何用 Claude 以 10 倍速度学习任何东西》的文案，[原视频链接](https://v.douyin.com/hwiWoDWZ-nU/)。本项目在此基础上重新编写执行指令，补充时间预算、先修保护、可验证的自测、循环退出、学习检查点与后续复习。
