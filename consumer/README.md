# Portable FDE consumer profiles

`business-context-v0.1.paths.json` is the profile build input. It selects a
verbatim closure of the Business Context and Mermaid authoring Skills, their
reader-facing review Skill, direct checks/references and the root `templates/` paths those Skills already
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

## Field delivery profile

`field-delivery-v0.1.paths.json` adds Discovery, Definition, Architecture and their
direct templates/references to the smaller modeling profile. Use it when carrying
a field problem through selection, conditions, work design and bounded trial.
Build with the same command and this profile path. Its additional methods are
provisional field guidance; packaging does not establish production readiness.
A full clone also contains the executable synthetic case and public examples.
No tagged release is published by a local build.

## Icon preference

The profile includes maakbo SVGs, the shared registry, and MDI license information.
MDI diagrams default to official MDI GitHub SVGs (v7.4.47); set
`"mdi_source": "iconify"` to use Iconify API instead. No MDI image data or package
is included. GitHub Mermaid blocks the Iconify API; use the default there.
Both families use uniform 28 x 28 image nodes.
Initial installation defaults to MDI; add `--icon-set maakbo` when desired.
An existing `.fde/config.json` is consumer-owned and takes precedence. It is
excluded from the managed manifest and is never overwritten on updates.

Use `icon_registry.py configure` to change the preference, `show` for semantic
URLs and dimensions, and `create` to instantiate a template for that project.
Existing diagrams keep their explicit URLs; use `migrate --write` only for an
intentional source migration. See the authoring Skill's icon-selection reference.

## Reader review

The profile includes `reader-facing-artifact-review` and its structural checker.
Use it to finish subject headings, diagrams, and business prose together, then
request a separate reviewer when the host supports authorized sub-agents.
Packaging a Skill does not create a sub-agent facility or publish a new release;
the host provides delegation and the existing update mechanism installs tagged
artifacts. Prose/source review needs only Python. Rendering remains optional and
requires a supported native preview or the upstream export Skill and renderer.
