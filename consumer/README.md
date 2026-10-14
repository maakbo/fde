# Portable FDE consumer profiles

`business-context-v0.1.paths.json` is the profile build input. It selects a
verbatim closure of the Business Context and Mermaid authoring Skills, their
direct checks/references and the root `templates/` paths those Skills already
reference. No Skill path is rewritten during packaging.

Build a reviewable artifact locally:

```bash
python3 scripts/build_consumer_profile.py \
  --profile consumer/profiles/business-context-v0.1.paths.json \
  --output /tmp/business-context-v0.1.zip \
  --version 0.1.0
```

The tagged GitHub Release publication step is intentionally separate. Until a
release URL exists, extract the artifact and run its staged
`.fde/fde-manage.py install --source <stage> --target <consumer-repository>`.
The installed `.fde/fde` and `.fde/fde.ps1` launchers centralize Python 3
selection for macOS/Linux and Windows respectively.

The consumer's root `AGENTS.md` and Copilot instructions remain untouched.
Read `.fde/fde-instructions.md` and decide locally whether to add its short
integration snippet.

## Icon preference

The profile includes maakbo SVGs, the shared registry, and MDI license information.
MDI diagrams refer directly to Iconify; no MDI image data or package is included.
Initial installation defaults to MDI; add `--icon-set maakbo` when desired.
An existing `.fde/config.json` is consumer-owned and takes precedence. It is
excluded from the managed manifest and is never overwritten on updates.

Use `icon_registry.py configure` to change the preference, `show` for semantic
URLs and dimensions, and `create` to instantiate a template for that project.
Existing diagrams keep their explicit URLs; use `migrate --write` only for an
intentional source migration. See the authoring Skill's icon-selection reference.
