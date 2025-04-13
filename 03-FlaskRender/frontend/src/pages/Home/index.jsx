import { useEffect, useState } from "react"
import Header from "../../components/Header"
import axios from "axios"

const Home = () => {
  // Paso 01: Crear un useState
  const [categorias, setCategorias] = useState([])

  // Paso 02: Crearemos la funcion para obtener las categorias
  const getCategorias = async () => {
    try {
      const response = await axios.get("https://tutorias-g23.onrender.com/categorias")
      setCategorias(response.data)
    } catch (error) {
      console.log(error)
    }
  }

  // Paso 03: Consumir una API de tipo GET => useEffect 

  useEffect(() => {
    getCategorias()
  }, [])


  return (
    <div>
      <Header />
      Home bienvenido
      <h1 className="text-xl">Categorias</h1>
      <ul>
        {
          categorias.map((categoria) =>
          (
            <li key={categoria.id}>{categoria.nombre}</li>
          ))
        }
      </ul>
    </div>
  )
}

export default Home