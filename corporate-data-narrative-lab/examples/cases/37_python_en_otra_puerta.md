# El Python correcto estaba en otra puerta

<!-- story
concept: interpretes de Python en VS Code
characters: Caro, Benja, Diana, el mentor
situation: VS Code ejecuta un interprete distinto al que el equipo configuro
bad_logic: si el archivo se abre en VS Code, se ejecuta con el entorno correcto
escalation: el codigo falla para unos y para otros usa paquetes viejos
data_turn: Caro muestra ruta de interprete, version y paquetes instalados
chart: rutas de interprete
decision: seleccionar interprete del proyecto y documentar activacion del entorno
punchline: No habia dos proyectos; habia dos Pythons peleando por el teclado.
rule: en VS Code, confirma el interprete antes de culpar al codigo
synthetic_data: true
-->

## El mismo archivo

> **Caro:** "El script corre en mi VS Code y falla en el tuyo."

> **Benja:** "Tu VS Code esta usando otro Python."

> **Diana:** "Pero abrimos la misma carpeta."

> **Caro:** "Abrir carpeta no elige interprete."

> **Diana:** "Abajo dice Python, eso cuenta."

> **el mentor:** "Cuenta como pista, no como garantia."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## La puerta equivocada

> **Diana:** "Reinstalamos todos los paquetes."

> **Benja:** "Primero veamos donde los instalarias."

> **Diana:** "En el Python que aparezca mas cerca."

> **el mentor:** "Asi terminamos con paquetes en tres lugares."

> **Diana:** "Al menos alguno debe funcionar."

> **Caro:** "Ese no es un plan, es una rifa."

> **Benja:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **el mentor:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## Ruta mata sospecha

> **Caro:** "Imprimi ruta, version y ubicacion de paquetes."

> **el mentor:** "Cual Python esta ejecutando el proyecto."

> **Caro:** "El editor apuntaba al global, no al entorno virtual."

> **Benja:** "Eso explica por que la salida parecia correcta al principio."

> **Caro:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="rutas de interprete">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">rutas de interprete</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="183" width="174" height="77" fill="#286d9b"/>
  <text x="157" y="173" font-size="18" text-anchor="middle">41</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">global</text>
  <rect x="272" y="85" width="174" height="175" fill="#d58b2f"/>
  <text x="359" y="75" font-size="18" text-anchor="middle">93</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">venv</text>
  <rect x="474" y="210" width="174" height="50" fill="#4c8b63"/>
  <text x="561" y="200" font-size="18" text-anchor="middle">27</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">conda viejo</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">La ruta del interprete explica diferencias de ejecucion.</text>
</svg>

<!-- learning:pause -->
> **Benja:** "Que informacion confirma que VS Code usa el mismo entorno que el proyecto."

**Lo que muestra:** La grafica compara interpretes globales y virtuales. La ruta del ejecutable, version y lista de paquetes deben coincidir con el proyecto. Seleccionar interprete evita instalar dependencias en el lugar equivocado.

## Un proyecto, un interprete

> **el mentor:** "Fijamos el interprete del entorno virtual en el proyecto."

> **el mentor:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Diana:** "Hay que mirar una configuracion mas."

> **Caro:** "Y dejamos de perseguir errores imaginarios."

> **Diana:** "Y si alguien pide excepcion."

> **Caro:** "Que la pida con costo visible y fecha."

> **el mentor:** "Y si no hay evidencia, no hay lanzamiento."

> **Benja:** "Eso va a incomodar a la prisa."

> **Caro:** "La prisa ya nos estaba cobrando intereses."

> **Benja:** "No habia dos proyectos; habia dos Pythons peleando por el teclado."

**Regla:** en VS Code, confirma el interprete antes de culpar al codigo.
