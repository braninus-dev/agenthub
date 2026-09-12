import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "skill" / "dujiangyan_harness.py"
SPEC = importlib.util.spec_from_file_location("dujiangyan_harness", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
DujiangyanHarness = MODULE.DujiangyanHarness


class HarnessTests(unittest.TestCase):
    def test_evidence_requires_non_empty_artifact(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            harness = DujiangyanHarness(root=root)
            artifact = root / "artifact.txt"
            self.assertFalse(harness.feishayan_verify(str(artifact)))
            artifact.write_text("verified", encoding="utf-8")
            self.assertTrue(harness.feishayan_verify(str(artifact)))

    def test_dredge_is_dry_run_by_default(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            harness = DujiangyanHarness(root=root)
            log = root / "logs" / "old.log.1"
            log.parent.mkdir(parents=True, exist_ok=True)
            log.write_text("old", encoding="utf-8")
            old = log.stat().st_mtime - 8 * 86400
            import os
            os.utime(log, (old, old))
            result = harness.suixiu_dredge()
            self.assertEqual(result["candidates"], 1)
            self.assertEqual(result["cleaned_logs"], 0)
            self.assertTrue(log.exists())
            result = harness.suixiu_dredge(apply=True)
            self.assertEqual(result["cleaned_logs"], 1)
            self.assertFalse(log.exists())


if __name__ == "__main__":
    unittest.main()
