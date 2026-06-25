# El score que no sabia que era mudanza

<!-- story
concept: human in the loop para decisiones de alto impacto
characters: Ines, Marco, Paula, la directora
situation: un score de riesgo marca cambios normales como senales peligrosas
bad_logic: si el score sube, la decision automatica debe endurecerse
escalation: personas con eventos normales quedan bloqueadas sin explicacion
data_turn: Ines compara errores con y sin revision de contexto
chart: errores por umbral y revision
decision: usar score como alerta, pedir contexto y dejar apelacion
punchline: El score veia riesgo; Paula tuvo que recordarle que la gente se muda.
rule: en decisiones de alto impacto, el score debe informar, no sustituir el juicio
synthetic_data: true
-->

## El riesgo que subio solo

> **Ines:** "El score sube cuando alguien cambia direccion y telefono."

> **Marco:** "Eso tambien pasa cuando alguien se muda."

> **Paula:** "El patron se parece a fraude."

> **Ines:** "Parecerse no alcanza para bloquear."

> **Paula:** "La automatizacion baja tiempo de respuesta."

> **la directora:** "Tambien baja la oportunidad de explicar."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## Cambiar de vida parecia fraude

> **Paula:** "Subimos el umbral y ya."

> **Marco:** "Seguira castigando eventos normales extremos."

> **Paula:** "Entonces que la gente avise antes de vivir."

> **la directora:** "La vida no siempre abre ticket preventivo."

> **Paula:** "Podemos mandar mensaje automatico."

> **Ines:** "Si la cuenta esta bloqueada, no lo va a leer."

> **Marco:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **la directora:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## El contexto baja errores

> **Ines:** "Compare decisiones automaticas con revision de contexto."

> **la directora:** "Cuanto error quitamos al preguntar antes."

> **Ines:** "La revision conserva alertas y baja bloqueos injustos."

> **Marco:** "Eso explica por que la salida parecia correcta al principio."

> **Ines:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="errores por umbral y revision">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">errores por umbral y revision</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="85" width="174" height="175" fill="#286d9b"/>
  <text x="157" y="75" font-size="18" text-anchor="middle">29</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">automatico</text>
  <rect x="272" y="134" width="174" height="126" fill="#d58b2f"/>
  <text x="359" y="124" font-size="18" text-anchor="middle">21</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">umbral alto</text>
  <rect x="474" y="218" width="174" height="42" fill="#4c8b63"/>
  <text x="561" y="208" font-size="18" text-anchor="middle">7</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">con revision</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">La revision humana baja errores de alto impacto.</text>
</svg>

<!-- learning:pause -->
> **Marco:** "Que papel debe tener una persona cuando el modelo afecta acceso, dinero o derechos."

**Lo que muestra:** La evidencia separa score, contexto y decision. El score detecta similitudes, pero una revision humana puede identificar explicaciones normales y pedir datos adicionales. Human in the loop no es adorno: reduce dano cuando la decision afecta a personas.

## Alerta no es sentencia

> **la directora:** "El bloqueo automatico queda limitado a casos confirmados."

> **la directora:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Paula:** "Algunas revisiones tardaran mas."

> **Ines:** "La rapidez deja de atropellar mudanzas."

> **Paula:** "Y si alguien pide excepcion."

> **Ines:** "Que la pida con costo visible y fecha."

> **la directora:** "Y si no hay evidencia, no hay lanzamiento."

> **Marco:** "Eso va a incomodar a la prisa."

> **Ines:** "La prisa ya nos estaba cobrando intereses."

> **Marco:** "El score veia riesgo; Paula tuvo que recordarle que la gente se muda."

**Regla:** en decisiones de alto impacto, el score debe informar, no sustituir el juicio.
