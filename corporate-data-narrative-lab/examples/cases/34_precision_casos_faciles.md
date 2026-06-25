# La precision que festejaba casos faciles

<!-- story
concept: evaluacion por segmentos y dificultad
characters: Santi, Marisol, Elia, el jefe
situation: un modelo presume alta precision porque la prueba tiene muchos casos faciles
bad_logic: la metrica promedio representa todos los tipos de caso
escalation: el modelo falla justo donde la decision importa mas
data_turn: Marisol divide desempeno por dificultad y valor de caso
chart: matriz por dificultad
decision: evaluar por segmento y lanzar solo donde cumple
punchline: El modelo era excelente nadando en alberca para ninos.
rule: una metrica promedio puede esconder fallas en los segmentos que importan
synthetic_data: true
-->

## El promedio feliz

> **Santi:** "La precision general esta altisima."

> **Marisol:** "La muestra tiene demasiados casos faciles."

> **Elia:** "Son casos reales."

> **Santi:** "Pero no son los que nos duelen."

> **Elia:** "El promedio resume todo."

> **el jefe:** "Tambien aplana lo dificil."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## La prueba estaba muy comoda

> **Elia:** "Lanzamos y vamos aprendiendo."

> **Marisol:** "Aprender con casos caros suena a colegiatura."

> **Elia:** "El modelo solo se equivoca donde hay matices."

> **el jefe:** "Los matices son precisamente los reclamos grandes."

> **Elia:** "Podemos excluir excepciones."

> **Santi:** "Eso deja fuera el trabajo importante."

> **Marisol:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **el jefe:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## Facil tambien cuenta, pero no decide solo

> **Santi:** "Separe la prueba por dificultad y valor."

> **el jefe:** "Donde acierta de verdad."

> **Santi:** "En facil va perfecto; en dificil se cae."

> **Marisol:** "Eso explica por que la salida parecia correcta al principio."

> **Santi:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="matriz por dificultad">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">matriz por dificultad</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="85" width="174" height="175" fill="#286d9b"/>
  <text x="157" y="75" font-size="18" text-anchor="middle">96</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">faciles</text>
  <rect x="272" y="126" width="174" height="134" fill="#d58b2f"/>
  <text x="359" y="116" font-size="18" text-anchor="middle">74</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">medios</text>
  <rect x="474" y="186" width="174" height="74" fill="#4c8b63"/>
  <text x="561" y="176" font-size="18" text-anchor="middle">41</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">dificiles</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">El promedio ocultaba el segmento de mayor riesgo.</text>
</svg>

<!-- learning:pause -->
> **Marisol:** "Por que conviene revisar metricas por segmento antes de lanzar un modelo."

**Lo que muestra:** La evidencia muestra que el promedio mezcla casos faciles y dificiles. Si los errores en el segmento dificil cuestan mas, la precision global no basta. Evaluar por segmentos evita aprobar modelos que funcionan solo en la parte comoda.

## Lanzar donde si sabe

> **el jefe:** "Lanzamos solo en casos simples y revisamos los dificiles."

> **el jefe:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Elia:** "El alcance inicial sera menor."

> **Santi:** "Y las fallas no caeran donde mas pesan."

> **Elia:** "Y si alguien pide excepcion."

> **Santi:** "Que la pida con costo visible y fecha."

> **el jefe:** "Y si no hay evidencia, no hay lanzamiento."

> **Marisol:** "Eso va a incomodar a la prisa."

> **Santi:** "La prisa ya nos estaba cobrando intereses."

> **Marisol:** "El modelo era excelente nadando en alberca para ninos."

**Regla:** una metrica promedio puede esconder fallas en los segmentos que importan.
