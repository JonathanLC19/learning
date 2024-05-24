// script.js
console.log('Hola desde un archivo externo de JavaScript');

// Sentencias
let mensaje = "Hola, Mundo";
console.log(mensaje);

// Espacios en Blanco y Sangría
let nombre = "Juan";
let edad = 30;
console.log(nombre, edad);


/* Interpolación de Cadenas:

A partir de ES6, 
puedes usar las plantillas de cadenas (template literals) para insertar variables en una cadena. 
Usa las comillas invertidas (backticks) `` y ${} para insertar valores.*/

console.log(`Nombre: ${nombre}, Edad: ${edad}`); // Usando plantillas de cadenas

//valor indefinido
let valorIndefinido;
console.log(valorIndefinido); // undefined

/*Symbol:
Introducido en ES6, representa un valor único y anónimo.*/
let simbolo = Symbol('descripcion');

console.log(simbolo); 

/*BigInt:
Introducido en ES2020, permite representar enteros con precisión arbitraria. */
let enteroGrande = BigInt(9007199254740991);
let otroEnteroGrande = 9007199254740991n;

console.log(enteroGrande); 
console.log(otroEnteroGrande); 

/* Objetos:
Los objetos son colecciones de pares clave-valor. 
En JavaScript, casi todo es un objeto,
y los objetos se utilizan para almacenar datos estructurados y entidades más complejas. */

let persona = {
    nombre: "Juan",
    edad: 30,
    esEmpleado: true
};

console.log(persona.nombre); // Juan
console.log(persona["edad"]); // 30

// Objeto con funciones

let persona2 = {
    nombre: "Juan",
    edad: 30,
    saludar: function() {
        console.log(`Hola, mi nombre es ${this.nombre}`);
    }
};

persona2.saludar(); // Hola, mi nombre es Juan

// Anidación de Objetos:

let empresa = {
    nombre: "Tech Corp",
    direccion: {
        calle: "Calle Falsa 123",
        ciudad: "Ciudad Ejemplo"
    }
};

console.log(empresa.direccion.calle); // Calle Falsa 123
