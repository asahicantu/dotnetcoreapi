# Análisis de requerimientos:
 Todo nace de un disparador que nos crea la necesidad de crear un artefacto o un sistema. Necesitamos entender cuál es el problema que queremos resolver. Hay requerimientos de negocio, requerimientos funcionales, requerimientos no funcionales.

# Diseño de la solución:
 Análisis profundo de los problemas para trabajar en conjunto y plantear posibles soluciones. 
El resultado de esto debe ser el detalle de la solución, a través de requerimientos, modelado, etc.
Importante en el método tradicional
Desarrollo y evolución: Implementación de la solución, para garantizar que lo que se esta construyendo es lo que se espera. Al finalizar esta etapa tendremos un artefacto de software.
Despliegue: Infraestructura / roles de operación para poder poner el artefacto a disponibilidad.
Mantenimiento y evolución: Desarrollo + despliegue + mantenimiento, mejoras al sistema. El software se mantiene hasta que deja de ser necesario.


# Dificultades

# Esenciales: Los podemos dividir en 4.
	• Complejidad:  No Desarrollar
	• La conformidad (Contexto, prerequerimientos y limitaciones) Prototipado rpaido
	• Tolerancia al cambio Desarrollo evolutivo
	• Invisibilidad (Abstraccion , dificultad para visalizar su forma) Grandes disenadores
# Accidentales:
	• Plataforma a implementar, tecnología, lenguajes, frameworks, integraciones, etc.\

 * There is no silver bullet - 

No hay bala de plata que solucione el problema esencial del software.

Problema accidental a resolver <> Problema esencial

Roles <> Puesto de trabajo
Rol	Tradicioal	Metodologias agiles (Equipo autogestionado)
Experto del dominio	Subjet matter expert	StakeHolder
Analista	Define requerimientos Analisis completo y detallado	Duenio del producto (Cliente)
Administrador de sistemas	SysAdmin (Servers, SO, Error log)	DevOps (Operaciones y desarrollo)  /SRE Site reliability engineer
Desarrollo	QA/Testing Devs / Arquitecto	Equipo de desarrollo holistico
Gestor de proyecto		Facilitador SCRUM Master


Arquitecturas
FLUX, Sistemas, Disponibilidad, servidores, etc
Ley de Conway - Comunicacion distribuida, una empresa genera vias  de comunicacion a fines a su propia organizacion

Arquitecto: Conecta los stakeholder con el sistema a construir. Cada uno de los roles que tienen los SH afectan de diferente forma el sistema
> 
Metodologia tradicional:
Diseno [No hay feedback]

Metoologias agiles
Momentos para reevaluar |El planear los momentos importantes o el ultimo momento responsible - Obtener feedback



Entender el problema
Requerimientos del producto Negocio, usuario guncionales
Funcionales y no funcionales (Maa globales, )
Requerimientos significativos de la arquitectura

Riesgos: Encontrary resolver. Identificar : Requerimientos-> Dificultad/complejidad, atribuos de calidad-> Incertidumbre, concoimientos del dominio->Riesgo prototipico.
Priorizar riesgos

Restricciones: Limitaciones de diseno o implementacion del desarrollado / Ecosistema, regulaciones, infraestructura, ecosistema,

Requerimientos de proyecto 

Arquitecturas: 
Microarquitecturas relativas a frameworks
Microservicios 
Necesitan analisis profundo NO SILVER BULLET -> BENEFICIOS Y CONSECUENCIAS
Estilo de arquitectura -> Problema a resolver arquitectonicamente

Llamado y retorno	Programa principal y sub rutinas
	POO
	Multinivel (Cliente/Servidor)
	
Flujos de datos	Lote secuencial | Texto, archios | BD
	Tubos y filtros [Linux pipes]
Centrada en datos	Pizaarron Componentes interactuan con componente central (Salida) Sistema fiscales
	Base de datos (Internet app)
	Sistema experto / Basado en reglas KB (Knowledge base)
Componentes independientes	Bajo acoplamiento
	Invocacion implicita
	Invocacion explicita
	Orientado a eventos
	Orientado a servicios
	Publicas suscribir
	ESB Enterprise service bus

