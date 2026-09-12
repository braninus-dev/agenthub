#!/usr/bin/env python3
import json
import time
import os
import sys

AGENTHUB_HOME = os.path.expanduser(os.environ.get("AGENTHUB_HOME", "~/.agenthub"))
EVENTS_FILE = os.path.join(AGENTHUB_HOME, "agent-events.json")
METRICS_FILE = os.path.join(AGENTHUB_HOME, "agent-metrics-live.json")

def emit_event(event_type, from_agent, to_agent, task_name, status="RUNNING", detail=""):
    event = {
        "event_id": f"evt_{int(time.time()*1000)}",
        "event_type": event_type,
        "from_agent": from_agent,
        "to_agent": to_agent,
        "task_name": task_name,
        "status": status,
        "timestamp": time.time(),
        "detail": detail
    }
    os.makedirs(AGENTHUB_HOME, exist_ok=True)
    temp_file = f"{EVENTS_FILE}.tmp"
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(event, f, indent=2)
    os.replace(temp_file, EVENTS_FILE)
    print(f"📡 [Event Emitted] {event_type}: {from_agent} ──▶ {to_agent} ({task_name})")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: dispatch_event.py <EVENT_TYPE> <FROM> <TO> <TASK_NAME> [STATUS]")
        sys.exit(1)
    ev_type = sys.argv[1]
    f_agent = sys.argv[2]
    t_agent = sys.argv[3]
    t_name = sys.argv[4]
    st = sys.argv[5] if len(sys.argv) > 5 else "RUNNING"
    emit_event(ev_type, f_agent, t_agent, t_name, status=st)
