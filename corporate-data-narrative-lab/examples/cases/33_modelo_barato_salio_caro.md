# El modelo barato que salio caro

<!-- story
concept: costo de error y metrica de negocio
characters: Emilia, Raul, Berta, la CFO
situation: un modelo barato tiene precision aceptable pero falla en casos de alto costo
bad_logic: si dos modelos tienen precision parecida, gana el mas barato
escalation: se ahorra en computo y se pierde mas por errores caros
data_turn: Emilia compara costo total de errores y operacion
chart: costo por error
decision: elegir modelo por costo esperado y no solo por costo de ejecucion
punchline: Ahorramos en el modelo y pagamos la factura en los errores.
rule: la metrica correcta incluye el costo de equivocarse
synthetic_data: true
-->

## La opcion economica

> **Emilia:** "El modelo ligero cuesta menos y acierta casi igual."

> **Raul:** "Casi igual en casos, no en dinero."

> **Berta:** "La precision se ve muy cercana."

> **Emilia:** "Cuanto cuesta cuando se equivoca."

> **Berta:** "El presupuesto de tecnologia baja bastante."

> **la CFO:** "El presupuesto de reclamos sube con ganas."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## El ahorro encontro otro recibo

> **Berta:** "Tomemos el barato y monitoreamos."

> **Raul:** "Monitorear perdidas no las vuelve descuento."

> **Berta:** "Pero la factura del proveedor se vera preciosa."

> **la CFO:** "La del cliente afectado no."

> **Berta:** "Podemos aceptar algunos errores."

> **Emilia:** "Aceptemos primero saber cuales."

> **Raul:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **la CFO:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## No todos los errores cuestan igual

> **Emilia:** "Multiplique errores por costo de negocio."

> **la CFO:** "Que modelo sale barato despues del dano."

> **Emilia:** "El caro en computo cuesta menos al final."

> **Raul:** "Eso explica por que la salida parecia correcta al principio."

> **Emilia:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="costo por error">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">costo por error</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="85" width="174" height="175" fill="#286d9b"/>
  <text x="157" y="75" font-size="18" text-anchor="middle">78</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">modelo barato</text>
  <rect x="272" y="164" width="174" height="96" fill="#d58b2f"/>
  <text x="359" y="154" font-size="18" text-anchor="middle">43</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">modelo robusto</text>
  <rect x="474" y="234" width="174" height="26" fill="#4c8b63"/>
  <text x="561" y="224" font-size="18" text-anchor="middle">12</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">solo computo</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">El costo total cambia la decision.</text>
</svg>

<!-- learning:pause -->
> **Raul:** "Que metrica falta cuando comparamos modelos solo por precision y precio de ejecucion."

**Lo que muestra:** La grafica muestra que errores raros pueden concentrar mucho costo. La precision trata errores como iguales, pero el negocio no. La comparacion debe incluir costo esperado, volumen, impacto y capacidad de corregir.

## Barato despues de sumar

> **la CFO:** "Elegimos por costo total esperado."

> **la CFO:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Berta:** "La factura tecnica sube."

> **Emilia:** "La factura completa baja."

> **Berta:** "Y si alguien pide excepcion."

> **Emilia:** "Que la pida con costo visible y fecha."

> **la CFO:** "Y si no hay evidencia, no hay lanzamiento."

> **Raul:** "Eso va a incomodar a la prisa."

> **Emilia:** "La prisa ya nos estaba cobrando intereses."

> **Raul:** "Ahorramos en el modelo y pagamos la factura en los errores."

**Regla:** la metrica correcta incluye el costo de equivocarse.
