
document.addEventListener("DOMContentLoaded", function () {
    const consejosContainer = document.getElementById("consejos");
    const previousPage = document.getElementById("previousPage");
    const nextPage = document.getElementById("nextPage");

    // Datos de ejemplo de consejos (títulos, imágenes, contenido, etc.)
    const consejosData = [
        {
            title1: "Cómo Conseguir un Pollo Asado Jugoso",
            title2: "Consejo para asar un pollo perfecto y jugoso",
            subtitle:"Preparación y técnica de cocción",
            imageUrl: "https://images.pexels.com/photos/2338407/pexels-photo-2338407.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Pollo",
            content: "Para lograr un pollo asado sumamente jugoso y lleno de sabor, es crucial dedicar tiempo a una marinada adecuada. Esto no solo infunde los sabores, sino que también ayuda a mantener la humedad durante la cocción. Opta por una marinada simple pero efectiva que combine aceite de oliva virgen extra, jugo fresco de limón, ajo picado finamente y una selección de hierbas frescas como romero, tomillo y perejil. Asegúrate de que el pollo esté completamente cubierto por la marinada y déjalo reposar en el refrigerador durante al menos varias horas, o idealmente durante la noche, para obtener los mejores resultados. <br><br> Cuando sea el momento de asar, precalienta tu horno o parrilla a una temperatura alta para comenzar el proceso de dorado. Esto no solo mejora la apariencia del pollo al crear una piel crujiente y dorada, sino que también sella los jugos en el interior. Después de unos minutos, reduce el calor a una temperatura media y continúa cocinando el pollo de manera lenta y constante. Utiliza un termómetro de cocina para asegurarte de que el pollo alcance una temperatura interna de al menos 75°C en la parte más gruesa de la carne. <br><br> Una vez que el pollo esté perfectamente cocido, retíralo del calor y deja que descanse durante unos minutos antes de cortarlo. Este paso crucial permite que los jugos naturales se redistribuyan por toda la carne, asegurando que cada bocado esté lleno de sabor y suculencia. Al seguir estos pasos, estarás en camino de servir un pollo asado que no solo impresionará por su sabor, sino también por su jugosidad incomparable."
        },
        {
            title1: "Cómo Elegir y Preparar Cortes de Carne para una Parrillada Perfecta",
            title2: "Selección y Preparación de Carnes para Parrilladas",
            subtitle: "Consejos para asegurar carnes jugosas y bien cocidas en la parrilla",
            imageUrl: "https://images.pexels.com/photos/410648/pexels-photo-410648.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Parrillada",
            content: "Para lograr una carne asada exquisitamente jugosa y sabrosa, es fundamental seleccionar cortes que presenten un abundante marmoleo de grasa. Esta grasa intramuscular no solo aporta sabor, sino que también ayuda a mantener la carne húmeda durante el proceso de cocción. Antes de colocar la carne sobre la parrilla caliente, sazónala generosamente con sal gruesa y pimienta recién molida para realzar sus sabores naturales. <br><br> Comienza la cocción a fuego medio-alto para sellar los jugos y caramelizar los bordes, creando una deliciosa costra dorada. Este paso inicial es crucial para atrapar los jugos dentro de la carne. Luego, ajusta el fuego a medio para permitir una cocción más gradual y uniforme, asegurando que la carne se cocine al punto exacto que prefieras. Utiliza un termómetro de cocina para monitorear la temperatura interna y lograr el término deseado, ya sea jugoso y rojo por dentro (punto rojo) o bien cocido (bien hecho). <br><br> Este método de cocción no solo optimiza la textura y la jugosidad de la carne, sino que también resalta su sabor natural, proporcionando una experiencia culinaria deliciosa y satisfactoria en cada porción. Al seguir estos pasos, te asegurarás de servir una carne perfectamente cocinada que impresionará a tus invitados y elevará cualquier comida a un nivel superior de disfrute gastronómico."
        },
        {
            title1: "Cómo Eliminar el Olor a Ajo de tus Manos",
            title2: "Consejos para Deshacerte del Olor a Ajo",
            subtitle: "Técnicas efectivas para neutralizar olores persistentes",
            content: "Después de manipular ajo, es común que el fuerte aroma persista en tus manos incluso después de lavarlas con agua y jabón. Para eliminar este olor de manera efectiva, puedes utilizar un truco casero probado: frota tus manos con utensilios de acero inoxidable, como una cuchara, bajo agua corriente fría durante unos segundos. El acero inoxidable tiene la propiedad de neutralizar los compuestos de azufre presentes en el ajo, que son los responsables del olor persistente. Esta reacción química ayuda a eliminar el aroma de manera eficiente y sin necesidad de productos químicos adicionales. <br><br>Además de ser efectivo, este método es fácil de realizar en casa y no requiere mucho tiempo. Después de frotar las manos con el utensilio de acero inoxidable, simplemente enjuágalas con agua y jabón para asegurarte de que queden completamente limpias y frescas. Así, podrás eliminar por completo el olor del ajo y sentirte cómodo/a al continuar con tus actividades diarias.",
            imageUrl: "https://images.pexels.com/photos/6576763/pexels-photo-6576763.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Manos lavándose",
        },
        {
            title1: "Cómo Conservar los Alimentos Frescos",
            title2: "Consejos para Mantener los Alimentos Frescos",
            subtitle: "Técnicas efectivas para prolongar la frescura de tus alimentos",
            imageUrl: "https://images.pexels.com/photos/2128535/pexels-photo-2128535.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Pan fresco",
            content: "Para asegurar que tu pan se mantenga fresco y delicioso por más tiempo, es importante almacenarlo correctamente. Guarda el pan en una bolsa de tela transpirable o en una caja de pan con buena ventilación. Estas opciones permiten que el pan respire, evitando la acumulación de humedad que puede provocar moho. Es fundamental evitar guardar el pan en el refrigerador, ya que las bajas temperaturas aceleran el proceso de desecación, haciendo que el pan se endurezca rápidamente y pierda su textura suave. <br><br> Si te encuentras con una cantidad excesiva de pan, considera congelarlo en porciones adecuadas para su uso posterior. Al congelar, envuelve cada porción de manera individual en papel film o bolsas herméticas para protegerlo de las quemaduras por congelación. Cuando necesites utilizar el pan, simplemente descongélalo a temperatura ambiente o en un horno a baja temperatura para recuperar su frescura. Este método asegura que puedas disfrutar de pan fresco durante más tiempo, sin necesidad de desperdiciar nada."
        },
        {
            title1: "Cómo Hacer que las Frutas Maduren Más Rápido",
            title2: "Consejos para Acelerar la Maduración de las Frutas",
            subtitle: "Utiliza el poder del etileno para madurar tus frutas más rápido",
            imageUrl: "https://images.pexels.com/photos/1300975/pexels-photo-1300975.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Frutas maduras",
            content: "Para acelerar la maduración de tus frutas, utiliza un método sencillo y eficaz: colócalas en una bolsa de papel junto con una manzana o un plátano. Estos frutos emiten etileno, un gas natural que actúa como una hormona vegetal, acelerando el proceso de maduración. Al encerrarlos en una bolsa de papel, el etileno se concentra alrededor de las frutas, promoviendo una maduración más rápida y uniforme.<br><br> Asegúrate de mantener la bolsa bien cerrada y a temperatura ambiente. Revisa el contenido diariamente para monitorear el progreso y evitar que las frutas se sobremaduren. En pocos días, tendrás frutas perfectamente maduras y listas para disfrutar. <br><br> Este método no solo es práctico y económico, sino que también te permite controlar el proceso de maduración según tus necesidades, garantizando que siempre tengas frutas en su punto óptimo de sabor y textura."
        },
        {
            title1: "Cómo Preparar el Arroz Perfecto",
            title2: "Secretos para Cocinar el Arroz de Manera Impecable",
            subtitle: "Pasos precisos para lograr un arroz cocido a la perfección",
            imageUrl: "https://images.pexels.com/photos/1717821/pexels-photo-1717821.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Arroz cocinado",
            content: "Para lograr un arroz perfectamente cocido y delicioso, es esencial seguir algunos pasos clave que aseguran la textura y el sabor ideales. Comienza por medir con precisión una proporción de 1 parte de arroz a 2 partes de agua. Este equilibrio es fundamental para que el arroz absorba la cantidad adecuada de agua sin quedar ni demasiado húmedo ni demasiado seco. <br><br> Antes de cocinar, es recomendable lavar el arroz bajo agua fría. Este paso ayuda a eliminar el exceso de almidón que puede hacer que el arroz quede pegajoso. Coloca el arroz en un colador fino y enjuágalo con agua corriente hasta que el agua salga clara. Este proceso no solo mejora la textura del arroz, sino que también lo hace más saludable al reducir su contenido de almidón. <br><br> Una vez lavado, coloca el arroz y el agua en una olla con tapa. Lleva la mezcla a ebullición a fuego medio-alto. Cuando comience a hervir, reduce el fuego a medio-bajo, tapa la olla y deja que el arroz se cocine lentamente. Este paso suele tomar entre 15 y 20 minutos, dependiendo del tipo de arroz y la altitud de tu ubicación. Es importante no destapar la olla durante este tiempo, ya que el vapor atrapado es crucial para la cocción uniforme del arroz. <br><br> Cuando toda el agua se haya absorbido y el arroz esté tierno, retira la olla del fuego. Deja reposar el arroz tapado durante unos 5 minutos adicionales. Este periodo de reposo permite que el arroz termine de cocinarse con el vapor restante, asegurando que cada grano esté perfectamente cocido y esponjoso. <br><br> Finalmente, esponja el arroz con un tenedor antes de servirlo para separar los granos y obtener una textura ligera y aireada. Siguiendo estos pasos meticulosamente, obtendrás un arroz cocido a la perfección, listo para acompañar cualquier plato principal con su sabor suave y su textura impecable. ¡Listo para disfrutar!"
        },
        {
            title1: "Cómo Realzar el Sabor de las Sopas y Guisos",
            title2: "Secretos para Mejorar el Sabor de tus Preparaciones Caldosas",
            subtitle: "Consejos para potenciar el sabor de tus platos de cuchara",
            imageUrl: "https://images.pexels.com/photos/1703272/pexels-photo-1703272.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Sopa caliente",
            content: "Para intensificar y enriquecer el sabor de tus sopas y guisos, puedes incorporar una variedad de ingredientes aromáticos y sabrosos que elevarán tu preparación a un nivel superior. Aquí te explico cómo hacerlo de manera detallada y efectiva: <br><br> 1. <b>Añade hierbas aromáticas:</b> Introduce una hoja de laurel al caldo al comienzo de la cocción. El laurel aporta un sabor sutil y terroso que se despliega lentamente, realzando los sabores de los demás ingredientes. Además, agrega ramitas de tomillo fresco. El tomillo tiene un perfil aromático que combina bien con una amplia gama de ingredientes, añadiendo una nota fresca y herbácea a tus sopas y guisos. <br><br> <b>2.Incorpora vino blanco:</b> Un chorrito de vino blanco seco puede transformar el sabor de tus caldos. Añádelo una vez que los vegetales estén dorados y antes de añadir el caldo. El vino blanco aporta una acidez suave y complejidad al plato, y a medida que se cocina, su alcohol se evapora, dejando solo el sabor refinado.<br><br> <b>3.Capas de sabor:</b> Además de los ingredientes mencionados, considera añadir otras capas de sabor. Por ejemplo, puedes saltear una mezcla de cebollas, zanahorias y apio (conocida como mirepoix) en un poco de aceite de oliva o mantequilla antes de añadir los ingredientes líquidos. Este proceso carameliza los azúcares naturales de los vegetales, añadiendo profundidad y dulzura a la base de tu sopa o guiso. <br><br> <b>4.Tiempo de cocción:</b> Permitir que tu sopa o guiso cocine a fuego lento durante un período prolongado también ayuda a intensificar los sabores. La cocción lenta y prolongada permite que todos los ingredientes se mezclen y desarrollen su máximo potencial de sabor.<br><br> <b>5.Reposo antes de servir:</b> Una vez que la sopa o guiso esté cocido, apaga el fuego y deja que repose durante unos minutos antes de servir. Este paso permite que los sabores se asienten y se mezclen adecuadamente, resultando en un plato más sabroso y equilibrado."
        },
        {
            title1: "Cómo Deshacerse del Exceso de Sal en una Sopa o Guiso",
            title2: "Consejos para Corregir el Nivel de Sal en tus Preparaciones",
            subtitle: "Soluciones rápidas para ajustar el sabor de tus platos salados",
            imageUrl: "https://images.pexels.com/photos/3693294/pexels-photo-3693294.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Cuchara y sal",
            content: "Si has preparado una sopa o guiso y ha quedado demasiado salado, no te preocupes, hay una solución sencilla para equilibrar el sabor. Un truco eficaz es añadir unas rodajas de papa cruda al plato. La papa tiene la capacidad de absorber parte del exceso de sal mientras se cocina. Simplemente agrega las rodajas y deja que la sopa o el guiso hiervan a fuego lento durante unos minutos. Después, retira las papas y prueba nuevamente el plato. <br><br> Otra opción es incorporar una cucharadita de azúcar. Aunque parezca sorprendente, el azúcar puede contrarrestar el sabor salado, creando un equilibrio más agradable al paladar. Añádela con moderación y cocina el plato por unos minutos antes de volver a probarlo. <br><br> Es importante probar el sabor después de cada adición, para asegurarte de no alterar demasiado el equilibrio de los sabores. Si es necesario, repite el proceso hasta alcanzar el sabor deseado. Este método no solo te ayudará a reducir la salinidad, sino que también permitirá mantener la textura y consistencia original de tu sopa o guiso. Con estos sencillos pasos, podrás disfrutar de un plato perfectamente equilibrado sin tener que empezar de nuevo."

        },
        {
            title1: "Cómo Evitar que las Papas Se Oxiden",
            title2: "Trucos para Mantener las Papas Frescas y Sin Oxidación",
            subtitle: "Consejos prácticos para conservar la frescura de las papas",
            imageUrl: "https://media.istockphoto.com/id/866584830/es/foto/patatas-asadas-sobre-mesa-de-cocina-de-madera.jpg?b=1&s=612x612&w=0&k=20&c=y2TPP8nyW-PnEOVGfWBcfBQNkSxxpVST_GPeSpUku_A=",
            altText: "Papas frescas",
            content: "Para evitar que las papas se oxiden después de pelarlas, es importante sumergirlas inmediatamente en agua fría. Este sencillo paso ayuda a prevenir que las papas se vuelvan marrones y pierdan su frescura. Para mejorar aún más este proceso, agrega unas gotas de jugo de limón o vinagre al agua. Estos ácidos naturales ayudan a mantener el color claro de las papas, retardando la oxidación. <br><br> Si no planeas usar las papas de inmediato, puedes almacenarlas en un recipiente con agua en el refrigerador. Asegúrate de que las papas estén completamente sumergidas para obtener los mejores resultados. De esta manera, las papas se mantendrán frescas y listas para usar cuando las necesites. Este método es especialmente útil si estás preparando una gran cantidad de papas con anticipación para una receta o una comida especial. Con estos simples pasos, podrás disfrutar de papas frescas y de buen aspecto, listas para ser cocinadas en cualquier momento."
        },
        {
            title1: "Cómo Conservar el Ajo Fresco por Más Tiempo",
            title2: "Trucos para Mantener el Ajo Aromático y Fresco",
            subtitle: "Técnicas para preservar la frescura y sabor del ajo",
            imageUrl: "https://images.pexels.com/photos/928251/pexels-photo-928251.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Ajo fresco",
            content: "Para conservar el ajo fresco por más tiempo, es recomendable guardarlo en un lugar fresco y seco, como una despensa o un armario. Evita almacenar el ajo en el refrigerador, ya que la humedad puede hacer que se ponga blando o que se forme moho, lo que compromete su sabor y textura. <br><br> Si has comprado una gran cantidad de ajo y no planeas usarlo todo de inmediato, considera congelarlo en porciones individuales. Una buena opción es pelar y picar el ajo, luego colocarlo en bandejas para cubos de hielo o en pequeñas porciones envueltas en papel film. De esta manera, tendrás ajo listo para usar sin necesidad de descongelar más de lo necesario. <br><br> Siguiendo estos sencillos consejos, podrás mantener tu ajo fresco y en óptimas condiciones por más tiempo, asegurando que siempre esté listo para añadir su característico sabor a tus platos."
        },
        {
            title1: "Cómo Conservar Hierbas Frescas por Más Tiempo",
            title2: "Secretos para Mantener Hierbas Aromáticas Siempre Frescas",
            subtitle: "Técnicas simples para prolongar la vida útil de tus hierbas",
            imageUrl: "https://images.pexels.com/photos/3912947/pexels-photo-3912947.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Hierbas frescas",
            content: "Para conservar las hierbas frescas por más tiempo, envuélvelas cuidadosamente en papel de cocina ligeramente húmedo. Este papel ayuda a mantener la humedad adecuada, evitando que las hierbas se sequen sin crear un ambiente demasiado húmedo que podría fomentar la aparición de moho. Luego, coloca las hierbas envueltas en una bolsa de plástico perforada, lo cual permite la circulación de aire y evita la acumulación de humedad excesiva. <br><br> Guarda esta bolsa en el cajón de verduras de tu refrigerador, que es el lugar más adecuado para mantener la frescura de las hierbas. Es importante cambiar el papel de cocina cada pocos días para asegurar que las hierbas se mantengan en un ambiente limpio y húmedo. Además, revisa regularmente las hierbas y elimina cualquier hoja marchita o dañada, ya que estas pueden acelerar el deterioro de las hojas sanas. <br><br> Siguiendo esta técnica, podrás mantener tus hierbas frescas y listas para usar durante más tiempo, asegurando que siempre tengas a mano ingredientes de alta calidad para dar sabor y aroma a tus platos favoritos. Con estos sencillos cuidados, tus hierbas permanecerán en óptimas condiciones, permitiéndote aprovechar al máximo sus propiedades y beneficios culinarios."
        },
        {
            title1: "Cómo Seleccionar el Pescado Fresco en el Mercado",
            title2: "Consejos para Elegir Pescado de Calidad en la Pescadería",
            subtitle: "Indicaciones clave para identificar pescado fresco y de buena calidad",
            imageUrl: "https://images.pexels.com/photos/61153/fish-fischer-ocean-market-61153.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Pescado fresco",
            content: "Al comprar pescado fresco, hay varios aspectos clave a considerar para asegurarte de que estás obteniendo un producto de calidad. Primero, verifica que los ojos del pescado estén brillantes y salientes, no hundidos ni opacos, ya que esto es un indicador de frescura. Las branquias deben ser de un color rojo o rosado vibrante y estar libres de moco, lo que sugiere que el pescado está en buen estado. <br><br>  Además, la piel del pescado debe tener un aspecto brillante y ser firme al tacto. Evita aquellos pescados cuya piel se sienta pegajosa o viscosa, ya que esto puede ser un signo de que el pescado no está fresco. Por último, el olor es un indicador crucial: el pescado fresco debe tener un olor suave y marino, no fuerte ni desagradable. <br><br> Siguiendo estos consejos, podrás seleccionar pescado fresco y de alta calidad, asegurando que tus platos tengan el mejor sabor y textura posibles." 
        },
        {
            title1: "Cómo Almacenar Aceite de Oliva para Mantener su Frescura",
            title2: "Consejos para Conservar las Propiedades del Aceite de Oliva",
            subtitle: "Mantén tu aceite de oliva en óptimas condiciones con estos consejos",
            imageUrl: "https://images.pexels.com/photos/1022385/pexels-photo-1022385.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Botella de aceite de oliva",
            content: "Para preservar la frescura y el sabor del aceite de oliva, es importante almacenarlo correctamente. Mantén el aceite en un lugar fresco y oscuro, lejos de la luz directa y fuentes de calor. La exposición a la luz y al calor puede acelerar la oxidación del aceite, lo que afecta negativamente su sabor y calidad. <br><br>  Después de cada uso, asegúrate de cerrar bien la botella para minimizar la exposición al aire y prevenir la oxidación. Es fundamental evitar almacenar el aceite cerca de fuentes de calor como la estufa o el horno, ya que las altas temperaturas pueden degradar el aceite más rápidamente. <br><br> Después de cada uso, asegúrate de cerrar bien la botella para minimizar la exposición al aire y prevenir la oxidación. Es fundamental evitar almacenar el aceite cerca de fuentes de calor como la estufa o el horno, ya que las altas temperaturas pueden degradar el aceite más rápidamente."
        },
        {
            title1: "Cómo Elegir y Preparar el Agua de Cocción para Pastas",
            title2: "Consejos para Cocinar Pasta Al Dente con Agua de Calidad",
            subtitle: "Secretos para lograr la cocción perfecta de tus pastas favoritas",
            imageUrl: "https://images.pexels.com/photos/3256807/pexels-photo-3256807.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Pasta cocinada",
            content: "Al cocinar pasta, alcanzar el punto perfecto requiere seguir algunos pasos esenciales. Comienza usando una olla grande con abundante agua. Esto asegura que la pasta tenga suficiente espacio para cocinarse de manera uniforme y no se pegue. Una vez que el agua esté hirviendo, añade sal generosamente para realzar el sabor de la pasta mientras se cocina. <br><br> Es crucial evitar añadir aceite al agua, ya que esto puede interferir con la capacidad de la salsa para adherirse correctamente a la pasta después de cocinarse. Durante la cocción, revuelve ocasionalmente la pasta para prevenir que se aglutine en el fondo de la olla. <br><br> Para determinar si la pasta está lista, prueba un poco unos minutos antes del tiempo indicado en el paquete. Debe estar al dente, lo que significa que esté firme pero tierna al morder. Una vez alcanzado este punto ideal, escurre la pasta inmediatamente para evitar que se cocine en exceso y se vuelva blanda. <br><br> Siguiendo estos pasos prácticos y precisos, podrás preparar pasta perfectamente cocida y lista para combinar con tu salsa preferida. Este proceso no solo garantiza una textura óptima, sino que también maximiza el sabor y la autenticidad de tu plato de pasta."
        },
        {
            title1: "Cómo Preparar un Caldo de Verduras Casero",
            title2: "Receta Sencilla para Hacer Caldo de Verduras desde Cero",
            subtitle: "Pasos básicos para un caldo aromático y nutritivo",
            imageUrl: "https://images.pexels.com/photos/20852223/pexels-photo-20852223/free-photo-of-vegetales-verduras-cuchara-comida.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Caldo de verduras",
            content: "Para preparar un delicioso caldo de verduras casero, es fundamental seleccionar vegetales frescos como zanahorias, cebollas, apio y perejil. Lava bien los vegetales y córtalos en trozos grandes para liberar sus sabores y nutrientes al máximo. <br><br> Coloca los vegetales en una olla grande y cúbrelos con agua fría. Lleva la olla a fuego lento y deja que hierva suavemente durante al menos una hora. Durante este tiempo, es posible que se forme espuma en la superficie del caldo; retírala con una cuchara para obtener un caldo más limpio y claro. <br><br> Una vez que el caldo haya cocido el tiempo necesario, cuela los vegetales y los sólidos para obtener un líquido dorado y aromático. Este caldo casero es perfecto como base para sopas y guisos, así como para cocinar arroces y otros platillos que se beneficien de su sabor natural y nutritivo. <br><br> Preparar tu propio caldo de verduras no solo añade un toque casero a tus recetas, sino que también te permite controlar los ingredientes y disfrutar de un resultado final lleno de frescura y sabor."
        },
        {
            title1: "Cómo Preparar una Salsa Marinara Casera",
            title2: "Receta Tradicional de Salsa Marinara Italiana",
            subtitle: "Pasos simples para una salsa de tomate deliciosa",
            imageUrl: "https://images.pexels.com/photos/26207761/pexels-photo-26207761/free-photo-of-plato-vegetales-verduras-comida.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Salsa marinara",
            content: "Para preparar una deliciosa salsa marinara casera, comienza salteando cebolla y ajo picados en aceite de oliva hasta que estén dorados y fragantes. A continuación, añade tomates pelados y triturados, hojas frescas de albahaca, sal, pimienta y una pizca de azúcar para equilibrar la acidez de los tomates. <br><br> Deja cocinar la salsa a fuego lento durante al menos 30 minutos para permitir que los sabores se mezclen y desarrollen completamente. Este tiempo de cocción lenta es crucial para lograr una salsa marinara rica y sabrosa. <br><br> Esta versátil salsa casera es perfecta para acompañar pasta, como base para pizzas caseras o como complemento para platos de pollo o pescado. Su aroma y sabor fresco añadirán un toque especial a cualquier comida que prepares. <br><br> Preparar tu propia salsa marinara no solo garantiza ingredientes frescos y naturales, sino que también te permite personalizar el nivel de sazón según tus preferencias. Disfruta explorando diferentes usos y sabores con esta salsa casera llena de autenticidad y calidad."
        },
        {
            title1: "Cómo Preparar un Bizcocho Esponjoso",
            title2: "Receta Clásica para Hacer un Bizcocho Perfecto",
            subtitle: "Pasos detallados para un bizcocho suave y delicioso",
            imageUrl: "https://images.pexels.com/photos/1938268/pexels-photo-1938268.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Bizcocho esponjoso",
            content: "Para lograr un bizcocho esponjoso y delicioso, sigue estos pasos detallados: <br><br> <b>1.Preparación de la mezcla seca:</b> En un bol, mezcla la harina con el polvo de hornear y una pizca de sal. Esto asegurará que la masa del bizcocho tenga una textura uniforme y aireada. <br><br> <b>2.Batido de la mantequilla y el azúcar:</b> En otro bol grande, bate la mantequilla suave con el azúcar hasta que la mezcla esté cremosa y suave. Este paso es crucial para incorporar aire a la masa y lograr una textura esponjosa en el bizcocho. <br><br> <b>3.Incorporación de los huevos:</b> Agrega los huevos uno a uno a la mezcla de mantequilla y azúcar, batiendo bien después de cada adición. Esto asegura que los huevos se integren completamente y contribuyan a la estructura del bizcocho. <br><br> <b>4.Incorporación de la mezcla de harina y líquidos:</b> Alterna la adición de la mezcla de harina (preparada en el paso 1) con la leche y la esencia de vainilla. Comienza y termina con la mezcla de harina para evitar que la masa se corte y mantener una textura uniforme. <br><br> <b>5.Preparación del molde y horneado:</b> Engrasa y enharina un molde adecuado para bizcochos. Vierte la masa preparada en el molde y extiéndela uniformemente. Hornea a 180°C (350°F) durante aproximadamente 30-35 minutos, o hasta que al insertar un palillo en el centro del bizcocho, este salga limpio. <br><br> <b>6.Enfriado y desmoldado:</b> Deja enfriar el bizcocho dentro del molde sobre una rejilla durante unos 10 minutos. Luego, desmolda cuidadosamente y deja que termine de enfriarse completamente sobre la rejilla.<br><br>Siguiendo estos pasos meticulosos, lograrás un bizcocho esponjoso y perfectamente horneado, ideal para disfrutar solo o acompañado de tus ingredientes favoritos."
        },
        {
            title1: "Cómo Preparar Salmón a la Parrilla con Limón y Eneldo",
            title2: "Receta Refrescante para Salmón a la Parrilla",
            subtitle: "Pasos simples para un plato de pescado sabroso y saludable",
            imageUrl: "https://images.pexels.com/photos/842142/pexels-photo-842142.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Salmón a la parrilla",
            content: "Para preparar salmón a la parrilla con un resultado jugoso y lleno de sabor, sigue estos pasos detallados:<br><br> <b>1.Preparación del salmón:</b> Sazona los filetes de salmón con sal y pimienta al gusto. Exprime jugo de limón fresco sobre los filetes y espolvorea eneldo picado uniformemente sobre ellos. El limón y el eneldo realzan el sabor natural del salmón y le dan un toque fresco.<br><br> <b>2.Preparación de la parrilla:</b> Precalienta la parrilla a fuego medio-alto y asegúrate de engrasar la rejilla con un poco de aceite para evitar que el salmón se pegue.<br><br> <b>3.Cocción del salmón:</b> Coloca los filetes de salmón en la parrilla con la piel hacia abajo. Cocina durante aproximadamente 4-5 minutos por cada lado, o hasta que el salmón esté cocido pero aún jugoso en el centro. Evita voltearlos demasiado pronto para asegurar que se formen esas atractivas marcas de parrilla y que el pescado se cocine de manera uniforme.<br><br> <b>4.Servir:</b> Una vez listos, retira los filetes de salmón de la parrilla con cuidado para evitar que se rompan. Sirve los filetes de salmón con rodajas de limón fresco y acompáñalos con una ensalada fresca o tus guarniciones preferidas.<br><br> Este método de cocción resalta el sabor natural y la textura suculenta del salmón, ofreciendo una opción saludable y sabrosa para cualquier comida. Disfruta de tu salmón a la parrilla como plato principal, complementado con sabores cítricos y herbales que lo hacen irresistible."
        },
        {
            title1: "Cómo Hacer un Guacamole Casero y Auténtico",
            title2: "Receta Tradicional de Guacamole Mexicano",
            subtitle: "Pasos sencillos para una salsa de aguacate deliciosa",
            imageUrl: "https://images.pexels.com/photos/5737254/pexels-photo-5737254.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Guacamole casero",
            content: "Para preparar un delicioso guacamole casero, comienza seleccionando aguacates maduros. Con la ayuda de un tenedor, machácalos hasta lograr una textura gruesa y uniforme. Añade cebolla finamente picada para darle un toque aromático, así como tomate fresco y cilantro picado para aportar frescura y color. Exprime un generoso chorro de jugo de limón para realzar los sabores, y sazona con sal y pimienta al gusto. <br><br> Es crucial mezclar todos los ingredientes de manera uniforme para que se integren los sabores. Prueba la mezcla y ajusta la sazón según tus preferencias personales, ya sea añadiendo más limón para un toque más ácido o más sal si lo prefieres más salado. <br><br> El guacamole está listo para servir. Disfrútalo acompañado de chips de maíz crujientes, o utilízalo como un complemento perfecto para tacos, quesadillas o nachos. Su cremosidad y sabor fresco lo convierten en una opción versátil y deliciosa para cualquier ocasión. <br><br> ¡Buen provecho!"
        },
        {
            title1: "Cómo Preparar la Quinua Perfecta",
            title2: "Consejo para Cocinar Quinua de Forma Óptima",
            subtitle: "Pasos simples para una cocción precisa",
            imageUrl: "https://images.pexels.com/photos/6740849/pexels-photo-6740849.jpeg?auto=compress&cs=tinysrgb&w=600",
            altText: "Quinua cocida",
            content: "Para asegurarte de cocinar quinua de manera perfecta y obtener granos tiernos y sabrosos, sigue estos pasos detallados:<br><br> <b>1.Enjuague inicial:</b> Comienza enjuagando la quinua bajo agua fría en un colador fino. Este paso es crucial para eliminar la saponina, una sustancia natural que puede darle un sabor amargo a la quinua.<br><br> <b>2.Proporción de líquido:</b> En una olla mediana, combina una taza de quinua con dos tazas de agua o caldo de tu elección. El caldo puede agregar un sabor adicional, así que elige según tus preferencias.<br><br> <b>3.Cocción inicial:</b> Lleva la mezcla a ebullición a fuego medio-alto. Una vez que hierva, reduce el fuego a bajo para mantener un hervor suave. Cubre la olla con una tapa ajustada.<br><br> <b>4.Tiempo de cocción:</b> Deja que la quinua se cocine a fuego lento durante 15-20 minutos. Durante este tiempo, la quinua absorberá el líquido y los granos deberían hincharse ligeramente y volverse tiernos. <br><br> <b>5.Reposo:</b> Una vez transcurrido el tiempo de cocción, retira la olla del fuego y deja reposar la quinua tapada durante unos 5 minutos más. Este paso final permite que la quinua absorba cualquier líquido restante y se vuelva aún más esponjosa.<br><br> <b>6.Desgrane con un tenedor:</b> Pasado el tiempo de reposo, utiliza un tenedor para desgranar suavemente la quinua. Esto ayuda a separar los granos y a airearlos, asegurando una textura ligera y esponjosa.<br><br> Con estos simples pasos, habrás preparado quinua perfectamente cocida, lista para disfrutar como un delicioso acompañamiento o como base nutritiva para tus platillos favoritos."
        },
    ];
    const consejosPorPagina = 10; // Número de consejos por página
    let currentPage = 1;

    // Función para mostrar los consejos según la página actual

    function mostrarConsejos() {
const startIndex = (currentPage - 1) * consejosPorPagina;
const endIndex = startIndex + consejosPorPagina;
const consejosToShow = consejosData.slice(startIndex, endIndex);

// Limpiar el contenedor antes de agregar nuevos elementos
consejosContainer.innerHTML = "";

consejosToShow.forEach((consejo) => {
const section = document.createElement("section");
section.classList.add("glossary");
section.innerHTML = `
    <h1>${consejo.title1}</h1>
    <h2>${consejo.title2}</h2>
    <h3>${consejo.subtitle}</h3>
    <br>
    <p style="text-align: justify;">${consejo.content}</p>
    <br>
    <img src="${consejo.imageUrl}" alt="${consejo.altText}">
`;
consejosContainer.appendChild(section);
});

// Actualizar la visibilidad de los botones de paginación
if (currentPage === 1) {
previousPage.classList.add("disabled");
} else {
previousPage.classList.remove("disabled");
}

if (endIndex >= consejosData.length) {
nextPage.classList.add("disabled");
} else {
nextPage.classList.remove("disabled");
}
}

    // Event listener para página anterior
    previousPage.addEventListener("click", function (event) {
        event.preventDefault();
        if (currentPage > 1) {
            currentPage--;
            mostrarConsejos();
            setTimeout(function() {
                window.scrollTo({ top: 0, behavior: 'smooth' }); // Scroll hacia arriba
            }, 100); // Ajusta el tiempo según sea necesario
        }
    });

    // Event listener para página siguiente
    nextPage.addEventListener("click", function (event) {
        event.preventDefault();
        if (currentPage < Math.ceil(consejosData.length / consejosPorPagina)) {
            currentPage++;
            mostrarConsejos();
            setTimeout(function() {
                window.scrollTo({ top: 0, behavior: 'smooth' }); // Scroll hacia arriba
            }, 100); // Ajusta el tiempo según sea necesario
        }
    });

    // Mostrar los consejos inicialmente
    mostrarConsejos();
});

