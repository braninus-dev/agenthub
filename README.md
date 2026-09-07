# AgentHub: Dujiangyan Harness Engineering Engine 🌊
> **The World's First Bio-Inspired Multi-Agent Harness Architecture Rooted in 2,200-Year-Old Ancient Hydraulic Engineering.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Architecture: Harness](https://img.shields.io/badge/Architecture-Harness%20Engineering-green.svg)](#architecture)

[中文文档 (Chinese)](./README_CN.md) | [English Documentation](./README.md)

---

## 🌊 The Core Philosophy: "Agent - LLM = Harness"

In 256 BC, Chinese engineer Li Bing constructed the **Dujiangyan Irrigation System**. Instead of building a massive, rigid dam to block the raging Minjiang River, he designed a fluid, self-governing hydraulic harness that utilized gravity, centrifugal force, and natural river bends. It turned annual deadly floods into the eternal agricultural paradise of the Chengdu Plain.

Modern LLMs are just like the unconstrained Minjiang River: **infinite kinetic energy, high entropy, and prone to flooding (context rot, runaway loops, hallucination, out-of-memory crashes).**

Most multi-agent frameworks today are built like brittle dams (rigid DAGs, brittle state machines). When the model hallucinates, the dam bursts.

**AgentHub implements the 4 Pillars of Dujiangyan Harness Engineering:**

```
                  [Raw LLM Kinetic Energy: Unconstrained Stream]
                                        │
                                        ▼
             ┌─────────────────────────────────────────────────────┐
             │    1. Fishmouth (鱼嘴): Task Impedance Routing       │
             │   Low-impedance crunching ──▶ ZCode (Free High-Flow)│
             │   High-impedance strategy ──▶ Hermes / Sol High     │
             └──────────────────────────┬──────────────────────────┘
                                        │
             ┌──────────────────────────┴──────────────────────────┐
             │    2. Baopingkou (宝瓶口): Information Choke Point    │
             │   Forces turbulent logs into 3-field laminar flow   │
             │   { status, artifact, summary }                     │
             └──────────────────────────┬──────────────────────────┘
                                        │
             ┌──────────────────────────┴──────────────────────────┐
             │    3. Feishayan (飞沙堰): Centrifugal Desilting      │
             │   Reality Anchors (Exit 0 + Non-empty artifact)     │
             │   80% noise/hallucination discarded automatically   │
             └──────────────────────────┬──────────────────────────┘
                                        │
                                        ▼
                   4. Sui Xiu (岁修): Self-Evolution & Dredging
                   Weekly cache purging & skill half-life pruning
```

---

## 🚀 Key Features

- **⚡ Zero-Crash Architecture**: Background watchdogs automatically sever orphaned or runaway processes before host memory is exhausted.
- **🛡️ Anti-Context Rot**: The **Baopingkou Choke** compresses noisy subagent execution outputs into clean, structured reality packets.
- **💎 Reality Anchors**: Subagents cannot self-report completion without verifiable physical artifacts on disk and clean compilation (`Exit 0`).
- **✨ Biomorphic HUD 2.0**: Real-time 2D Canvas rendering Bezier particle light trails connecting the orchestrator and worker agents with shockwave impacts.

---

## 🛠️ Quick Start

```bash
# Clone the repository
git clone https://github.com/your-username/agenthub.git
cd agenthub

# Test the Dujiangyan Harness Engine
python3 skill/dujiangyan_harness.py test
```

### Output:
```text
🧪 Testing Dujiangyan Harness Engine Components...
1. Fishmouth Routing ──▶ Target: ZCode (Low impedance detected)
2. Baopingkou Choke  ──▶ Laminar Packet: {'status': 'SUCCESS', 'artifact': '...', 'summary': '...'}
3. Feishayan Anchor  ──▶ Status: PASSED (Physical file exists > 0 bytes)
4. Sui Xiu Dredging  ──▶ Cleaned 4 stale items
✅ All 4 Harness components verified!
```

---

## 📜 License
MIT License. Built for autonomous self-improving single-person enterprises.
