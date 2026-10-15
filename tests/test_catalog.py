import datetime as dt
import importlib.util
from pathlib import Path
import unittest

MODULE = Path(__file__).resolve().parents[1] / "automation" / "update_catalog.py"
spec = importlib.util.spec_from_file_location("catalog_bot", MODULE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class CatalogTests(unittest.TestCase):
    def test_replaces_only_generated_block(self):
        text = "Intro\nSTART\nold\nEND\nHuman section\n"
        self.assertEqual(mod.replace_between(text, "START", "END", "new"),
                         "Intro\nSTART\nnew\nEND\nHuman section\n")

    def test_refuses_missing_markers(self):
        with self.assertRaises(ValueError):
            mod.replace_between("START\nold", "START", "END", "new")

    def test_escaping_description(self):
        self.assertEqual(mod.safe_text("<script>hi</script> |bad\nmore"), "hi bad more")

    def test_accurate_REA_reference(self):
        pat = mod.EXPLICIT_REA_PATTERN
        self.assertIsNotNone(pat.search("built with https://github.com/morluto/rea"))
        self.assertIsNotNone(pat.search("see https://rea.tools/ docs"))
        self.assertIsNone(pat.search("Rea is just a common first name"))
        self.assertIsNone(pat.search("https://github.com/morluto/reaction"))

    def test_priority_outweighs_stars(self):
        projects = [{"repo":"someone/utility", "priority":5},
                    {"repo":"someone/popular", "priority":4}]
        metadata = {"someone/utility":{"stargazers_count":1},
                    "someone/popular":{"stargazers_count":100000}}
        ranked = mod.rank_featured(projects, metadata, dt.date(2026,10,15))
        self.assertEqual(ranked[0]["repo"], "someone/utility")

    def test_known_links_deduplicate(self):
        links = mod.links_in_readme("[Foo](https://github.com/OWNER/project) and https://github.com/OWNER/other#readme")
        self.assertIn("owner/project", links)
        self.assertIn("owner/other", links)

    def test_discover_requires_readme_evidence(self):
        class FakeGitHub:
            def search(self, query, per_page):
                return [{"full_name":"demo/real-example", "fork":False,"archived":False,
                         "description":"tool | example", "stargazers_count":3, "pushed_at":"2026-10-14T00:00:00Z"},
                        {"full_name":"demo/not-rea", "fork":False, "archived":False,
                         "description":"just a test", "stargazers_count":7, "pushed_at":"2026-10-14T00:00:00Z"}]
            def readme(self, full_name):
                return ("uses https://github.com/morluto/rea" if full_name == "demo/real-example"
                        else "no relation")
        config = {"featured":[], "excluded_repositories":[], "search_queries":["a"],
                  "search_results_per_query": 25, "readme_checks_per_run": 18,
                  "candidates_limit": 15}
        candidates, added = mod.discover(FakeGitHub(), config, [], "", dt.date(2026,10,15))
        self.assertEqual(len(added), 1)
        self.assertEqual(candidates[0]["repo"], "demo/real-example")
        self.assertEqual(candidates[0]["status"], "Needs review — README mentions REA")


if __name__ == "__main__":
    unittest.main()
