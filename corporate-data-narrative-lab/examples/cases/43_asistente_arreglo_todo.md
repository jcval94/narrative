# El asistente que arreglo tambien lo que servia

<!-- story
concept: control de cambios al trabajar con asistentes de codigo
characters: Iris, Gael, Marta, el tech lead
situation: un asistente de codigo modifica archivos fuera del alcance pedido
bad_logic: si el asistente mejora el codigo, cualquier cambio adicional es bienvenido
escalation: se mezclan refactors, cambios visuales y bugfix en un solo parche dificil de revisar
data_turn: Iris compara diff solicitado contra diff real por archivo
chart: diff revisado
decision: dar alcance explicito, revisar diff y separar cambios no pedidos
punchline: El asistente arreglo el bug y de paso redecoró la cocina.
rule: con asistentes de codigo, controla alcance, revisa diff y conserva decision humana
synthetic_data: true
-->

## El bug desaparecio

> **Iris:** "El asistente ya corrigio el error."

> **Gael:** "Tambien cambio nombres, estilos y dos helpers."

> **Marta:** "Seguro lo vio necesario."

> **Iris:** "O vio oportunidad."

> **Marta:** "El resultado se ve mas limpio."

> **el tech lead:** "La revision se ve mas imposible."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## Tambien desaparecio medio estilo

> **Marta:** "Aceptamos todo si pasan pruebas."

> **Gael:** "Las pruebas no cubren el cambio visual."

> **Marta:** "Entonces confiamos en su gusto."

> **el tech lead:** "Su gusto movio un boton que ventas usa diario."

> **Marta:** "Pero arreglo el bug principal."

> **Iris:** "Nadie discute eso; discutimos todo lo demas."

> **Gael:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **el tech lead:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## El diff cuenta la verdad

> **Iris:** "Separe el diff por alcance pedido y alcance extra."

> **el tech lead:** "Cuanto cambio venia de la tarea."

> **Iris:** "La mitad del parche era sorpresa."

> **Gael:** "Eso explica por que la salida parecia correcta al principio."

> **Iris:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="diff revisado">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">diff revisado</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="99" width="174" height="161" fill="#286d9b"/>
  <text x="157" y="89" font-size="18" text-anchor="middle">48</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">pedido</text>
  <rect x="272" y="85" width="174" height="175" fill="#d58b2f"/>
  <text x="359" y="75" font-size="18" text-anchor="middle">52</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">extra</text>
  <rect x="474" y="112" width="174" height="148" fill="#4c8b63"/>
  <text x="561" y="102" font-size="18" text-anchor="middle">44</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">aceptado</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">El diff debe coincidir con la intencion.</text>
</svg>

<!-- learning:pause -->
> **Gael:** "Que debes revisar antes de aceptar cambios generados por un asistente de codigo."

**Lo que muestra:** La evidencia separa archivos tocados por la tarea y archivos modificados por iniciativa del asistente. Trabajar con Codex, Cursor, Claude Code o Gemini CLI exige especificar alcance, revisar diff, correr pruebas y rechazar cambios no pedidos.

## Pedir con bardas

> **el tech lead:** "El parche se reduce al bug y el resto va a otra tarea."

> **el tech lead:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Marta:** "Perdemos una limpieza gratis."

> **Iris:** "Ganamos una revision que si cabe en la cabeza."

> **Marta:** "Y si alguien pide excepcion."

> **Iris:** "Que la pida con costo visible y fecha."

> **el tech lead:** "Y si no hay evidencia, no hay lanzamiento."

> **Gael:** "Eso va a incomodar a la prisa."

> **Iris:** "La prisa ya nos estaba cobrando intereses."

> **Gael:** "El asistente arreglo el bug y de paso redecoró la cocina."

**Regla:** con asistentes de codigo, controla alcance, revisa diff y conserva decision humana.
