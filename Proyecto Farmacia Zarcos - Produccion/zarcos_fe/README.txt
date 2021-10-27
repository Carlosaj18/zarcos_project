I. CONFIGURACION DE CORS EN DJANGO

    1. Se hace desde django ->  pip install django-cors-headers
    2. Una vez se ha instalado, se debe añadir este paquete en el archivo requirements.txt
    3. Se debe realizar la configuración del servidor del componente lógico para aceptar peticiones de los 
    dominios que se requieren -> El primero de ellos es añadir corsheaders a la lista de aplicaciones instaladas en el proyecto
    4. Luego, en el mismo archivo se debe añadir corsheaders.middleware.CorsMiddleware a la lista de 
    middlewares del servidor
    5. Lo último que se debe hacer es configurar los orígenes desde los cuales el servidor aceptará peticiones. Esto 
    se puede realizar de dos formas, la primera es declarando la variable CORS_ALLOWED_ORIGINS que 
    contendrá una lista de cadenas con los nombres de los orígenes que aceptará
    6. La segunda forma es indicarle a Django que acepte las todas peticiones sin importar su origen. Para ello, se 
    declara la variable CORS_ALLOW_ALL_ORIGINS = True
    7. Se debe hacer el despliegue en Heroku


II. CREACION DE VUE

    1. vue create appName
    2. Para probar el proyecto -> npm run serve
    3. node_modules: donde se almacenan las librerías externas del proyecto
    4. public: donde se almacenan los archivos base de la aplicación web.
    5. src: dnde se almacena el código fuente de la aplicación web

III. MAIN.JS

    1. El archivo src/main.js es aquel en el que se realizan las configuraciones del servidor, incluyendo el uso de un 
    router, y la asignación de un componente inicial a la página web.Da el inicio de la aplicacion. 
    2. Importa los routers de router.js 
    3. Usa el router que saco del archivo y se lo pasa como una funcionalidad a APP -> createApp(App).use(router).mount('#app')

IV. ROUTER -> Vue ofrece el concepto de Router, el cual tiene como objetivo manejar las URL dentro la aplicación

    1. Ya que solo se utilizará un archivo JavaScript para indicar las rutas de la página web
    2. Para esto, parte de la idea básica de asociar una URL a un Componente de Vue, es decir, cada una de las 
    funcionalidades implementadas en un componente tendrá una URL asociada.
    3. Un punto a tener en cuenta es que la propia aplicación puede manipular la URL, y no solamente el usuario, 
    es decir que la aplicación también puede cambiar de componentes y funcionalidades con ayuda del Router.
    4. Se debe tener en cuenta una de las principales características del navegador 
    que es la navegación a través de la URL, es decir acceder a recursos o cambiar el estado de la aplicación a 
    través de interacciones con la URL, ya sea ingresando o modificando la URL del sitio o componente web.
    5.  Para esto,parte de la idea básica de asociar una URL a un Componente de Vue, es decir, cada una de las 
    funcionalidades implementadas en un componente tendrá una URL asociada. Esto genera la interacción 
    deseada, ya que, al cambiar de URL la aplicación cambiará de componente y por consiguiente se accederá 
    a otra funcionalidad. 
    6. La implementación de un Router es bastante sencilla ya que únicamente se deben asociar los componentes 
    con sus respectivas URLs y agregar un nombre clave que pueda ser usado dentro de la aplicación

V. COMPONENTE APP
    1. Por ahora, el único componente que se utilizará en la página web, es el componente principal App.vue. En este 
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
    2. El componente principal de cualquier aplicación de Vue es el componente APP, ya que a partir de este se 
    construye toda la aplicación, agregando de manera directa o indirecta los demás componentes

    3. Router-View: a través del elemento Router, Vue ofrece algunas herramientas que facilitan el 
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

        INTERACCION ENTRE PADRE E HIJOS
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

    4. El componente APP es el encargado de gestionar el flujo de la aplicación y sus componentes, por ello su 
    desarrollo se realizará por partes
    5. El componente APP servirá de base de la aplicación y sobre este se cargarán todos los demás 
    componentes dependiendo de la URL.
    6. Por ello se hará uso de un router view para cargar los componentes hijos. Además, en el componente APP se definen algunas etiquetas que estarán en todo 
    momento durante la ejecución de la aplicación: El header y el footer.
    7. Los botones Iniciar Sesión y Registrarse tienen asociada una función al evento click, esta función 
    deberá modificar la ruta para cargar el componente correspondiente en el router view
    8. El componente APP delegará a componentes hijos la implementación de las funcionalidades LogIn y 
    SignUp, pero este quiere controlar el resultado de estas operaciones, para ello definirá dos métodos 
    completedLogIn y completedSignUp, los cuales sus hijos podrán emitir para informar que se ha 
    finalizado el proceso.

