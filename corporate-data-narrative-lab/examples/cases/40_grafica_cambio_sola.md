# La grafica que cambio sola

<!-- story
concept: diferencias reproducibles en codigo y datos
characters: Noe, Sara, Miguel, la gerente
situation: una grafica cambia porque el dato fuente se actualizo sin registro
bad_logic: si el codigo no cambio, el resultado debe ser el mismo
escalation: se discute el analisis sin saber que tabla alimento cada version
data_turn: Sara compara hash de datos, fecha de extraccion y commit de codigo
chart: diff de datos y codigo
decision: registrar versiones de datos y parametros junto con cada salida
punchline: La grafica no cambio sola; solo fue mas discreta que nosotros.
rule: para reproducir un analisis versiona codigo, datos y parametros
synthetic_data: true
-->

## El mismo notebook

> **Noe:** "La grafica de hoy no coincide con la de ayer."

> **Sara:** "El codigo no cambio."

> **Miguel:** "Entonces alguien movio una formula."

> **Noe:** "O cambio el dato de entrada."

> **Miguel:** "La consulta jala lo mas reciente."

> **la gerente:** "Eso es comodo y peligrosamente silencioso."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## El dato se movio sin hacer ruido

> **Miguel:** "Ponemos una nota de actualizado."

> **Sara:** "La nota no dice que filas cambiaron."

> **Miguel:** "Podemos jurar que corrimos lo mismo."

> **la gerente:** "Corrimos lo mismo contra otro mundo."

> **Miguel:** "El numero nuevo se ve mejor."

> **Noe:** "No confundamos mejora con actualizacion."

> **Sara:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **la gerente:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## Tres huellas para una grafica

> **Noe:** "Compare codigo, parametros y fuente usada."

> **la gerente:** "Que huella cambio entre salidas."

> **Noe:** "El commit era igual; el corte de datos no."

> **Sara:** "Eso explica por que la salida parecia correcta al principio."

> **Noe:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="diff de datos y codigo">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">diff de datos y codigo</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="242" width="174" height="18" fill="#286d9b"/>
  <text x="157" y="232" font-size="18" text-anchor="middle">0</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">codigo</text>
  <rect x="272" y="85" width="174" height="175" fill="#d58b2f"/>
  <text x="359" y="75" font-size="18" text-anchor="middle">63</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">datos</text>
  <rect x="474" y="227" width="174" height="33" fill="#4c8b63"/>
  <text x="561" y="217" font-size="18" text-anchor="middle">12</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">parametros</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">El cambio principal venia de los datos fuente.</text>
</svg>

<!-- learning:pause -->
> **Sara:** "Que piezas deben guardarse para reproducir una grafica de negocio."

**Lo que muestra:** La evidencia separa tres fuentes de cambio: codigo, parametros y datos. Si solo se versiona el notebook, una actualizacion de fuente puede cambiar resultados sin explicacion. Cada salida debe guardar corte o identificador de datos.

## La salida lleva acta

> **la gerente:** "Cada grafica guardara commit, fecha de datos y parametros."

> **la gerente:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Miguel:** "La carpeta de salidas tendra mas metadata."

> **Noe:** "Y menos misterio."

> **Miguel:** "Y si alguien pide excepcion."

> **Noe:** "Que la pida con costo visible y fecha."

> **la gerente:** "Y si no hay evidencia, no hay lanzamiento."

> **Sara:** "Eso va a incomodar a la prisa."

> **Noe:** "La prisa ya nos estaba cobrando intereses."

> **Sara:** "La grafica no cambio sola; solo fue mas discreta que nosotros."

**Regla:** para reproducir un analisis versiona codigo, datos y parametros.
