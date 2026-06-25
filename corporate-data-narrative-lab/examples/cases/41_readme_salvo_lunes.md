# El README que salvo el lunes

<!-- story
concept: documentacion minima reproducible
characters: Tania, Joel, Eva, la coordinadora
situation: un proyecto de datos funciona solo para quien lo hizo porque no explica como correrlo
bad_logic: el codigo se explica solo si esta bien escrito
escalation: la persona dueña sale de vacaciones y el equipo no puede regenerar resultados
data_turn: Tania compara tiempos de arranque con y sin README
chart: checklist de reproducibilidad
decision: agregar objetivo, datos, setup, comandos y salida esperada
punchline: El README no hizo analisis; solo encontro la luz del cuarto.
rule: un README util permite correr, entender y verificar el proyecto
synthetic_data: true
-->

## La carpeta muda

> **Tania:** "El proyecto esta listo, solo hay que correrlo."

> **Joel:** "Nadie sabe con que comando."

> **Eva:** "El codigo esta bastante claro."

> **Tania:** "El codigo no dice donde bajar datos."

> **Eva:** "Eso lo sabia Eva."

> **la coordinadora:** "Eva esta de vacaciones y no dejo webhook mental."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## El codigo no contestaba llamadas

> **Eva:** "Le escribimos rapido."

> **Joel:** "Tambien necesitamos repetirlo el proximo mes."

> **Eva:** "Podemos guardar sus respuestas en favoritos."

> **la coordinadora:** "Eso se llama README con pasos extra."

> **Eva:** "La carpeta tiene nombres descriptivos."

> **Tania:** "Descriptivos para quien ya entiende la historia."

> **Joel:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **la coordinadora:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## Cinco cosas para empezar

> **Tania:** "Medi cuanto tarda alguien nuevo en correrlo."

> **la coordinadora:** "Que parte los detiene."

> **Tania:** "Faltan objetivo, setup, datos, comando y salida esperada."

> **Joel:** "Eso explica por que la salida parecia correcta al principio."

> **Tania:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="checklist de reproducibilidad">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">checklist de reproducibilidad</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="224" width="174" height="36" fill="#286d9b"/>
  <text x="157" y="214" font-size="18" text-anchor="middle">18</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">sin README</text>
  <rect x="272" y="136" width="174" height="124" fill="#d58b2f"/>
  <text x="359" y="126" font-size="18" text-anchor="middle">62</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">con comandos</text>
  <rect x="474" y="85" width="174" height="175" fill="#4c8b63"/>
  <text x="561" y="75" font-size="18" text-anchor="middle">87</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">con salida</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">La documentacion minima acelera reproduccion.</text>
</svg>

<!-- learning:pause -->
> **Joel:** "Que debe decir un README minimo para que otra persona reproduzca un analisis."

**Lo que muestra:** La evidencia muestra que el README reduce tiempo perdido antes del analisis. Debe explicar objetivo, fuentes, entorno, comandos, salida esperada y criterios de verificacion. No reemplaza el codigo; abre la puerta correcta.

## El lunes encuentra instrucciones

> **la coordinadora:** "Agregamos README antes de compartir resultados."

> **la coordinadora:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Eva:** "Tardaremos una hora en escribirlo."

> **Tania:** "Y ahorraremos muchas horas de lunes."

> **Eva:** "Y si alguien pide excepcion."

> **Tania:** "Que la pida con costo visible y fecha."

> **la coordinadora:** "Y si no hay evidencia, no hay lanzamiento."

> **Joel:** "Eso va a incomodar a la prisa."

> **Tania:** "La prisa ya nos estaba cobrando intereses."

> **Joel:** "El README no hizo analisis; solo encontro la luz del cuarto."

**Regla:** un README util permite correr, entender y verificar el proyecto.
