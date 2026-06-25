# La rama que llego por WhatsApp

<!-- story
concept: branches, commits, issues y pull requests
characters: Mauro, Nelly, Isabel, el responsable
situation: un cambio de datos se comparte por chat en lugar de branch y pull request
bad_logic: mandar el archivo rapido equivale a colaborar
escalation: se pierde contexto, revision y motivo del cambio
data_turn: Nelly compara cambios enviados por chat contra cambios con pull request
chart: flujo branch PR
decision: abrir issue, trabajar en branch, explicar commit y revisar PR
punchline: La rama no venia en WhatsApp; venia un archivo con exceso de confianza.
rule: colaborar en GitHub significa dejar contexto revisable, no solo mandar archivos
synthetic_data: true
-->

## El archivo urgente

> **Mauro:** "Te mande el cambio por WhatsApp para avanzar."

> **Nelly:** "Me mandaste un archivo, no el motivo."

> **Isabel:** "El motivo era obvio."

> **Mauro:** "Entonces deberia caber en un issue."

> **Isabel:** "No queria hacer burocracia."

> **el responsable:** "La burocracia acaba de salvarnos de pisar produccion."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## El cambio sin pasaporte

> **Isabel:** "Lo pego directo en la rama principal."

> **Nelly:** "Sin revisar, sin prueba y sin rastro."

> **Isabel:** "Pero con palomita azul."

> **el responsable:** "La palomita no hace diff."

> **Isabel:** "El chat tiene fecha."

> **Mauro:** "No tiene prueba ni conversacion tecnica."

> **Nelly:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **el responsable:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## La revision necesita contexto

> **Mauro:** "Compare cambios por chat contra cambios por PR."

> **el responsable:** "Que informacion se pierde."

> **Mauro:** "Se pierde problema, revision, prueba y aprobacion."

> **Nelly:** "Eso explica por que la salida parecia correcta al principio."

> **Mauro:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="flujo branch PR">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">flujo branch PR</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="215" width="174" height="45" fill="#286d9b"/>
  <text x="157" y="205" font-size="18" text-anchor="middle">24</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">chat</text>
  <rect x="272" y="141" width="174" height="119" fill="#d58b2f"/>
  <text x="359" y="131" font-size="18" text-anchor="middle">63</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">branch</text>
  <rect x="474" y="85" width="174" height="175" fill="#4c8b63"/>
  <text x="561" y="75" font-size="18" text-anchor="middle">92</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">PR revisado</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">La revision vive en el flujo, no en el adjunto.</text>
</svg>

<!-- learning:pause -->
> **Nelly:** "Que aporta un pull request que no aporta mandar el archivo por mensaje."

**Lo que muestra:** El flujo muestra que issue, branch, commit y pull request guardan contexto. Permiten revisar diferencias, discutir decisiones, correr pruebas y dejar evidencia. El chat puede avisar, pero no reemplaza el proceso.

## Del chat al PR

> **el responsable:** "Todo cambio compartido entra por branch y PR."

> **el responsable:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Isabel:** "No habra atajos con archivo adjunto."

> **Mauro:** "Tampoco accidentes con confianza adjunta."

> **Isabel:** "Y si alguien pide excepcion."

> **Mauro:** "Que la pida con costo visible y fecha."

> **el responsable:** "Y si no hay evidencia, no hay lanzamiento."

> **Nelly:** "Eso va a incomodar a la prisa."

> **Mauro:** "La prisa ya nos estaba cobrando intereses."

> **Nelly:** "La rama no venia en WhatsApp; venia un archivo con exceso de confianza."

**Regla:** colaborar en GitHub significa dejar contexto revisable, no solo mandar archivos.