document.addEventListener("DOMContentLoaded", function () {
    function initNovedadesPagination() {
        const novedadesContainer = document.getElementById("novedadesContainer");
        const previousPage = document.getElementById("previousPageNovedades");
        const nextPage = document.getElementById("nextPageNovedades");

        const novedadesPorPagina = 7; // Número de novedades por página
        let currentPage = 1;

        // Datos de las novedades
        const novedadesData = [
            {
                title: "Nueva Receta: Ensalada Fresca",
                subtitle: "Cómo preparar una ensalada saludable",
                subsubtitle: "Ingredientes frescos para una comida ligera",
                content: "Descubre cómo preparar una ensalada fresca con ingredientes de temporada. Perfecta para el verano. Esta receta utiliza lechuga, tomates cherry, pepinos, y una vinagreta casera hecha con aceite de oliva extra virgen, jugo de limón, y hierbas frescas. Es fácil de hacer y muy refrescante. La ensalada no solo es deliciosa sino también muy saludable, rica en vitaminas y minerales que son esenciales para una dieta equilibrada. Además, puedes personalizar la ensalada agregando tus ingredientes favoritos como aguacate, queso feta, o nueces para darle un toque especial. Esta ensalada es perfecta para acompañar cualquier comida o para disfrutar como un plato principal ligero. No olvides que la clave de una buena ensalada es la frescura de los ingredientes y una vinagreta bien balanceada. Disfruta de este plato nutritivo y refrescante.",
                imageUrl: "https://images.pexels.com/photos/1213710/pexels-photo-1213710.jpeg?auto=compress&cs=tinysrgb&w=600",
                altText: "Ensalada Fresca"
            },
            {
                title: "Tendencias en la Cocina: Plant Based",
                subtitle: "Adopta una dieta basada en plantas",
                subsubtitle: "Beneficios de una alimentación saludable",
                content: "Explora la tendencia de la cocina basada en plantas y cómo integrarla en tu dieta diaria. La cocina plant based se centra en el uso de alimentos derivados de plantas, incluyendo frutas, verduras, granos, nueces, y legumbres. Este tipo de dieta no solo es beneficiosa para tu salud, ayudando a reducir el riesgo de enfermedades crónicas, sino que también es más sostenible para el medio ambiente. Para empezar, puedes intentar reemplazar las proteínas animales por proteínas vegetales como el tofu, las lentejas, y los garbanzos. También puedes experimentar con recetas nuevas y creativas que incorporen una variedad de colores y texturas, haciendo tus comidas no solo nutritivas sino también visualmente atractivas. La adopción de una dieta basada en plantas puede ser un cambio significativo, pero con el tiempo, notarás mejoras en tu bienestar general y en la calidad de tus comidas.",
                imageUrl: "https://images.pexels.com/photos/2062426/pexels-photo-2062426.jpeg?auto=compress&cs=tinysrgb&w=600",
                altText: "Cocina Plant Based"
            },
            {
                title: "Técnicas de Cocina: Sous Vide",
                subtitle: "Cocina como un profesional",
                subsubtitle: "Domina la técnica de cocción al vacío",
                content: "Aprende a cocinar con la técnica sous vide para obtener resultados perfectos cada vez. La técnica sous vide consiste en cocinar alimentos en una bolsa sellada al vacío a una temperatura controlada en agua. Esto permite una cocción uniforme y precisa, conservando el sabor y los nutrientes de los alimentos. Es ideal para cocinar carnes, pescados, y verduras, y aunque puede parecer complicado al principio, con un poco de práctica, podrás dominar esta técnica. La cocción sous vide garantiza que tus alimentos estén cocidos a la perfección, manteniendo su jugosidad y textura. Además, una vez que los alimentos están cocidos, puedes sellarlos rápidamente en una sartén para darles una capa exterior crujiente y dorada. Esta técnica no solo es usada por chefs profesionales sino que también puede ser una herramienta poderosa para mejorar tus habilidades culinarias en casa.",
                imageUrl: "https://images.pexels.com/photos/1080721/pexels-photo-1080721.jpeg?auto=compress&cs=tinysrgb&w=600",
                altText: "Sous Vide"
            },
            {
                title: "Entrevista con el Chef Juan Pérez",
                subtitle: "Consejos y trucos de un experto",
                subsubtitle: "Secretos de la cocina revelados",
                content: "Una charla inspiradora con el Chef Juan Pérez sobre sus recetas favoritas y consejos culinarios. En esta entrevista, el Chef Juan Pérez comparte sus secretos para crear platos deliciosos y saludables. Habla sobre la importancia de usar ingredientes frescos y de temporada, y cómo experimentar con diferentes sabores y técnicas puede llevar tus habilidades culinarias al siguiente nivel. También ofrece consejos prácticos para cocinar en casa, desde cómo organizar tu cocina hasta cómo planificar tus comidas de manera eficiente. Esta entrevista es una fuente de inspiración para cualquier amante de la cocina que desee mejorar sus habilidades y creatividad en la cocina. Descubre los métodos y pensamientos detrás de algunos de sus platos más famosos y cómo puedes aplicar estas ideas en tu propia cocina.",
                imageUrl: "https://images.pexels.com/photos/2696064/pexels-photo-2696064.jpeg?auto=compress&cs=tinysrgb&w=600",
                altText: "Chef Juan Pérez"
            },
            {
                title: "Historias de la Comunidad: María García",
                subtitle: "Transformación a través de la cocina",
                subsubtitle: "Un viaje hacia una vida más saludable",
                content: "Conoce cómo María García ha transformado su dieta siguiendo nuestras recetas saludables. María García, una miembro activa de nuestra comunidad, ha adoptado una dieta más saludable incorporando nuestras recetas en su rutina diaria. Ella comparte su viaje de transformación, hablando sobre los desafíos que enfrentó y cómo logró superarlos. Desde perder peso hasta sentirse más energizada, la historia de María es un testimonio de cómo una alimentación saludable puede tener un impacto positivo en tu vida. Además, ofrece consejos útiles para aquellos que están comenzando su propio viaje hacia una mejor alimentación y bienestar. Su historia es un recordatorio de que con dedicación y las herramientas adecuadas, cualquier persona puede lograr una vida más saludable y feliz.",
                imageUrl: "https://images.pexels.com/photos/3771106/pexels-photo-3771106.jpeg?auto=compress&cs=tinysrgb&w=600",
                altText: "María García"
            },
            {
                title: "Producto Destacado: Aceite de Oliva",
                subtitle: "Beneficios del oro líquido",
                subsubtitle: "Incorporando el aceite de oliva en tus recetas",
                content: "Conoce las propiedades y beneficios del aceite de oliva extra virgen en tus preparaciones. El aceite de oliva es un ingrediente básico en la cocina mediterránea y es conocido por sus numerosos beneficios para la salud. Rico en antioxidantes y grasas saludables, el aceite de oliva puede ayudar a reducir la inflamación y mejorar la salud del corazón. Es ideal para aderezar ensaladas, cocinar a la parrilla, y hacer marinadas. En este artículo, exploramos los diferentes tipos de aceite de oliva y cómo elegir el mejor para tus necesidades culinarias. También ofrecemos consejos sobre cómo almacenar el aceite de oliva para mantener su frescura y sabor. Aprovecha al máximo este ingrediente versátil y descubre nuevas maneras de incluirlo en tus recetas diarias para mejorar tanto el sabor como el valor nutricional de tus comidas.",
                imageUrl: "https://images.pexels.com/photos/33783/olive-oil-salad-dressing-cooking-olive.jpg?auto=compress&cs=tinysrgb&w=600",
                altText: "Aceite de Oliva"
            },
            {
                title: "Explorando Sabores: Cocina Asiática",
                subtitle: "Descubre los secretos de la cocina oriental",
                subsubtitle: "Platos auténticos y técnicas tradicionales",
                content: "La cocina asiática es famosa por su diversidad y riqueza de sabores. Desde el sushi japonés hasta el curry tailandés, cada plato ofrece una experiencia única. En esta sección, te invitamos a explorar los secretos de la cocina oriental. Aprenderás a preparar platos auténticos como el ramen, el dim sum, y el bibimbap. La clave de la cocina asiática radica en el equilibrio de sabores: dulce, salado, ácido y umami. Utilizando ingredientes frescos como jengibre, ajo, y salsa de soja, puedes crear comidas deliciosas y saludables. También te enseñaremos técnicas tradicionales como el wok y la fermentación. Estas técnicas no solo realzan el sabor de los ingredientes, sino que también conservan sus nutrientes. Cocinar platos asiáticos en casa puede ser una aventura emocionante que amplía tus horizontes culinarios. Con nuestras recetas y consejos, podrás impresionar a tus amigos y familiares con comidas exóticas y auténticas.",
                imageUrl: "https://images.pexels.com/photos/628776/pexels-photo-628776.jpeg?auto=compress&cs=tinysrgb&w=600",
                altText: "Cocina Asiática"
            },
            {
                title: "Sistema de Consejeros: Expertos a tu Disposición",
                subtitle: "Asesoría personalizada para tus necesidades culinarias",
                subsubtitle: "Consejos y trucos de profesionales",
                content: "Nuestro nuevo sistema de consejeros está diseñado para ofrecerte asesoría personalizada en el mundo culinario. Contamos con una red de expertos en diversas áreas de la cocina que están disponibles para ayudarte con cualquier consulta que tengas. Ya sea que necesites consejos sobre técnicas de cocción, recomendaciones de ingredientes, o ayuda con la planificación de menús, nuestros consejeros están aquí para asistirte. Además, puedes recibir sugerencias personalizadas basadas en tus preferencias y necesidades dietéticas. Con nuestro sistema de consejeros, tendrás acceso a una fuente inagotable de conocimientos y experiencia que te ayudará a mejorar tus habilidades culinarias y a disfrutar más de tu tiempo en la cocina.",
                imageUrl: "https://media.istockphoto.com/id/921788682/es/foto/mostrando-contrato-a-camarera.jpg?b=1&s=612x612&w=0&k=20&c=1z_0Jn7DYL5KYrxUN6rwFYss9OS3R_ap1oP2AJEvwYQ=",
                altText: "Sistema de Consejeros"
            },
            {
                title: "Nuevas Dietas: Salud y Nutrición",
                subtitle: "Encuentra la dieta perfecta para ti",
                subsubtitle: "Opciones balanceadas y nutritivas",
                content: "Explora nuestras nuevas dietas diseñadas para promover una alimentación saludable y equilibrada. Ofrecemos una variedad de planes alimenticios que se adaptan a diferentes necesidades y objetivos, ya sea que quieras perder peso, ganar masa muscular, o simplemente mantener un estilo de vida saludable. Nuestras dietas están elaboradas por nutricionistas expertos y se basan en ingredientes frescos y naturales. Cada plan incluye recetas detalladas, listas de compras, y consejos para mantener la motivación. Además, puedes personalizar tu dieta según tus preferencias y restricciones alimenticias. Con nuestras dietas, mejorar tu salud y bienestar nunca fue tan fácil y delicioso.",
                imageUrl: "https://images.pexels.com/photos/2318966/pexels-photo-2318966.jpeg?auto=compress&cs=tinysrgb&w=600",
                altText: "Dietas Saludables"
            },
            {
                title: "Descubre y Encuentra Recetas: Cocina a Tu Alcance",
                subtitle: "Tu biblioteca culinaria personal",
                subsubtitle: "Miles de recetas al alcance de tu mano",
                content: "Nuestra plataforma te ofrece una amplia colección de recetas para todos los gustos y ocasiones. Desde platos rápidos y fáciles hasta creaciones gourmet, aquí encontrarás inspiración para cualquier momento. Nuestra biblioteca de recetas está organizada de manera intuitiva, permitiéndote buscar por ingredientes, tipo de cocina, nivel de dificultad, y más. Además, cada receta viene con instrucciones detalladas y consejos prácticos para ayudarte a lograr resultados perfectos. Ya sea que estés buscando una nueva idea para la cena de esta noche o planeando un banquete para una ocasión especial, nuestra sección de recetas tiene todo lo que necesitas. Con nuestras herramientas de búsqueda avanzada y recomendaciones personalizadas, cocinar se convierte en una experiencia agradable y sin complicaciones.",
                imageUrl: "https://images.pexels.com/photos/5737454/pexels-photo-5737454.jpeg?auto=compress&cs=tinysrgb&w=600",
                altText: "Biblioteca de Recetas"
            },
            {
                title: "Calendario Nutricional: Planificación Saludable",
                subtitle: "Organiza tus comidas de manera equilibrada",
                subsubtitle: "Plan semanal de nutrición",
                content: "Presentamos nuestro nuevo calendario nutricional, una herramienta diseñada para ayudarte a planificar tus comidas de manera equilibrada y saludable. Con esta herramienta, puedes organizar tu semana con recetas nutritivas y balanceadas, asegurándote de incluir todos los grupos alimenticios necesarios. El calendario nutricional ofrece recomendaciones personalizadas basadas en tus objetivos de salud y preferencias dietéticas. Además, cada plan incluye listas de compras, consejos para la preparación de alimentos y sugerencias para optimizar tu tiempo en la cocina. Ya sea que busques perder peso, ganar músculo o simplemente mantener un estilo de vida saludable, nuestro calendario nutricional te proporciona la guía que necesitas para alcanzar tus metas de manera efectiva y sin estrés.",
                imageUrl: "https://images.pexels.com/photos/20849552/pexels-photo-20849552/free-photo-of-romantico-calendario-pastel-delicioso.jpeg?auto=compress&cs=tinysrgb&w=600",
                altText: "Calendario Nutricional"
            },
            {
                title: "Calculadora de IMC: Evalúa tu Salud",
                subtitle: "Conoce tu Índice de Masa Corporal",
                subsubtitle: "Herramienta fácil y precisa",
                content: "Presentamos nuestra nueva calculadora de IMC (Índice de Masa Corporal), una herramienta fácil de usar que te permite evaluar rápidamente si tu peso está en un rango saludable. Introduce tu peso y altura, y nuestra calculadora te proporcionará tu IMC junto con una interpretación clara de los resultados. Esta herramienta te ayudará a determinar si estás en un peso saludable, con bajo peso, sobrepeso o en obesidad. Además, ofrecemos recomendaciones personalizadas y consejos prácticos para ayudarte a alcanzar y mantener un peso ideal. Ya sea que busques mejorar tu salud general, perder peso o simplemente mantenerte en forma, nuestra calculadora de IMC es el primer paso hacia un bienestar óptimo.",
                imageUrl: "https://media.istockphoto.com/id/1705803105/es/foto/imc-o-medidor-de-escala-de-%C3%ADndice-de-masa-corporal-dial-gage-renderizado-3d.jpg?b=1&s=612x612&w=0&k=20&c=3nFwcQhHcbSDnMhS9UEq5hSIjYc_GFughzNmzH-JENU=",
                altText: "Calculadora de IMC"
            },
            {
                title: "Generador de Recetas Personalizado",
                subtitle: "Encuentra la receta perfecta con lo que tienes a mano",
                subsubtitle: "Aprovecha al máximo tus ingredientes",
                content: "Nuestro generador de recetas personalizado te permite buscar recetas deliciosas utilizando los ingredientes que tienes disponibles en tu despensa. Ya sea que quieras improvisar con lo que tienes o planificar una comida con ingredientes específicos, nuestra herramienta te ofrece opciones creativas y sabrosas. Simplemente ingresa los ingredientes que tienes a mano y descubre una variedad de recetas que puedes preparar fácilmente. Desde platos principales hasta postres, te sorprenderá la diversidad de opciones que nuestra plataforma puede ofrecerte. Con recetas paso a paso y consejos útiles, cocinar será más fácil y divertido que nunca.",
                imageUrl: "https://images.pexels.com/photos/4473496/pexels-photo-4473496.jpeg?auto=compress&cs=tinysrgb&w=600",
                altText: "Generador de Recetas"
            },
            {
                title: "Soporte Técnico",
                subtitle: "Asistencia personalizada para resolver tus problemas",
                subsubtitle: "Estamos aquí para ayudarte en cada paso",
                content: "Nuestro equipo de soporte técnico está aquí para ayudarte con cualquier problema que puedas tener. Ya sea que necesites asistencia con la configuración, solucionar problemas técnicos o resolver preguntas generales sobre nuestra plataforma, estamos listos para brindarte una solución rápida y efectiva. Utiliza nuestro servicio de chat en vivo, envía un correo electrónico o consulta nuestra base de conocimientos para obtener respuestas inmediatas. Estamos comprometidos a proporcionar un soporte excepcional y asegurarnos de que tengas la mejor experiencia posible con nuestros servicios.",
                imageUrl: "https://images.pexels.com/photos/5453811/pexels-photo-5453811.jpeg?auto=compress&cs=tinysrgb&w=600",
                altText: "Soporte Técnico"                
            }
        ];

        // Función para mostrar las novedades según la página actual
        function mostrarNovedades() {
            const startIndex = (currentPage - 1) * novedadesPorPagina;
            const endIndex = startIndex + novedadesPorPagina;
            const novedadesToShow = novedadesData.slice(startIndex, endIndex);

            // Limpiar el contenedor antes de agregar nuevos elementos
            novedadesContainer.innerHTML = "";

            novedadesToShow.forEach((novedad) => {
                const section = document.createElement("section");
                section.classList.add("glossary");
                section.innerHTML = `
                    <h1>${novedad.title}</h1>
                    <h2>${novedad.subtitle}</h2>
                    <h3>${novedad.subsubtitle}</h3>
                    <br>
                    <p style="text-align: justify;">${novedad.content}</p>
                    <br>
                    <img src="${novedad.imageUrl}" alt="${novedad.altText}">
                `;
                novedadesContainer.appendChild(section);
            });

            // Actualizar la visibilidad de los botones de paginación
            if (currentPage === 1) {
                previousPage.classList.add("disabled");
            } else {
                previousPage.classList.remove("disabled");
            }

            if (endIndex >= novedadesData.length) {
                nextPage.classList.add("disabled");
            } else {
                nextPage.classList.remove("disabled");
            }
        }

        // Event listener para página anterior
        previousPage.addEventListener("click", function (event) {
            event.preventDefault();
            if (currentPage > 1) {
                currentPage--;
                mostrarNovedades();
                setTimeout(function() {
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }, 100);
            }
        });

        // Event listener para página siguiente
        nextPage.addEventListener("click", function (event) {
            event.preventDefault();
            if (currentPage < Math.ceil(novedadesData.length / novedadesPorPagina)) {
                currentPage++;
                mostrarNovedades();
                setTimeout(function() {
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }, 100);
            }
        });

        // Mostrar las novedades inicialmente
        mostrarNovedades();
    }

    // Inicializar la paginación para las novedades
    initNovedadesPagination();
});