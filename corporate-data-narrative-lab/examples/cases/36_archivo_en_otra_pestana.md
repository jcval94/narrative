# El archivo que vivia en otra pestana

<!-- story
concept: rutas, montaje de Drive y carga de datos en Colab
characters: Vero, Hector, Nadia, el instructor
situation: un notebook usa un archivo abierto en otra sesion y no documenta como cargarlo
bad_logic: si el archivo se ve en el navegador, Python tambien sabe donde esta
escalation: cada estudiante sube datos con nombres distintos y aparecen resultados incompatibles
data_turn: Vero compara rutas usadas y numero de filas cargadas
chart: rutas y fuentes
decision: definir una sola ruta, validar columnas y mostrar conteo antes de analizar
punchline: El archivo estaba cerca visualmente, que es muy lejos para Python.
rule: antes de analizar, valida ruta, columnas y conteo de datos
synthetic_data: true
-->

## La pestana de al lado

> **Vero:** "El CSV esta abierto aqui junto al notebook."

> **Hector:** "Python no lee pestanas, lee rutas."

> **Nadia:** "Pero se ve clarito."

> **Vero:** "Se ve para ti, no para el runtime."

> **Nadia:** "Les dije que subieran el archivo."

> **el instructor:** "Cada quien subio uno con nombre diferente."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## Cada quien cargo su mundo

> **Nadia:** "Que cambien la ruta a mano."

> **Hector:** "Entonces cada resultado tendra una biografia distinta."

> **Nadia:** "Podemos decir que es aprendizaje personalizado."

> **el instructor:** "Uno cargo la muestra vieja y gano otra conclusion."

> **Nadia:** "Al menos todos hicieron analisis."

> **Vero:** "De archivos que no eran el mismo."

> **Hector:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **el instructor:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## La ruta tambien es dato

> **Vero:** "Liste rutas, columnas y filas cargadas."

> **el instructor:** "Cuantos analizaron la misma fuente."

> **Vero:** "Menos de los que creian."

> **Hector:** "Eso explica por que la salida parecia correcta al principio."

> **Vero:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="rutas y fuentes">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">rutas y fuentes</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="85" width="124" height="175" fill="#286d9b"/>
  <text x="132" y="75" font-size="18" text-anchor="middle">88</text>
  <text x="132" y="286" font-size="13" text-anchor="middle">ruta unica</text>
  <rect x="222" y="115" width="124" height="145" fill="#d58b2f"/>
  <text x="284" y="105" font-size="18" text-anchor="middle">73</text>
  <text x="284" y="286" font-size="13" text-anchor="middle">mismo conteo</text>
  <rect x="374" y="99" width="124" height="161" fill="#4c8b63"/>
  <text x="436" y="89" font-size="18" text-anchor="middle">81</text>
  <text x="436" y="286" font-size="13" text-anchor="middle">columnas ok</text>
  <rect x="526" y="203" width="124" height="57" fill="#c64e36"/>
  <text x="588" y="193" font-size="18" text-anchor="middle">29</text>
  <text x="588" y="286" font-size="13" text-anchor="middle">sin validar</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">La fuente debe comprobarse antes del analisis.</text>
</svg>

<!-- learning:pause -->
> **Hector:** "Que validaciones deben correr antes de confiar en una carga de datos en Colab."

**Lo que muestra:** La evidencia muestra rutas distintas y conteos distintos. Antes de graficar o modelar, conviene validar nombre de archivo, columnas esperadas, filas cargadas y fecha de fuente. La ruta es parte de la reproducibilidad.

## Leer antes de concluir

> **el instructor:** "El notebook descarga una fuente unica y valida esquema."

> **el instructor:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Nadia:** "Habra menos libertad creativa con nombres."

> **Vero:** "Y mas confianza en el resultado compartido."

> **Nadia:** "Y si alguien pide excepcion."

> **Vero:** "Que la pida con costo visible y fecha."

> **el instructor:** "Y si no hay evidencia, no hay lanzamiento."

> **Hector:** "Eso va a incomodar a la prisa."

> **Vero:** "La prisa ya nos estaba cobrando intereses."

> **Hector:** "El archivo estaba cerca visualmente, que es muy lejos para Python."

**Regla:** antes de analizar, valida ruta, columnas y conteo de datos.
