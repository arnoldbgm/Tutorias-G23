import { useState } from "react"
import Header from "../../components/Header"
import axios from "axios";

const Form = () => {
  // Paso 02: Creamos la variable nombre
  const [nombre, setNombre] = useState("")
  // Paso 03: Debemos captuar los valores del input onChange => input

  // Paso 04: Crear el evento onSubmit para el formulario
  const handleSubmit = async (e) => {
    e.preventDefault() // Evita que se recargue la pagina
    // Paso 05: Enviar el formulario al backend
    try {
      const response = await axios.post("https://tutorias-g23.onrender.com/categorias", {
        nombre: nombre
      })
      alert("Categoria creada")
      console.log(response.data)
      setNombre("")
    } catch (error) {
      console.log(error)
    }
  }

  // Paso 06: Asociar el evento onSubmit al formulario

  return (
    <div>
      <Header />
      <h1 className="text-xl">Formulario de Categorias</h1>
      {/* Paso 01: Crear el Formulario */}
      <form onSubmit={handleSubmit} className="max-w-sm mx-auto">
        <label htmlFor="nombre" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >Nombre:</label>
        <input
          type="text"
          id="nombre"
          className="shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-xs-light"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
        />
        <button className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Enviar</button>
      </form>
    </div>
  )
}

export default Form