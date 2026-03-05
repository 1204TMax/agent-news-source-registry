# agent-news-source-registry

中文 | English

---

## 中文说明

这是一个**给 Agent 使用的新闻源注册库（registry）**，用于结构化管理新闻网站来源，方便检索、筛选、交叉验证与任务编排。

### 致谢与来源说明（重要）

本项目中的新闻网站来源清单，**来源于并整理自**以下聚合项目：

- World Monitor: <https://www.worldmonitor.app>
- World Monitor GitHub: <https://github.com/koala73/worldmonitor>

感谢原项目提供的聚合与整理基础。  
本仓库仅做二次结构化整理，便于 Agent 读取与查询。

### 项目用途

- 面向 Agent 的结构化数据源（JSONL/JSON）
- 支持按标签、主题、区域、可靠性等维度筛选
- 支持在工作流中进行来源选择与交叉验证

### 非目标（请注意）

- **本项目不提供任何 API 服务**
- **本项目不提供 MCP 服务**
- 本项目是数据与规则仓库，不是在线服务端

### 目录结构

- `data/sources.jsonl`：主数据（每行一个 source）
- `schemas/source.schema.json`：字段与结构约束
- `tags/taxonomy.yaml`：标签体系
- `prompts/source-selection.md`：Agent 选源提示词模板
- `policies/source-trust-policy.md`：来源信任与冲突处理规则
- `scripts/validate.py`：数据校验脚本
- `scripts/build.py`：导出构建脚本
- `exports/`：面向人类阅读的导出文件

### 快速使用

```bash
python3 scripts/validate.py
python3 scripts/build.py
```

---

## English

This is an **agent-first news source registry** for structured source management, designed for retrieval, filtering, cross-checking, and workflow orchestration.

### Attribution & Upstream Source (Important)

The news website/source list in this repository is **derived from and organized based on** the following upstream aggregation project:

- World Monitor: <https://www.worldmonitor.app>
- World Monitor GitHub: <https://github.com/koala73/worldmonitor>

Huge thanks to the upstream project for the aggregation foundation.  
This repository only restructures that source list for agent-readable/queryable workflows.

### What this repository is for

- Structured datasets for agent consumption (JSONL/JSON)
- Filtering by tags, topics, regions, and reliability signals
- Source selection and multi-source verification in agent workflows

### Non-goals (Important)

- **This project does NOT provide any API**
- **This project does NOT provide any MCP service**
- This is a data/rules repository, not an online backend service

### Layout

- `data/sources.jsonl`: canonical dataset (one source per line)
- `schemas/source.schema.json`: schema constraints
- `tags/taxonomy.yaml`: tag taxonomy
- `prompts/source-selection.md`: source-selection prompt template for agents
- `policies/source-trust-policy.md`: trust/conflict policy
- `scripts/validate.py`: validation script
- `scripts/build.py`: build/export script
- `exports/`: human-readable exports

### Quickstart

```bash
python3 scripts/validate.py
python3 scripts/build.py
```
