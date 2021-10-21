I. CREACION DE VUE

II. CONFIGURACION INICIAL 

    1. Ya que solo se utilizará un archivo JavaScript para indicar las rutas de la página web
    2. El archivo src/main.js es aquel en el que se realizan las configuraciones del servidor, incluyendo el uso de un 
        router, y la asignación de un componente inicial a la página web.
    3. Por ahora, el único componente que se utilizará en la página web, es el componente principal App.vue. En este 
        se declara el código HTML, JavaScript y CSS de la página inicial de la página web
        i. En el código que se encuentra en la etiqueta script, se exporta el objeto que define por medio de llaves/valores, 
        los atributos y métodos del componente.
        ii.  name: a esta llave se asigna una cadena que indica el nombre del componente. Este nombre 
            comúnmente es utilizado por otros componentes del proyecto para referenciar al componente.
        iii. data: a esta llave se asigna una función que retorna un objeto, cuyas llaves son el nombre de la variable, 
            y los valores son el valor que se da a cada una de ellas. Estas variables pueden ser utilizadas en 
            cualquier parte del componente, ya sea en sus funciones, o en su código HTML.
        iv. methods: a esta llave se asigna un objeto. La llaves de este objeto representan el nombre de las 
            funciones, y sus valores contienen la definición de cada función del componente.
        v. created: a esta llave se asigna la función que debe ejecutar el componente cada vez que se renderice. 
            Esta no debe retornar nada, y se utiliza para realizar alguna operación necesaria tras renderizar el 
            componente en la página web.

III. ROUTER 

    1. Para esto, parte de la idea básica de asociar una URL a un Componente de Vue, es decir, cada una de las 
    funcionalidades implementadas en un componente tendrá una URL asociada.
    2. Un punto a tener en cuenta es que la propia aplicación puede manipular la URL, y no solamente el usuario, 
    es decir que la aplicación también puede cambiar de componentes y funcionalidades con ayuda del Router.

IV. COMPONENTE APP

    1. Router-View: a través del elemento Router, Vue ofrece algunas herramientas que facilitan el 
    desarrollo de la aplicación, en cuanto al manejo de la URL se refiere, la principal herramienta que 
    ofrece Vue es Router-View, esta herramienta es una etiqueta que se utiliza en el template y permite 
    cargar de manera dinámica el componente correspondiente a la URL actual de la aplicaciónI.
        
        ROUTER-VIEW
        i. Carga estatica -> uso de etiquetas <LogIn></LogIn> y carga el componente Login
        ii. Carga dinamica -> uso de etiqueta <router-view></router-view> y carga el componente asociado a la URL y cuando se modifique la URL cambia el componente.
        
        ROUTER-PUSH 
        i.  Router Push permite cambiar la URL de la aplicación desde el script de un componente, esto resulta útil 
        cuando se desea cambiar de componentes debido a algún evento ocurrido dentro de la aplicación

        INTERACION ENTRE TEMPLETE Y SCRIPT 
        i. Dotar de interacción a la estructura HTML, es decir, sea una página dinámica que se construya 
        y modifique a partir de ciertos eventos y valores.  
        
            * v-if=“value”: -> este es un atributo que puede asociar a cualquier etiqueta del template, dicha 
            etiqueta se cargará únicamente si el valor asignado es True

            * v-on:click=”function”: -> con añadir este atributo a una etiqueta, se asociará una función definida en el script, al evento 
            click de la etiqueta.

    2. INTERACCION ENTRE PADRE E HIJOS
        i. Vue permite definir una estructura de árbol jerárquica entre los 
        componentes, de tal manera que los componentes de un nivel superior (llamados padres), pueden 
        controlar a los componentes de un nivel inferior (llamados hijos)

            *Props: -> son un mecanismo en el cual un componente padre le puede pasar un valor a un 
            componente hijo al momento de definirlo. Esto permite que el hijo realice operaciones a partir 
            de cierta información provista por su padre.

            * Emit: -> Emit: Uno de los mecanismos más interesantes de Vue es ejecutar funciones del componente 
            padre desde los componentes hijos, es decir que, un componente padre puede definir una 
            función, pero puede ser un componente hijo quien la ejecute o emita. Esto resulta útil, pues si 
            bien el hijo puede controlar el momento de ejecución, el padre tiene el control sobre lo que se 
            ejecuta, ya que en este se realiza la implementación de la funciónI.

    3. El componente APP es el encargado de gestionar el flujo de la aplicación y sus componentes, por ello su 
    desarrollo se realizará por partes

    4. El componente APP servirá de base de la aplicación y sobre este se cargarán todos los demás 
    componentes dependiendo de la URL.
    5. Por ello se hará uso de un router view para cargar los 
    componentes hijos. Además, en el componente APP se definen algunas etiquetas que estarán en todo 
    momento durante la ejecución de la aplicación: El header y el footer.
    6. Los botones Iniciar Sesión y Registrarse tienen asociada una función al evento click, esta función 
    deberá modificar la ruta para cargar el componente correspondiente en el router view
    7. El componente APP delegará a componentes hijos la implementación de las funcionalidades LogIn y 
    SignUp, pero este quiere controlar el resultado de estas operaciones, para ello definirá dos métodos 
    completedLogIn y completedSignUp, los cuales sus hijos podrán emitir para informar que se ha 
    finalizado el proceso.