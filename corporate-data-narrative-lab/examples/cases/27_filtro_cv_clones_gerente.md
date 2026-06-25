# El filtro que contrataba clones del gerente

<!-- story
concept: sesgo en datos historicos y decisiones automatizadas
characters: Ana, Pablo, Lorena, el gerente
situation: un filtro de CV aprende del historial de contrataciones de un area poco diversa
bad_logic: si los mejores empleados historicos se parecen, el modelo debe buscar perfiles parecidos
escalation: candidatos capaces quedan abajo por no parecerse al patron anterior
data_turn: Ana compara seleccion por experiencia real y por parecido historico
chart: seleccion por grupo
decision: auditar sesgos, quitar proxies y mantener revision humana
punchline: El modelo no buscaba talento; buscaba al gerente con otro correo.
rule: un modelo entrenado con historia injusta puede repetirla con mejor velocidad
synthetic_data: true
-->

## La terna perfecta

> **Ana:** "El filtro ya nos deja ternas muy parecidas al equipo actual."

> **Pablo:** "Esa frase no suena tan bien como crees."

> **Lorena:** "El equipo actual funciona."

> **Ana:** "Tambien es resultado de decisiones viejas."

> **Lorena:** "El modelo aprendio de los mejores."

> **el gerente:** "Aprendio de quienes tuvieron oportunidad."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## Parecido no era desempeno

> **Lorena:** "Podemos subir el corte para asegurar calidad."

> **Pablo:** "Eso haria mas fuerte el mismo sesgo."

> **Lorena:** "Pero la terna tendria mucha afinidad cultural."

> **el gerente:** "Afinidad se parece demasiado a estudiaste donde yo."

> **Lorena:** "No descarta por grupo, descarta por senales."

> **Ana:** "Algunas senales son el grupo con bigote falso."

> **Pablo:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **el gerente:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## El historial tenia memoria selectiva

> **Ana:** "Revise seleccion controlando experiencia y prueba tecnica."

> **el gerente:** "Quien baja aunque tenga buen resultado."

> **Ana:** "Los perfiles no historicos caen mas aun con desempeno similar."

> **Pablo:** "Eso explica por que la salida parecia correcta al principio."

> **Ana:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="seleccion por grupo">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">seleccion por grupo</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="85" width="174" height="175" fill="#286d9b"/>
  <text x="157" y="75" font-size="18" text-anchor="middle">76</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">historico</text>
  <rect x="272" y="187" width="174" height="73" fill="#d58b2f"/>
  <text x="359" y="177" font-size="18" text-anchor="middle">32</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">no historico</text>
  <rect x="474" y="120" width="174" height="140" fill="#4c8b63"/>
  <text x="561" y="110" font-size="18" text-anchor="middle">61</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">con revision</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">La revision reduce el castigo a perfiles distintos.</text>
</svg>

<!-- learning:pause -->
> **Pablo:** "Por que una variable aparentemente neutral puede copiar una exclusion pasada."

**Lo que muestra:** La grafica muestra seleccion desigual entre perfiles con resultados comparables. El modelo no necesita usar una categoria sensible para sesgar; puede usar escuela, colonia, trayectoria o huecos como proxies. Por eso hace falta auditoria y revision humana.

## Revisar antes de descartar

> **el gerente:** "El filtro deja de descartar solo y pasa a priorizar revision."

> **el gerente:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Lorena:** "RH leera mas candidatos."

> **Ana:** "Y menos copias del mismo pasado."

> **Lorena:** "Y si alguien pide excepcion."

> **Ana:** "Que la pida con costo visible y fecha."

> **el gerente:** "Y si no hay evidencia, no hay lanzamiento."

> **Pablo:** "Eso va a incomodar a la prisa."

> **Ana:** "La prisa ya nos estaba cobrando intereses."

> **Pablo:** "El modelo no buscaba talento; buscaba al gerente con otro correo."

**Regla:** un modelo entrenado con historia injusta puede repetirla con mejor velocidad.
