# Universal Agent Protocol (UAP) Specification

## 1. Event Bus Schema (~/.hermes/agent-events.json)
Whenever an orchestrator or worker changes state, emit an atomic JSON record:
```json
{
  "event_id": "evt_1788743900",
  "event_type": "TASK_DISPATCH | TASK_PROGRESS | TASK_DONE | OVERLOAD_ALERT",
  "from_agent": "hermes | codex | zcode | workbuddy",
  "to_agent": "zcode | workbuddy | codex | hermes",
  "task_name": "clean_batch_1",
  "status": "IDLE | RUNNING | COMPLETED | BLOCKED",
  "timestamp": 1788743900.123
}
```

## 2. HUD Visual Binding
- `TASK_DISPATCH` -> Triggers photon particle beam from `from_agent` to `to_agent`.
- `TASK_PROGRESS` -> Triggers target card dynamic pulse & number roll.
- `TASK_DONE` -> Emits shockwave ripple and increments target done_count.
