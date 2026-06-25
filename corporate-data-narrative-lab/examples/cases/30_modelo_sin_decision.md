# El modelo que no sabia que decision tomar

<!-- story
concept: definir la decision antes del modelo
characters: Clara, Diego, Ramon, la directora
situation: un equipo predice abandono sin definir que accion tomara con cada prediccion
bad_logic: predecir algo importante ya es un producto
escalation: las areas reciben scores pero nadie sabe si llamar, descontar o esperar
data_turn: Clara convierte el score en un arbol de decisiones por accion y costo
chart: arbol de decision
decision: crear segmentos accionables y medir respuesta por accion
punchline: El modelo sabia quien se iba; nosotros no sabiamos que hacer con la despedida.
rule: un modelo de datos debe ayudar a tomar una decision concreta
synthetic_data: true
-->

## La lista de riesgo

> **Clara:** "Tenemos una lista de clientes con alto riesgo de irse."

> **Diego:** "Que hara el negocio con esa lista."

> **Ramon:** "La va a usar para retener."

> **Clara:** "Retener como, llamar, descontar o cambiar servicio."

> **Ramon:** "Eso lo define cada area."

> **la directora:** "Entonces el producto es una adivinanza compartida."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## Saber no era actuar

> **Ramon:** "Mandamos el score y que prioricen."

> **Diego:** "Priorizar sin accion solo ordena la ansiedad."

> **Ramon:** "Podemos poner semaforo para que se vea claro."

> **la directora:** "Rojo no dice si conviene llamar o no molestar."

> **Ramon:** "Ventas pedira descuento para todos los rojos."

> **Clara:** "Finanzas acaba de sentir un escalofrio."

> **Diego:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **la directora:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## El score necesita verbo

> **Clara:** "Cruce riesgo con accion posible y costo."

> **la directora:** "Quien necesita que respuesta."

> **Clara:** "Hay clientes para llamada, oferta y no intervencion."

> **Diego:** "Eso explica por que la salida parecia correcta al principio."

> **Clara:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="arbol de decision">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">arbol de decision</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="187" width="174" height="73" fill="#286d9b"/>
  <text x="157" y="177" font-size="18" text-anchor="middle">34</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">solo score</text>
  <rect x="272" y="105" width="174" height="155" fill="#d58b2f"/>
  <text x="359" y="95" font-size="18" text-anchor="middle">72</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">accion definida</text>
  <rect x="474" y="85" width="174" height="175" fill="#4c8b63"/>
  <text x="561" y="75" font-size="18" text-anchor="middle">81</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">resultado medido</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">La utilidad aparece cuando hay decision y seguimiento.</text>
</svg>

<!-- learning:pause -->
> **Diego:** "Que decision debe existir antes de entrenar o publicar un modelo predictivo."

**Lo que muestra:** El arbol muestra que el score solo ordena probabilidad. Para crear producto hacen falta acciones, responsables, costos y resultados esperados. La prediccion vale cuando cambia una decision concreta y medible.

## Prediccion con accion

> **la directora:** "Publicamos recomendaciones por accion, no solo riesgo."

> **la directora:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Ramon:** "El modelo se vera menos magico."

> **Clara:** "Y mas facil de usar el lunes."

> **Ramon:** "Y si alguien pide excepcion."

> **Clara:** "Que la pida con costo visible y fecha."

> **la directora:** "Y si no hay evidencia, no hay lanzamiento."

> **Diego:** "Eso va a incomodar a la prisa."

> **Clara:** "La prisa ya nos estaba cobrando intereses."

> **Diego:** "El modelo sabia quien se iba; nosotros no sabiamos que hacer con la despedida."

**Regla:** un modelo de datos debe ayudar a tomar una decision concreta.
