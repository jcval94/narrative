from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

import yaml


CSS = """
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  background: #f6f7f9;
  color: #1d2433;
}
main {
  width: min(920px, calc(100% - 32px));
  margin: 0 auto;
  padding: 36px 0 52px;
}
.panel {
  background: #fff;
  border: 1px solid #d7dde7;
  border-radius: 8px;
  padding: 18px;
}
h1 {
  margin: 0 0 10px;
  font-size: clamp(1.8rem, 4vw, 2.8rem);
}
p {
  color: #5e697a;
  line-height: 1.55;
}
canvas {
  width: 100%;
  max-height: 460px;
}
"""


def build_html(spec: dict[str, object]) -> str:
    chart = spec["chart"]
    chart_json = json.dumps(chart, ensure_ascii=False)
    title = str(spec.get("title", "Evidencia visual"))
    subtitle = str(spec.get("subtitle", "Una gráfica simple como evidencia narrativa."))
    note = str(spec.get("note", "Observa el patrón antes de proponer una solución."))

    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>{CSS}</style>
</head>
<body>
  <main>
    <h1>{html.escape(title)}</h1>
    <p>{html.escape(subtitle)}</p>
    <section class="panel">
      <canvas id="evidenceChart" aria-label="{html.escape(title)}"></canvas>
      <p>{html.escape(note)}</p>
    </section>
  </main>
  <script>
    const config = {chart_json};
    const ctx = document.getElementById('evidenceChart');
    new Chart(ctx, config);
  </script>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a simple Chart.js HTML evidence file.")
    parser.add_argument("visual_spec_path", type=Path)
    parser.add_argument("output_path", type=Path)
    args = parser.parse_args()

    spec = yaml.safe_load(args.visual_spec_path.read_text(encoding="utf-8"))
    output = build_html(spec)
    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    args.output_path.write_text(output, encoding="utf-8")
    print(f"Wrote {args.output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

