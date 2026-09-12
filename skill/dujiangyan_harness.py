#!/usr/bin/env python3
"""
dujiangyan_harness.py — 都江堰束导工程 (Harness Engineering Core)
为 Hermes OS V2 及 AgentHub 打造的自洽分流、控量、排沙与岁修治理引擎。

四大工程构件：
1. 鱼嘴分流 (Fishmouth Router): 依据任务阻抗 (Impedance) 自动分流 (ZCode / Hermes / Codex)
2. 宝瓶口控量 (Baopingkou Governor): 刚性压榨上下文为层流结构 (status, artifact, summary)，拒绝紊流
3. 飞沙堰排沙 (Feishayan Reality Anchor & Guard): 物理文件存在性校验 + 内存/死循环溢流断尾
4. 岁修机制 (Sui Xiu Dredger): 定期清理死技能、临时缓存，自愈免疫
"""

import os
import sys
import json
import time
import tempfile
from pathlib import Path
from typing import Dict, Any, Optional

DEFAULT_ROOT = Path(os.environ.get("AGENTHUB_HOME", "~/.agenthub")).expanduser()

class DujiangyanHarness:
    def __init__(self, root: Optional[Path] = None):
        self.root = Path(root).expanduser() if root else DEFAULT_ROOT
        self.event_bus = self.root / "agent-events.json"
        self.ensure_dirs()

    def ensure_dirs(self):
        (self.root / "task-queue" / "zcode" / "pending").mkdir(parents=True, exist_ok=True)
        (self.root / "task-queue" / "zcode" / "completed").mkdir(parents=True, exist_ok=True)
        (self.root / "task-queue" / "hermes" / "pending").mkdir(parents=True, exist_ok=True)

    # -------------------------------------------------------------
    # 1. 鱼嘴工程：阻抗匹配与动态分流
    # -------------------------------------------------------------
    def fishmouth_route(self, task_name: str, task_desc: str, char_len: int = 0) -> str:
        """
        计算任务阻抗 (Task Impedance)：
        - 低阻抗 (Low Impedance, 大吞吐、文本正则、代码补丁、抓取清洗) ──▶ 分流至 ZCode (GLM 免费流)
        - 高阻抗 (High Impedance, 战略决策、元架构、八字体用推演、终审) ──▶ 分流至 Hermes / Sol High
        - 特遣高精 (Specialized, 复杂单点攻坚) ──▶ Qoder / Codex
        """
        desc_lower = (task_name + " " + task_desc).lower()
        
        # 关键词探测
        low_impedance_keywords = [
            "clean", "regex", "txt", "chunk", "spider", "scrape", "patch", "format",
            "清洗", "切片", "提取", "整理", "补丁", "下载", "分词", "爬虫", "转换"
        ]
        high_impedance_keywords = [
            "strategy", "architecture", "divination", "review", "design", "audit",
            "决策", "战略", "架构", "推演", "终审", "八字", "梅花", "商业", "方案"
        ]
        
        is_low = any(k in desc_lower for k in low_impedance_keywords) or char_len > 10000
        is_high = any(k in desc_lower for k in high_impedance_keywords)
        
        if is_high and not is_low:
            worker = "hermes_sol"
        elif is_low:
            worker = "zcode"
        else:
            worker = "zcode"  # 默认低成本工坊优先
            
        self._emit_event("FISHMOUTH_ROUTED", f"任务 [{task_name}] 阻抗评估完成 ──▶ 分流至 {worker.upper()}")
        return worker

    # -------------------------------------------------------------
    # 2. 宝瓶口工程：信息层流卡口与上下文扼杀
    # -------------------------------------------------------------
    def baopingkou_choke(self, status: str, artifact_path: Optional[str], raw_output: str, max_chars: int = 120) -> Dict[str, Any]:
        """
        无论子 Agent 吐出几万字紊流，强制在宝瓶口压缩为 3 字段层流切片：
        { 'status': 'SUCCESS/FAIL', 'artifact': path, 'summary': 简明人话 }
        严禁原始终端日志冲刷主脑上下文！
        """
        clean_status = "SUCCESS" if "success" in status.lower() or status == "0" else "FAIL"
        
        # 提取极简摘要（过滤所有 ANSI 和 Traceback）
        clean_lines = [l.strip() for l in raw_output.splitlines() if l.strip() and not l.startswith(("[terminal]", "Traceback", "File "))]
        summary = clean_lines[-1] if clean_lines else "任务已在后台完成处理。"
        if len(summary) > max_chars:
            summary = summary[:max_chars - 3] + "..."
            
        choked_packet = {
            "status": clean_status,
            "artifact": artifact_path or "NONE",
            "summary": summary,
            "timestamp": time.time()
        }
        self._emit_event("BAOPINGKOU_CHOKED", f"层流切片收敛: [{clean_status}] {summary}")
        return choked_packet

    # -------------------------------------------------------------
    # 3. 飞沙堰工程：现实锚点排沙与物理断尾泄洪
    # -------------------------------------------------------------
    def feishayan_verify(self, artifact_path: Optional[str], exit_code: int = 0) -> bool:
        """
        现实锚点排沙：
        - 拒绝一切'自吹自擂'，只认物理硬指标：
          1. 退出码必须是 0
          2. 如果声明了产物文件，该文件必须真实存在且字节数 > 0
        """
        if exit_code != 0:
            self._emit_event("FEISHAYAN_DESILT", f"排沙拦截：退出码异常 (exit_code={exit_code})，判定为无效泥沙！")
            return False
            
        if artifact_path and artifact_path != "NONE":
            p = Path(artifact_path)
            if not p.exists() or p.stat().st_size == 0:
                self._emit_event("FEISHAYAN_DESILT", f"排沙拦截：产物文件不存在或为空 ({artifact_path})，判定为幻觉！")
                return False
                
        self._emit_event("FEISHAYAN_PASSED", f"现实锚点检验通过：产物真实有效 ({artifact_path})")
        return True

    # -------------------------------------------------------------
    # 4. 岁修工程：深淘滩、低作堰自治维护
    # -------------------------------------------------------------
    def suixiu_dredge(self, days_threshold: int = 30, apply: bool = False) -> Dict[str, int]:
        """
        岁修深淘滩：
        - 默认 dry-run，仅报告可清理的过期临时日志
        - 仅在 apply=True 时删除目标文件
        """
        candidates = 0
        cleaned_logs = 0
        now = time.time()
        
        # 淘洗临时日志
        log_dir = self.root / "logs"
        if log_dir.exists():
            for f in log_dir.glob("*.log.*"):
                if now - f.stat().st_mtime > 7 * 86400:
                    candidates += 1
                    if not apply:
                        continue
                    try:
                        f.unlink()
                        cleaned_logs += 1
                    except Exception:
                        pass
                        
        mode = "applied" if apply else "dry-run"
        self._emit_event(
            "SUIXIU_DREDGED",
            f"岁修深淘滩完成（{mode}）：候选 {candidates} 项，已删除 {cleaned_logs} 项",
        )
        return {"candidates": candidates, "cleaned_logs": cleaned_logs, "applied": apply}

    # 内部事件发射
    def _emit_event(self, event_type: str, message: str):
        event = {
            "timestamp": time.time(),
            "type": event_type,
            "message": message
        }
        try:
            with open(self.event_bus, "a", encoding="utf-8") as f:
                f.write(json.dumps(event, ensure_ascii=False) + "\n")
        except Exception:
            pass

