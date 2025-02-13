# Reto 1.2: Exploración de la base de datos


**Dificultad:** 🌻


**Aprendizaje:** 🍯🍯


**Tiempo:** ⏱️️⏱️️⏱️️ 2-3 hrs.


**Reacciona** con 👀 cuando comiences la lectura y/o actividad.


---


## Meta de Aprendizaje
Desarrollarás habilidades para explorar y analizar una base de datos de marketing digital, identificando las principales métricas disponibles. Aprenderás a calcular números totales y segmentados por campaña, así como a visualizar los datos mediante gráficos para facilitar su interpretación.

## Descripción
Para darte un poco de contexto, en este proyecto trabajaremos con una base de datos real extraída del repositorio de datasets de Kaggle. Hemos realizado algunas modificaciones con fines didácticos. En esta base de datos podemos encontrar las siguientes variables:


1.) ad_id: Identificador único para cada anuncio (el ID del anuncio es único, pero la campaña puede haber sido anunciada varias veces).
2.) xyz_campaign_id: ID asociado a cada campaña publicitaria de la empresa XYZ.
3.) fb_campaign_id: ID utilizado por Facebook para rastrear cada campaña.
4.) age: Edad de la persona a la que se muestra el anuncio.
5.) gender: Género de la persona a la que se muestra el anuncio.
6.) interest: Código que especifica la categoría de interés del usuario (según su perfil público en Facebook).
7.) Impressions: Número de veces que se mostró el anuncio.
8.) Clicks: Número de clics recibidos por el anuncio.
9.) Spent: Monto pagado por la empresa XYZ a Facebook para mostrar el anuncio.
10.) Total conversion: Número total de personas que solicitaron información sobre el producto después de ver el anuncio.
11.) Approved conversion: Número total de personas que compraron el producto después de ver el anuncio.


Como ya estudiaste en el reto anterior, aquí tenemos las principales métricas que nos permitirán calcular algunos KPIs en los siguientes retos. Además, con el conocimiento adquirido hasta ahora, podemos comprender mejor el origen de los datos, como por ejemplo, cómo se extrajeron los datos de clics, cómo se identificó que cada campaña era distinta y cómo se pueden definir distintos "targets" para posteriormente analizar el comportamiento de cada perfil de cliente.


Teniendo esto en cuenta, exploraremos aún más la base de datos para conocer en detalle la información contenida en cada variable. Esto nos permitirá obtener un conocimiento profundo que será clave en los próximos retos. Comprender los datos disponibles y su origen es una parte fundamental del análisis de datos, ya que nos ayuda a realizar un mejor estudio y tomar decisiones más informadas.
Revisa los datos disponibles en la base de datos proporcionada en  "Insumos para tu aprendizaje" y responde a las siguientes preguntas:
- ¿Cuáles son los principales datos disponibles en la base de datos y qué representan?
- ¿Cómo se pueden calcular los números totales de anuncios, clics, impresiones, gasto y conversiones? 
- ¿Cómo se pueden segmentar los datos para obtener estos mismos indicadores por campaña? 
- ¿Cómo se pueden agrupar los anuncios por género, edad e intereses para un análisis más detallado? 
- ¿Qué tipo de gráficos pueden ayudar a visualizar mejor la información por género en términos de clics y conversiones?


### Cumples con la meta de aprendizaje si:
- [x] Identificas y describes correctamente los datos disponibles en la base de datos.
- [x] Eres capaz de calcular los números totales de las métricas clave.
- [x] Puedes agrupar y segmentar los datos por campaña, género, edad e intereses.
- [x] Creas gráficos adecuados que representen la información de manera clara y comprensible.

## Insumos para tu aprendizaje
📈[Base de datos](https://docs.google.com/spreadsheets/d/1WZQDO4b-CrXtiYbgGk__mcmtKofkP6q3_AuFcJ6xkcw/copy?)
*Haz una copia del dataset para comenzar tu análisis. Recuerda que debes estar registrada en tu cuenta de Google.
📺[Video: Tablas dinámicas](https://www.loom.com/share/5937ac5fb32c424285e952bc07097580?sid=44e51ec0-a90d-4657-ab8d-ed543513adff)
📄[Texto: Cómo crear y usar tablas dinámicas](https://support.google.com/docs/answer/1272900?sjid=13953989927308243057-EU)
📄 [Texto: Documentación Gráficos](https://support.google.com/docs/answer/63824?hl=es&co=GENIE.Platform%3DDesktop)
📄 [Texto: Artículo sobre gráficos de barras](https://tipshojasdecalculo.com/grafico-de-barras-en-google-sheets/)
📄 [Texto: Documentación tipos de gráficos](https://support.google.com/docs/answer/190718?hl=es-419)
📺 [Video: como crear y personalizar gráficos](https://www.youtube.com/watch?v=Ws2cTgMTPQE&t=17s)





## Pauta de Trabajo
- Revisa la base de datos para familiarizarte con las variables disponibles y su descripción.
- Calcula los números totales de anuncios, clics, impresiones, gasto y conversiones utilizando funciones de agregación como [SUM](https://support.google.com/docs/answer/3093669?hl=es-419) o a través de tablas dinámicas.
- Segmenta los datos por campaña para obtener los mismos indicadores desglosados según cada estrategia publicitaria. Utiliza tablas dinámicas para organizar la información, empleando el recurso ROW (fila) para agrupar los datos por filas y VALUE (valor) para realizar cálculos como sumas, promedios, entre otros.
- Agrega los datos por género, edad e intereses, y analiza si existen diferencias significativas en los resultados. Puedes utilizar COLUMN (columna) para agrupar por columnas y comparar, por ejemplo, los resultados de campaña frente a género..
- Crea gráficos (barras, líneas o tablas dinámicas) para otras segmentaciones relevantes.
- Interpreta los resultados y reflexiona sobre las informaciones que encontraste.

Tip: Usa herramientas como tablas dinámicas y gráficos en Google Sheets para facilitar la segmentación y el análisis de datos. Aquí dejamos un pequeño ejemplo de como puedes utilizar tablas dinámicas y gráficos para resumir informaciones.

![imagen1](https://drive.google.com/uc?id=1Rn6GuS28FmVbQr6AE_jwGQkJt4c31ahM)

![imagen2](https://drive.google.com/uc?id=1R18idIhUQgmmSN_JalgmS48A5KKOSA24xd)

---


¡Diviértete y disfruta del proceso de aprendizaje! Recuerda que sentirte confundido o desorientado es parte natural del proceso.