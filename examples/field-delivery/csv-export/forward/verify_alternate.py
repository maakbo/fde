import csv,io,sys
from pathlib import Path
raw=Path(sys.argv[1]).read_bytes()
if not raw.startswith(b'\xef\xbb\xbf'):raise ValueError('BOM missing')
rows=list(csv.reader(io.StringIO(raw.decode('utf-8-sig'),newline='')))
ids=['comma,only','quote"only','cr\ronly','lf\nonly','日本語のみ']
expected=[['受注ID','受注日','状況']]+[[x,'2026-10-06','NEW'] for x in ids]
if rows!=expected:raise ValueError(f'alternate mismatch: {rows!r}')
print('PASS alternate fixture: comma-only, quote-only, CR-only, LF-only, Japanese-only; five rows preserved')