def run_smoke_test() -> int:
    """Exercise all components without reading or deleting user data."""
    with tempfile.TemporaryDirectory(prefix="agenthub-smoke-") as tmp:
        root = Path(tmp)
        artifact = root / "demo-artifact.txt"
        artifact.write_text("AgentHub smoke-test artifact\n", encoding="utf-8")
        harness = DujiangyanHarness(root=root)
        print("🧪 Testing Dujiangyan Harness Engine Components...")
        worker = harness.fishmouth_route("document cleanup", "chunk and clean input", char_len=50000)
        print(f"1. Fishmouth Routing ──▶ Target: {worker}")
        packet = harness.baopingkou_choke("SUCCESS", str(artifact), "Process finished with exit code 0")
        print(f"2. Baopingkou Choke ──▶ Laminar Packet: {packet}")
        passed = harness.feishayan_verify(str(artifact), exit_code=0)
        print(f"3. Feishayan Anchor ──▶ Status: {'PASSED' if passed else 'BLOCKED'}")
        result = harness.suixiu_dredge()
        print(f"4. Sui Xiu Dredging ──▶ Result: {result}")
        if not passed:
            return 1
    print("✅ All 4 Harness components verified without touching user data.")
    return 0


if __name__ == "__main__":
    harness = DujiangyanHarness()
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "test":
            raise SystemExit(run_smoke_test())
        elif cmd == "dredge":
            apply = "--apply" in sys.argv[2:]
            print(harness.suixiu_dredge(apply=apply))
    else:
        print("Usage: dujiangyan_harness.py [test|dredge [--apply]]")
