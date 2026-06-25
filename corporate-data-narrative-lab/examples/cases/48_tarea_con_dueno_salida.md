# La tarea que tenia dueno, salida y no drama

<!-- story
concept: tareas para agentes con responsable, salida y revision
characters: Fabi, Tono, Greta, el responsable
situation: un equipo convierte pedidos ambiguos en tareas listas para un agente
bad_logic: una tarea corta es mejor aunque no diga salida esperada
escalation: los agentes entregan cosas incompatibles y nadie sabe quien aprueba
data_turn: Fabi compara tareas con dueno, salida y revision contra tareas abiertas
chart: flujo de revision
decision: crear tareas con contexto, archivos, salida esperada, pruebas y aprobador
punchline: La tarea no se volvio larga; se volvio adulta.
rule: una tarea para agentes necesita contexto, limites, salida verificable y responsable de revision
synthetic_data: true
-->

## La tarea chiquita

> **Fabi:** "La tarea dice ajustar reporte."

> **Tono:** "Eso no dice quien aprueba ni que debe salir."

> **Greta:** "Era para no abrumar al agente."

> **Fabi:** "Lo abrumador es adivinar."

> **Greta:** "Mientras menos texto, mas rapido empieza."

> **el responsable:** "Y mas rapido se va por otra calle."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## Chiquita pero incompleta

> **Greta:** "Le damos libertad y corregimos despues."

> **Tono:** "Corregir despues es escribir la tarea tarde."

> **Greta:** "Entonces hacemos la especificacion cuando falle."

> **el responsable:** "Ese metodo ya tiene calendario completo."

> **Greta:** "Al menos la tarea se ve simple."

> **Fabi:** "Simple para enviar, cara para revisar."

> **Tono:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **el responsable:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## La salida se puede revisar

> **Fabi:** "Compare tareas abiertas contra tareas con salida verificable."

> **el responsable:** "Cuales llegan listas para revision."

> **Fabi:** "Las que tienen dueno, archivos, pruebas y aprobador."

> **Tono:** "Eso explica por que la salida parecia correcta al principio."

> **Fabi:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="flujo de revision">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">flujo de revision</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="196" width="124" height="64" fill="#286d9b"/>
  <text x="132" y="186" font-size="18" text-anchor="middle">33</text>
  <text x="132" y="286" font-size="13" text-anchor="middle">abierta</text>
  <rect x="222" y="128" width="124" height="132" fill="#d58b2f"/>
  <text x="284" y="118" font-size="18" text-anchor="middle">68</text>
  <text x="284" y="286" font-size="13" text-anchor="middle">con salida</text>
  <rect x="374" y="101" width="124" height="159" fill="#4c8b63"/>
  <text x="436" y="91" font-size="18" text-anchor="middle">82</text>
  <text x="436" y="286" font-size="13" text-anchor="middle">con dueno</text>
  <rect x="526" y="85" width="124" height="175" fill="#c64e36"/>
  <text x="588" y="75" font-size="18" text-anchor="middle">90</text>
  <text x="588" y="286" font-size="13" text-anchor="middle">con revision</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">La tarea ejecutable deja evidencia revisable.</text>
</svg>

<!-- learning:pause -->
> **Tono:** "Que campos hacen que una tarea para agentes sea ejecutable y revisable."

**Lo que muestra:** La evidencia muestra el flujo completo: contexto, alcance, salida esperada, prueba y responsable. Una tarea buena no describe cada movimiento, pero si elimina decisiones que el agente no debe inventar. Eso reduce vueltas y sorpresas.

## Menos drama por escrito

> **el responsable:** "Adoptamos plantilla de tarea antes de invocar agentes."

> **el responsable:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Greta:** "La tarea tendra mas lineas."

> **Fabi:** "Y menos drama en la revision."

> **Greta:** "Y si alguien pide excepcion."

> **Fabi:** "Que la pida con costo visible y fecha."

> **el responsable:** "Y si no hay evidencia, no hay lanzamiento."

> **Tono:** "Eso va a incomodar a la prisa."

> **Fabi:** "La prisa ya nos estaba cobrando intereses."

> **Tono:** "La tarea no se volvio larga; se volvio adulta."

**Regla:** una tarea para agentes necesita contexto, limites, salida verificable y responsable de revision.
