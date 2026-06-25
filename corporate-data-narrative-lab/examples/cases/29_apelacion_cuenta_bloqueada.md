# La apelacion que pedia entrar a la cuenta bloqueada

<!-- story
concept: apelacion y gobernanza de decisiones automatizadas
characters: Rocio, Ivan, Teresa, el director
situation: un flujo automatico bloquea cuentas y solo permite apelar desde la cuenta bloqueada
bad_logic: si el sistema ya decidio, el usuario puede resolver todo por autoservicio
escalation: las personas afectadas no pueden ver motivo ni presentar evidencia
data_turn: Rocio dibuja el flujo de bloqueo, notificacion y apelacion
chart: flujo de apelacion
decision: abrir canal externo, mostrar motivo y registrar revision
punchline: La apelacion existia; estaba guardada detras de la puerta cerrada.
rule: toda decision automatizada de alto impacto necesita explicacion y via real de apelacion
synthetic_data: true
-->

## El canal autoservicio

> **Rocio:** "El flujo ya tiene boton de apelacion."

> **Ivan:** "El boton aparece despues de iniciar sesion."

> **Teresa:** "Eso protege datos del usuario."

> **Rocio:** "Tambien protege al bloqueo de ser revisado."

> **Teresa:** "No queriamos abrir canales inseguros."

> **el director:** "Abrimos un laberinto seguro."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## La llave adentro del cuarto

> **Teresa:** "Que llamen al centro de ayuda."

> **Ivan:** "El centro pide validar en la cuenta."

> **Teresa:** "Entonces si son ellos, podran entrar."

> **el director:** "No pueden, porque por eso llaman."

> **Teresa:** "El sistema cierra el caso por falta de respuesta."

> **Rocio:** "Respuesta que encerramos con el caso."

> **Ivan:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **el director:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## El flujo se mordia la cola

> **Rocio:** "Dibuje el recorrido desde bloqueo hasta apelacion."

> **el director:** "Donde se atoran las personas."

> **Rocio:** "En el mismo paso que exige acceso negado."

> **Ivan:** "Eso explica por que la salida parecia correcta al principio."

> **Rocio:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="flujo de apelacion">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">flujo de apelacion</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="85" width="124" height="175" fill="#286d9b"/>
  <text x="132" y="75" font-size="18" text-anchor="middle">84</text>
  <text x="132" y="286" font-size="13" text-anchor="middle">notificados</text>
  <rect x="222" y="196" width="124" height="64" fill="#d58b2f"/>
  <text x="284" y="186" font-size="18" text-anchor="middle">31</text>
  <text x="284" y="286" font-size="13" text-anchor="middle">entienden motivo</text>
  <rect x="374" y="223" width="124" height="37" fill="#4c8b63"/>
  <text x="436" y="213" font-size="18" text-anchor="middle">18</text>
  <text x="436" y="286" font-size="13" text-anchor="middle">pueden apelar</text>
  <rect x="526" y="96" width="124" height="164" fill="#c64e36"/>
  <text x="588" y="86" font-size="18" text-anchor="middle">79</text>
  <text x="588" y="286" font-size="13" text-anchor="middle">canal externo</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">La via real de apelacion no puede depender de acceso bloqueado.</text>
</svg>

<!-- learning:pause -->
> **Ivan:** "Cuando una decision automatica afecta a alguien, que debe existir fuera del sistema que lo bloqueo."

**Lo que muestra:** El flujo muestra un ciclo imposible: el usuario necesita entrar para apelar, pero la decision le impide entrar. Una apelacion real requiere canal alterno, motivo comprensible, evidencia recibida y revision registrada.

## Apelar desde afuera

> **el director:** "Abrimos apelacion externa con motivo y folio visible."

> **el director:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Teresa:** "Habra mas casos para revisar."

> **Rocio:** "Al menos seran casos que pueden entrar por la puerta."

> **Teresa:** "Y si alguien pide excepcion."

> **Rocio:** "Que la pida con costo visible y fecha."

> **el director:** "Y si no hay evidencia, no hay lanzamiento."

> **Ivan:** "Eso va a incomodar a la prisa."

> **Rocio:** "La prisa ya nos estaba cobrando intereses."

> **Ivan:** "La apelacion existia; estaba guardada detras de la puerta cerrada."

**Regla:** toda decision automatizada de alto impacto necesita explicacion y via real de apelacion.
