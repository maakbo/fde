$ErrorActionPreference = "Stop"
$scriptPath = Join-Path $PSScriptRoot "fde-manage.py"
if (-not (Test-Path $scriptPath)) {
  $scriptPath = Join-Path $PSScriptRoot "fde_consumer.py"
}

if (Get-Command py -ErrorAction SilentlyContinue) {
  & py -3 $scriptPath @args
  exit $LASTEXITCODE
}
if (Get-Command python -ErrorAction SilentlyContinue) {
  & python -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 9) else 1)"
  if ($LASTEXITCODE -eq 0) {
    & python $scriptPath @args
    exit $LASTEXITCODE
  }
}
Write-Error "Portable FDE requires Python 3.9+ (py -3 or python)."
