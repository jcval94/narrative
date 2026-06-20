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
- Crear investigaciones educativas, no reportes expositivos.
- Abrir con intriga antes que contexto.
- Definir protagonista, narrador o rol del alumno.
- Hacer que el alumno investigue con preguntas activas.
- Usar datos sintéticos.
- Explicitar técnica mínima suficiente.
- Traducir jerga: primero lenguaje humano, después término técnico.
- Incluir mala decisión plausible.
- Incluir acción robusta y acción débil.
- Incluir piloto medible.
- Incluir revisión ética.
- Mantener HTML autocontenido y simple.
- Usar humor integrado solo donde ayude a ver el absurdo organizacional.
- Cerrar con consecuencia cómica o tragicómica, regla transferible y pregunta de transferencia.
- Permitir tarjetas narrativas solo si enseñan una pista, contraste, cálculo o regla.
- Prohibir KPI cards de monitoreo, filtros, tabs, drilldowns, navegación compleja y self-service.

## Estructura De Un Caso

Usa `templates/case_story_template.md`. Todo caso publicado debe pasar:

```powershell
python tools/validate_case_structure.py examples/cases/nombre_del_caso.md
python tools/validate_case_structure.py --narrative-learning-standard examples/cases/nombre_del_caso.md
python -m pytest
```

## Convenciones

- Archivos de caso: `examples/cases/NN_titulo_en_snake_case.md`
- HTML: `examples/html/NN_titulo_en_snake_case.html`
- Especificación de datos: `examples/data_specs/NN_titulo_en_snake_case.yml`
- Especificación visual: `examples/visual_specs/NN_titulo_en_snake_case.yml`
