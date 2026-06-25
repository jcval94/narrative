# final_final_v7_ahora_si

<!-- story
concept: control de versiones para proyectos de datos
characters: Ari, Leo, Fernanda, el jefe
situation: un analisis vive en archivos copiados con nombres finales contradictorios
bad_logic: duplicar archivos es una forma suficiente de versionar
escalation: nadie sabe que notebook produjo la grafica enviada a direccion
data_turn: Ari reconstruye cambios con historial manual contra historial de Git
chart: historial de versiones
decision: usar commits pequenos con mensajes y datos versionados por referencia
punchline: El archivo era final tantas veces que ya parecia promesa de campana.
rule: versionar es explicar cambios, no coleccionar nombres nerviosos
synthetic_data: true
-->

## El ultimo final

> **Ari:** "Use el archivo final final ahora si."

> **Leo:** "Hay otro final final con fecha de ayer."

> **Fernanda:** "Ese era antes del ajuste."

> **Ari:** "Cual ajuste."

> **Fernanda:** "El que pidio Finanzas en la junta."

> **el jefe:** "Finanzas pidio tres cosas en esa junta."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## La carpeta como arqueologia

> **Fernanda:** "Abrimos todos y comparamos a ojo."

> **Leo:** "La grafica ya se mando a direccion."

> **Fernanda:** "Entonces elegimos el que se vea mas reciente."

> **el jefe:** "Uno dice reciente porque lo copiaron hoy sin cambios."

> **Fernanda:** "El nombre tiene ahora si."

> **Ari:** "El nombre esta pidiendo terapia."

> **Leo:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **el jefe:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## Historial que contesta

> **Ari:** "Reconstrui quien cambio que y cuando."

> **el jefe:** "Que version produjo la grafica enviada."

> **Ari:** "Con nombres manuales no queda claro; con commits si."

> **Leo:** "Eso explica por que la salida parecia correcta al principio."

> **Ari:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="historial de versiones">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">historial de versiones</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="212" width="174" height="48" fill="#286d9b"/>
  <text x="157" y="202" font-size="18" text-anchor="middle">26</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">nombres</text>
  <rect x="272" y="179" width="174" height="81" fill="#d58b2f"/>
  <text x="359" y="169" font-size="18" text-anchor="middle">44</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">fechas</text>
  <rect x="474" y="85" width="174" height="175" fill="#4c8b63"/>
  <text x="561" y="75" font-size="18" text-anchor="middle">94</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">commits</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">El historial util explica diferencias, no solo orden aparente.</text>
</svg>

<!-- learning:pause -->
> **Leo:** "Que informacion guarda Git que un nombre de archivo no puede garantizar."

**Lo que muestra:** La evidencia compara carpetas copiadas contra historial con commits. Git registra autor, momento, diferencia y mensaje. Eso permite explicar por que cambio un resultado y volver a una version sin adivinar por nombres.

## Final se jubila

> **el jefe:** "El analisis entra a Git con commits por cambio logico."

> **el jefe:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Fernanda:** "Ya no podremos decorar nombres con angustia."

> **Ari:** "A cambio sabremos que se movio."

> **Fernanda:** "Y si alguien pide excepcion."

> **Ari:** "Que la pida con costo visible y fecha."

> **el jefe:** "Y si no hay evidencia, no hay lanzamiento."

> **Leo:** "Eso va a incomodar a la prisa."

> **Ari:** "La prisa ya nos estaba cobrando intereses."

> **Leo:** "El archivo era final tantas veces que ya parecia promesa de campana."

**Regla:** versionar es explicar cambios, no coleccionar nombres nerviosos.