V. COMPONENTE LOGIN 
    1. La capa de presentación es la encargada de interactuar directamente con el 
    usuario final, para hacer esto posible debe comunicarse con la capa de lógica y consumir los servicios 
    que esta ofrece. Para implementar la funcionalidad de LogIn la capa de lógica ofrece un endpoint que 
    el componente bank_fe deberá utilizar a través de una petición HTTP, es decir, el componente de 
    front-end deberá asumir el rol de cliente y realizar una petición al componente de backend que asumirá 
    el rol de servidor.
    2. Para consumir los servicios del componente de back-end en Vue se hace uso de la herramienta Axios, 
    esta permite realizar y manejar peticiones HTTP de una manera rápida y sencilla. Para hacer uso de 
    esta herramienta en el proyecto, simplemente se debe instalar, lo cual se logra ejecutando el siguiente 
    comando en una consola ubicada en la raíz del proyecto:
    3. npm install axios && npm audit fix
    4. ra hacer esto posible debe comunicarse con la capa de lógica y consumir los servicios 
    que esta ofrece. Para implementar la funcionalidad de LogIn la capa de lógica ofrece un endpoint que 
    el componente bank_fe deberá utilizar a través de una petición HTTP, es decir, el componente de 
    front-end deberá asumir el rol de cliente y realizar una petición al componente de backend que asumirá 
    el rol de servidor.
    5. npm install axios. 

    FORMULARIOS
    i.  Formularios: el principal objetivo de la capa de presentación es recolectar información del usuario de 
    una manera rápida y sencilla para ser procesada por las demás capas.
        ii. v-model: Vue permite asociar las entradas de un formulario ubicado en el template de un 
        componente, con un objeto ubicado en el script. Para hacer esto posible simplemente se debe 
        definir el objeto en la data del script y con ayuda del atributo v-model asociarlo con la entrada 
        correspondiente, Vue se encarga de mantener actualizado los valores en ambos lugares.
        iii. Submit: los formularios suelen tener asociado un botón que permite enviar el formulario para 
        ser procesado, Vue ofrece un atributo que permite asociar una función a dicho evento, con 
        ayuda del atributo v-on:submit.prevent=”functionName” en el formulario, se le indica a Vue que 
        se ejecute una determinada función cuando el usuario realice el envío del formulario.
    iv. El template es relativamente simple, es un formulario asociado a una función llamada processLogInUser que 
detectará cuando el usuario lo envíe. Dicho formulario tiene dos entradas que son username y password,estas 
están asociadas al objeto user.


VI. LOCALSTORAGE 

    1. El localStorage se utilizará en el desarrollo del componente de presentación para almacenar algunos datos
    importantes, como los access y refresh tokens, el nombre del usuario y una variable que le permitirá saber a 
    la aplicación en todo momento si el usuario se encuentra o no autenticado. 
    2. En la guía anterior se desarrollaron los componentes de inicio de sesión y de registro del usuario, y se crearon 
    en el componente App.vue las funciones completedLogin y completedSignUp, cuyo propósito es procesar las 
    respuestas obtenidas del componente lógico, al realizar la autenticación o el registro correctamente. La idea
    de dicho procesamiento es almacenar en el localStorage del navegador web la información importante, de 
    forma que esta pueda ser accedida desde cualquier otro componente Vue. Por esta razón, el código de estas 
    dos funciones se debe reemplazar por lo siguiente.
    ● Para crear o modificar un item se utiliza localStorage.setItem(key, value), en caso de que la llave no 
    exista se crea el item, si existe se actualiza su valor.
    ● Para consultar el valor de un item se utiliza localStorage.getItem(key)
    ● Para borrar un item se utiliza localStorage.removeItem(key)
    ● Para borrar todos los items localStorage.clear()

VII. COMPONENTE HOME

    1. Se diseña el home con el template, script y style. 
    2. Se registra el componente de Home en el Router 
        i. De la misma forma que se explicó en la guía anterior, es necesario registrar los componentes en el router para 
        poder acceder a ellos desde otros componentes. Para registrar al componente Home, se debe dirigir al archivo 
        src/router.js, importar allí el componente Home, y registrarlo en la lista de la variable router.
    3. Método verifyAuth -> La idea es que esta función 
    redireccione al usuario al componente Home si se encuentra autenticado, o al componente LogIn si no lo está.
    4. Añadir funcionalidad a los botones Inicio y Cerrar sesión -> 

VIII. OTROS COMPONENTES 

    1. r la dependencia jwt-decode, la cual servirá para desencriptar el access token -> npm install jwt-decode