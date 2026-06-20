# Contributing

## Antes De Crear Un Caso

Lee:

- [DATA_SCIENCE_CURRICULUM.md](DATA_SCIENCE_CURRICULUM.md)
- [NARRATIVE_PRINCIPLES.md](NARRATIVE_PRINCIPLES.md)
- [DATA_VISUAL_EVIDENCE_GUIDE.md](DATA_VISUAL_EVIDENCE_GUIDE.md)
- [HUMOR_GUIDE.md](HUMOR_GUIDE.md)
- [CASE_RUBRIC.md](CASE_RUBRIC.md)

## Reglas

- No crear dashboards.
- Usar datos sintéticos.
- Explicitar técnica mínima suficiente.
- Incluir mala decisión plausible.
- Incluir acción robusta y acción débil.
- Incluir piloto medible.
- Incluir revisión ética.
- Mantener HTML autocontenido y simple.
- Usar humor solo donde ayude a ver el absurdo organizacional.

## Estructura De Un Caso

Usa `templates/case_story_template.md`. Todo caso publicado debe pasar:

```powershell
python tools/validate_case_structure.py examples/cases/nombre_del_caso.md
python -m pytest
```

## Convenciones

- Archivos de caso: `examples/cases/NN_titulo_en_snake_case.md`
- HTML: `examples/html/NN_titulo_en_snake_case.html`
- Especificación de datos: `examples/data_specs/NN_titulo_en_snake_case.yml`
- Especificación visual: `examples/visual_specs/NN_titulo_en_snake_case.yml`

