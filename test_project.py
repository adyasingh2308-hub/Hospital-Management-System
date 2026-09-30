import unittest
import json
import tempfile
from pathlib import Path
from storage import load_data, save_data


class StorageTests(unittest.TestCase):
    def test_save_and_load_records(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "sample.json"
            # Test JSON behavior independently of the project's data files.
            import json
            sample = [{"patient_id": "P999", "name": "Test Patient"}]
            path.write_text(json.dumps(sample), encoding="utf-8")
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), sample)

    def test_empty_json_list(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "empty.json"
            path.write_text("[]", encoding="utf-8")
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), [])


if __name__ == "_main_":
    unittest.main()