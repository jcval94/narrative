# Pip instalo en la oficina de al lado

<!-- story
concept: entornos virtuales y dependencias
characters: Javi, Renata, Ulises, la lider
situation: el equipo instala paquetes con pip pero el proyecto usa otro entorno
bad_logic: si pip dice instalado, el programa ya lo puede importar
escalation: se duplican instalaciones, cambian versiones y nadie sabe que entorno corre
data_turn: Renata compara paquetes instalados por entorno y comando usado
chart: paquetes por ambiente
decision: usar python -m pip dentro del entorno activo y guardar requirements
punchline: Pip si trabajo; solo fue a la oficina equivocada.
rule: instala dependencias desde el mismo Python que ejecuta el proyecto
synthetic_data: true
-->

## Instalado pero invisible

> **Javi:** "Pip dice que pandas ya esta instalado."

> **Renata:** "El proyecto dice que no puede importarlo."

> **Ulises:** "Uno de los dos miente."

> **Javi:** "O hablan de entornos distintos."

> **Ulises:** "Use el comando de siempre."

> **la lider:** "El comando de siempre apunta al lugar de siempre."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## La recepcion equivocada

> **Ulises:** "Instalamos otra vez."

> **Renata:** "Eso puede empeorar el mapa."

> **Ulises:** "Si lo instalamos suficientes veces, aparecera."

> **la lider:** "Tambien aparecieron versiones diferentes."

> **Ulises:** "La computadora esta llena de soluciones."

> **Javi:** "Ninguna en el cuarto correcto."

> **Renata:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **la lider:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## El paquete estaba, pero no ahi

> **Javi:** "Compare pip, Python y paquetes por ruta."

> **la lider:** "Donde quedo instalado el paquete."

> **Javi:** "En el global, mientras el proyecto corre en el virtual."

> **Renata:** "Eso explica por que la salida parecia correcta al principio."

> **Javi:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="paquetes por ambiente">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">paquetes por ambiente</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="143" width="174" height="117" fill="#286d9b"/>
  <text x="157" y="133" font-size="18" text-anchor="middle">64</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">pip global</text>
  <rect x="272" y="85" width="174" height="175" fill="#d58b2f"/>
  <text x="359" y="75" font-size="18" text-anchor="middle">95</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">python -m pip</text>
  <rect x="474" y="190" width="174" height="70" fill="#4c8b63"/>
  <text x="561" y="180" font-size="18" text-anchor="middle">38</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">sin venv</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">Instalar y ejecutar deben apuntar al mismo entorno.</text>
</svg>

<!-- learning:pause -->
> **Renata:** "Por que conviene usar python -m pip dentro del entorno activo."

**Lo que muestra:** La evidencia muestra que pip y Python pueden apuntar a lugares distintos. Usar python -m pip amarra la instalacion al interprete que ejecuta el proyecto. El archivo de dependencias deja una receta repetible.

## Una puerta para instalar y correr

> **la lider:** "Instalamos desde el entorno activo y congelamos versiones."

> **la lider:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Ulises:** "El comando es mas largo."

> **Javi:** "Pero llega a la oficina correcta."

> **Ulises:** "Y si alguien pide excepcion."

> **Javi:** "Que la pida con costo visible y fecha."

> **la lider:** "Y si no hay evidencia, no hay lanzamiento."

> **Renata:** "Eso va a incomodar a la prisa."

> **Javi:** "La prisa ya nos estaba cobrando intereses."

> **Renata:** "Pip si trabajo; solo fue a la oficina equivocada."

**Regla:** instala dependencias desde el mismo Python que ejecuta el proyecto.
