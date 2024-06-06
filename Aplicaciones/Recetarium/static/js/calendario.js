const meals = {
    "domingo-desayuno": "Avena cocida con trozos de fruta fresca y un puñado de nueces.",
    "lunes-desayuno": "Huevos revueltos con vegetales.",
    "martes-desayuno": "Smoothie bowl.",
    "miercoles-desayuno": "Yogur griego con miel y nueces.",
    "jueves-desayuno": "Tostadas de aguacate.",
    "viernes-desayuno": "Panqueques con jarabe de arce.",
    "sabado-desayuno": "Tostadas francesas.",
    "domingo-media-manana": "Un puñado de almendras o nueces mixtas.",
    "lunes-media-manana": "Barrita de granola.",
    "martes-media-manana": "Rodajas de manzana con mantequilla de cacahuate.",
    "miercoles-media-manana": "Batido.",
    "jueves-media-manana": "Mezcla de nueces y semillas.",
    "viernes-media-manana": "Yogur con bayas.",
    "sabado-media-manana": "Hummus con vegetales.",
    "domingo-almuerzo": "Ensalada de pollo a la parrilla.",
    "lunes-almuerzo": "Sándwich de pavo con vegetales.",
    "martes-almuerzo": "Bol de quinoa y frijoles negros.",
    "miercoles-almuerzo": "Wrap de vegetales con hummus.",
    "jueves-almuerzo": "Ensalada César con pollo.",
    "viernes-almuerzo": "Sushi.",
    "sabado-almuerzo": "Ensalada de atún.",
    "domingo-merienda": "Batido de proteínas.",
    "lunes-merienda": "Palitos de queso.",
    "martes-merienda": "Chips de vegetales.",
    "miercoles-merienda": "Batido de frutas.",
    "jueves-merienda": "Requesón con frutas.",
    "viernes-merienda": "Tostadas con mantequilla de cacahuate.",
    "sabado-merienda": "Almendras.",
    "domingo-cena": "Salmón al horno con quinoa.",
    "lunes-cena": "Espaguetis con salsa marinara.",
    "martes-cena": "Filete a la parrilla con vegetales.",
    "miercoles-cena": "Tofu salteado con arroz.",
    "jueves-cena": "Curry de pollo con arroz.",
    "viernes-cena": "Pizza.",
    "sabado-cena": "Tacos de carne de res."
};

window.onload = () => {
    for (const [key, value] of Object.entries(meals)) {
        document.getElementById(key).innerText = value;
    }
};
