#!/usr/bin/env python3
"""Regression tests for the whole-work System Context source guard.

This verifies source structure, not rendered visual coordinates or business meaning.
"""
from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / ".agents/skills/mermaid-diagram-authoring/scripts/check_context_diagram.py"
ICON_ROOT = "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/"


def image_node(name: str, label: str, icon: str) -> str:
    return (
        f'  {name}@{{ label: "{label}", img: "{ICON_ROOT}{icon}", '
        'pos: "b", w: 28, h: 28, constraint: "on" }'
    )


def valid_system_context() -> str:
    original = (ROOT / "templates/icon-context.md").read_text(encoding="utf-8")
    prefix = original.split("flowchart LR", 1)[0]
    graph = "\n".join([
        "flowchart LR",
        image_node("a_provider", "提供者", "user.svg"),
        image_node("b_work", "仕事", "ellipse.svg"),
        '  p_goal("関係者と目的を共有して価値を届ける")',
        image_node("a_recipient", "利用者", "user.svg"),
        "  a_provider --- b_work",
        "  b_work -.- p_goal",
        "  b_work --- a_recipient",
        "  class a_provider,a_recipient actor;",
        "  class b_work business;",
        "  class p_goal purpose;",
        "  classDef actor fill:none,stroke:none,color:#25231F;",
        "  classDef business fill:none,stroke:none,color:#25231F;",
        "  classDef purpose fill:#FFFFFF,stroke:#9E988E,color:#25231F,stroke-width:0.75px;",
        "  linkStyle default stroke:#9E988E,stroke-width:0.75px;",
    ])
    return prefix + graph + "\n" + chr(96) * 3 + "\n"


class WholeWorkContextProfile(unittest.TestCase):
    def assert_check(self, source: str, success: bool, message: str = "", *options: str) -> None:
        with tempfile.TemporaryDirectory() as workdir:
            path = Path(workdir) / "context.md"
            path.write_text(source, encoding="utf-8")
            command = [
                sys.executable, str(CHECKER), str(path),
                "--profile", "system-context", "--strict", *options,
            ]
            result = subprocess.run(command, capture_output=True, text=True, check=False)
            output = result.stdout + result.stderr
            if success:
                self.assertEqual(result.returncode, 0, output)
            else:
                self.assertNotEqual(result.returncode, 0, output)
                self.assertIn(message, output)

    def test_sparse_whole_work_context_is_accepted(self) -> None:
        self.assert_check(valid_system_context(), True)

    def test_information_is_not_allowed_in_first_view(self) -> None:
        source = valid_system_context()
        source = source.replace(
            image_node("b_work", "仕事", "ellipse.svg"),
            image_node("i_request", "依頼", "file.svg") + "\n" +
            image_node("b_work", "仕事", "ellipse.svg"),
        )
        source = source.replace("  a_provider --- b_work", "  i_request --- b_work\n  a_provider --- b_work")
        source = source.replace("  class b_work business;", "  class b_work business;\n  class i_request information;")
        source = source.replace(
            "  classDef purpose ",
            "  classDef information fill:none,stroke:none,color:#5F5A52;\n  classDef purpose ",
        )
        self.assert_check(source, False, "System Context excludes Information")

    def test_missing_purpose_is_rejected(self) -> None:
        source = valid_system_context().replace(
            '  p_goal("関係者と目的を共有して価値を届ける")\n', ""
        ).replace("  b_work -.- p_goal\n", "").replace(
            "  class p_goal purpose;\n", ""
        ).replace(
            "  classDef purpose fill:#FFFFFF,stroke:#9E988E,color:#25231F,stroke-width:0.75px;\n", ""
        )
        self.assert_check(source, False, "exactly one agreed purpose note")

    def test_arrows_fail_even_with_general_exception(self) -> None:
        source = valid_system_context().replace(
            "  a_provider --- b_work", "  a_provider --> b_work"
        )
        self.assert_check(source, False, "System Context must not use directed arrows", "--allow-arrow-exception")

    def test_no_recipient_side_fails(self) -> None:
        source = valid_system_context()
        recipient = image_node("a_recipient", "利用者", "user.svg")
        source = source.replace(recipient + "\n", "")
        source = source.replace(
            image_node("b_work", "仕事", "ellipse.svg"),
            recipient + "\n" + image_node("b_work", "仕事", "ellipse.svg"),
        )
        self.assert_check(source, False, "providers left and recipients right")

    def test_goal_must_be_dotted_not_a_process_step(self) -> None:
        source = valid_system_context().replace(
            "  b_work -.- p_goal", "  b_work --- p_goal"
        )
        self.assert_check(source, False, "requires one dotted Business-to-purpose relation")

    def test_multiple_businesses_are_rejected(self) -> None:
        source = valid_system_context().replace(
            image_node("b_work", "仕事", "ellipse.svg"),
            image_node("b_work", "仕事", "ellipse.svg") + "\n" +
            image_node("b_other", "別業務", "ellipse.svg"),
        ).replace("  class b_work business;", "  class b_work,b_other business;")
        self.assert_check(source, False, "requires one central whole-work Business")

    def test_participant_relation_does_not_bypass_central_business(self) -> None:
        source = valid_system_context().replace(
            "  a_provider --- b_work", "  a_provider --- a_recipient"
        )
        self.assert_check(source, False, "relations must join the central Business")

    def test_default_box_cannot_hide_an_extra_phase(self) -> None:
        for name in ("phase", "Phase"):
            with self.subTest(name=name):
                source = valid_system_context().replace(
                    "flowchart LR", f'flowchart LR\n  {name}["工程"]'
                )
                self.assert_check(source, False, "requires canonical semantic nodes")

    def test_device_is_rejected(self) -> None:
        source = valid_system_context().replace(
            image_node("a_provider", "提供者", "user.svg"),
            image_node("v_device", "端末", "laptop.svg"),
        ).replace("a_provider", "v_device").replace(
            "  class v_device,a_recipient actor;", "  class a_recipient actor;"
        )
        self.assert_check(source, False, "excludes Information and devices")

    def test_default_checker_remains_backward_compatible(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CHECKER), str(ROOT / "templates/icon-context.md"), "--strict"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
