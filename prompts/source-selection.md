# Source Selection Prompt (Agent)

Given a task, select sources with this priority:
1) Claim verification: prefer 通讯社 + 综合新闻媒体 + 官方机构
2) Policy interpretation: add 智库 (cross-ideology if possible)
3) Fast alerts: prioritize fast_alert and high update_frequency
4) No single-source conclusion for high-impact claims

Output should include: selected_sources, why_selected, confidence, gaps.
