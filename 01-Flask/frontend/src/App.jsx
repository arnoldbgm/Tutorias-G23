import { useEffect, useState } from 'react'
import './App.css'

function App() {

  // 1. Consumir una API (Backend) => useState
  const [usuarios, setUsuarios] = useState([])

  // 2. Debemos usar el useEffect
  useEffect(() => {
    // 3. Crear nuestra funcion para consumir nuestra API
    const fetchUsuarios = async () => {
      const res = await fetch("http://127.0.0.1:5000/api/usuarios")
      const data = await res.json()
      setUsuarios(data)
    }

    // 4. Ejecutar nuestra funcion
    fetchUsuarios()

  }, []);

  return (
    <>
      {/* 5. Renderizado del Backend */}
      {
        usuarios.map((user) => (
          <>
            <h1>Nombre: {user.nombre}</h1>
            <h2>Ciudad: {user.ciudad}</h2>
          </>
        ))
      }
    </>
  )
}

export default App
