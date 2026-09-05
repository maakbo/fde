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
