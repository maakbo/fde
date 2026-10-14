#!/usr/bin/env python3
"""Regression checks for reader-artifact boundaries and title ownership."""

import unittest

from check_reader_artifact import inspect


def diagram(settings="", title=""):
    header = f"---\n{title}{settings}\n---\n" if settings or title else ""
    return f"```mermaid\n{header}flowchart LR\n  a --- b\n```\n"


class ReaderArtifactTests(unittest.TestCase):
    def test_embedded_title_is_rejected_with_explicit_exception(self):
        text = "# 受注\n" + diagram(title="title: 受注\n") + "注文を受け付ける。\n"
        self.assertTrue(any("frontmatter title" in item for item in inspect(text)[0]))
        self.assertEqual(inspect(text, allow_diagram_title=True)[0], [])

    def test_next_section_cannot_supply_missing_explanation(self):
        text = "# 受注\n" + diagram() + "## 出荷\n商品を発送する。\n"
        self.assertTrue(any("business explanation" in item for item in inspect(text)[0]))

    def test_multiple_diagrams_and_child_headings(self):
        text = "# 受注\n## 注文受付\n" + diagram() + "注文を受け付ける。\n"
        text += "### 内容確認\n" + diagram() + "内容を確認する。\n### 出荷\n" + diagram() + "商品を発送する。\n"
        self.assertEqual(inspect(text)[0], [])

    def test_code_heading_is_not_subject_or_section_boundary(self):
        no_subject = "```text\n# 注文\n```\n" + diagram() + "受け付ける。\n"
        self.assertTrue(any("subject heading" in item for item in inspect(no_subject)[0]))
        text = "# 注文\n" + diagram() + "```text\n# このページの構成\n```\n受け付ける。\n"
        self.assertEqual(inspect(text)[0], [])

    def test_mixed_settings_are_observations(self):
        text = "# 受注\n" + diagram("config:\n  layout: dagre\n  flowchart:\n    curve: basis") + "受け付ける。\n"
        text += "## 出荷\n" + diagram("config:\n  layout: elk\n  flowchart:\n    curve: basis") + "発送する。\n"
        errors, observations = inspect(text)
        self.assertEqual(errors, [])
        self.assertTrue(any("mixed layout/curve" in item for item in observations))

    def test_author_heading_and_comment_only_reading(self):
        text = "# このモデルが表していること\n" + diagram() + "%% 保守コメント\n"
        errors, _ = inspect(text)
        self.assertTrue(any("business/theme heading" in item for item in errors))
        self.assertTrue(any("business explanation" in item for item in errors))

    def test_multiline_html_comment_cannot_supply_explanation(self):
        text = "# 受注\n" + diagram() + "<!--\n注文を受け付ける。\n## 隠れた見出し\n-->\n"
        errors, _ = inspect(text)
        self.assertTrue(any("business explanation" in item for item in errors))
        self.assertEqual(inspect(text + "注文を受け付ける。\n")[0], [])

    def test_inline_html_comment_preserves_visible_explanation(self):
        text = "# 受注\n<!-- 保守用\nコメント -->\n" + diagram()
        text += "<!-- 補足 -->注文を<!-- 内部メモ -->受け付ける。<!--\n非公開\n-->\n"
        self.assertEqual(inspect(text)[0], [])

    def test_introductory_prose_must_follow_diagram(self):
        text = "# 受注\n注文を受け付ける。\n" + diagram() + "内容を確認する。\n"
        self.assertTrue(any("directly after" in item for item in inspect(text)[0]))


if __name__ == "__main__":
    unittest.main()
