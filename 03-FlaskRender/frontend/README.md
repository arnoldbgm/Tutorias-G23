¡Perfecto! Aquí tienes la guía para crear un **formulario en React** que envía un solo campo por **POST** a un endpoint, siguiendo el estilo de documentación que me compartiste:

---

# 📌 **Guía: Formulario simple en React con POST a una API REST**

En esta guía, crearemos un formulario en **React** que contiene un solo campo (`nombre`) y realiza una solicitud **POST** a un endpoint de una API REST.

---

## **📂 Estructura del componente**

```bash
/src
├── components/
│   └── Header.jsx           # Componente de encabezado reutilizable
├── pages/
│   └── Form.jsx             # Página del formulario
```

---

## **1️⃣ Crear el formulario (`Form.jsx`)**

📌 **Código completo del formulario:**

```jsx
import { useState } from "react";
import Header from "../../components/Header";
import axios from "axios"; // Asegúrate de instalar axios con: npm install axios

const Form = () => {
  const [nombre, setNombre] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault(); // Evita que se recargue la página
    try {
      const response = await axios.post("http://localhost:5000/api/crear", {
        nombre: nombre,
      });
      alert("Formulario enviado correctamente ✅");
      console.log(response.data);
      setNombre(""); // Limpiar campo
    } catch (error) {
      console.error("Error al enviar el formulario ❌", error);
    }
  };

  return (
    <div className="p-4">
      <Header />
      <h2 className="text-xl font-semibold mb-2">Crear Formulario</h2>
      <form onSubmit={handleSubmit} className="space-y-2">
        <label htmlFor="nombre">Nombre:</label>
        <input
          type="text"
          id="nombre"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
          className="border rounded px-2 py-1"
          required
        />
        <br />
        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-1 rounded hover:bg-blue-600"
        >
          Enviar
        </button>
      </form>
    </div>
  );
};

export default Form;
```

---

## **2️⃣ Instalar dependencias necesarias**

📌 **Instalar `axios` para realizar peticiones HTTP:**

```bash
npm install axios
```

---

## **3️⃣ Ejemplo de lo que se enviará al backend**

Al enviar el formulario, se enviará este JSON:

```json
{
  "categoria": "Rock"
}
```