Arquitectura monolitica: Eficiencia, Facil de probar, curva de aprendizaje, dificil de modificar
Arquitectura distribuido Modularidad, disponibilidad, uso de recursos, adaptabilidad









En el contexto de metodologías ágiles, ¿dónde encontraremos el rol del arquitecto? | Equipo de desarrollo

En los frameworks web modernos existe el concepto de middleware, que describe una forma de interceptar el pedido o la respuesta del sistema con componentes desarrollados independientes uno del otro. ¿Qué estilo de arquitectura están implementando? | Pizarron

“Toda interacción con el sistema debe ser compatible con usuarios con discapacidad visual.” ¿Qué tipo de requerimiento es? | No funcional

“El sistema deberá estar disponible para ser presentado en la conferencia de la empresa en abril de este año.” ¿Qué tipo de requerimiento es? | De Proyecto

Y en el contexto de metodologías ágiles, ¿cuándo se toman las decisiones de arquitectura? " En  cada iteracion

¿Cuál de los siguientes mejor describe el objetivo de un arquitecto? | Comprender las necesidaded de sus stakeholders al disenar el sistema

Una librería desarrolló un sistema para administrar su venta y existencia de libros. Diez años más tarde, la empresa cuenta con más de 800 librerías distribuidas en 30 países de américa y europa. El sistema de administración de ventas y existencia se sigue usando para cada librería, mientras que muchos otros sistemas se encargan de la gestión global de la compañía, sus métricas por región y su expansión. ¿Qué estilo de arquitectura estamos describiendo? | Oriendato a servicios

¿Cuáles de estas puede ser considerada una restricción de diseño? | El sistema debe estar disponible 99.99% del tiempo

La empresa GitJam es una organización multinacional con desarrolladores distribuidos en todo el mundo. Su metodología de trabajo es principalmente remoto: No tienen oficina más allá de un pequeño headquarters en San Francisco, donde se reúnen los directivos. Los desarrolladores se comunican por email y disponen de una plataforma de chat. ¿cómo es el diseño de su sistema? | Distribuido, asincrono

En el contexto de metodologías tradicionales, ¿en qué etapa del proceso de desarrollo de software se toman las decisiones de arquitectura? | Diseno de la solucion

En un centro de investigación, científicos de diferentes áreas utilizan un sistema para, a través de un modelo común de física, química y biología, simular hipótesis de procesos que se podrían haber dado durante la historia de nuestro planeta. Para esto, le deben describir al sistema los hechos que forman parte de su hipótesis y luego consultar el resultado simulado. ¿Qué estilo de arquitectura usará el sistema? | Experto basado en reglas

El usuario podrá comprar con tarjeta de crédito a través del sistema, ¿qué tipo de requerimiento es? | Funcional

¿Por qué no podemos resolver todos los riesgos detectados?  | Dedicamos esfyerzo a atacarlos y no a desarrollar el trabaho

“El sistema podría ser atacado a través de una denegación distribuida de servicio.” ¿Qué describe esto? |  Riesgo

¿Cuál de estas definiciones mejor describe la arquitectura de software? | Es la estructura de un sistema, sus interconexiones, y las decisiones de diseño que llevaron a éstas

De los siguientes estilos, ¿cuál es que más se usa al desarrollar aplicaciones web? | Cliente/Servidor

¿Cuál de estas prácticas es esencial para un arquitecto en contexto de metodologías ágiles?  | Reevaluar la arquitectura en cada iteración a través de métricas y alertas

En la compañía ACME-Products quieren comenzar un nuevo producto, capaz de analizar datos de compras y comportamiento de compradores en tiempo real. En una conversación sobre requerimientos, el dueño del producto le comunica al arquitecto que deben usar la base de datos GuayabaDB, ya que tienen un acuerdo previo con la compañía que la desarrolla. ¿Qué es esto?   | REstriccion de diseno

“Los precios podrán ser actualizados desde un panel de administración.” ¿Qué tipo de requerimiento es? | Funcional

Luego de identificar los riesgos, ¿qué hace el arquitecto con esta información? | Prioriza para resolver los importantesoo
        