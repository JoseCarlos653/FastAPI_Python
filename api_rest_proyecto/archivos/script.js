document.addEventListener('DOMContentLoaded', () => {
    const peliculasSection = document.getElementById('peliculas-list');
    const form = document.getElementById('pelicula-form');

    // Función para cargar todas las películas
    const cargarPeliculas = async () => {
        const response = await fetch('/peliculas');
        const peliculas = await response.json();
        peliculasSection.innerHTML = '';

        peliculas.forEach(pelicula => {
            const peliculaDiv = document.createElement('div');
            peliculaDiv.classList.add('pelicula');
            peliculaDiv.innerHTML = `
                <h3>${pelicula.titulo}</h3>
                <p>${pelicula.descripcion}</p>
                <p>Año: ${pelicula.año}</p>
                <p>Calificación: ${pelicula.calificacion}</p>
                <p>Categoría: ${pelicula.categoria}</p>
                <button onclick="editarPelicula(${pelicula.id})">Editar</button>
                <button onclick="eliminarPelicula(${pelicula.id})">Eliminar</button>
            `;
            peliculasSection.appendChild(peliculaDiv);
        });
    };

    // Función para manejar el envío del formulario
    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const id = form.id.value;
        const titulo = form.titulo.value;
        const descripcion = form.descripcion.value;
        const año = form.año.value;
        const calificacion = form.calificacion.value;
        const categoria = form.categoria.value;

        const payload = {
            id: parseInt(id) || undefined,
            titulo,
            descripcion,
            año: parseInt(año),
            calificacion: parseFloat(calificacion),
            categoria
        };

        if (id) {
            // Actualizar película
            await fetch(`/peliculas/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });
        } else {
            // Crear nueva película
            await fetch('/peliculas', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });
        }

        form.reset();
        cargarPeliculas();
    });

    // Función para editar una película
    window.editarPelicula = async (id) => {
        const response = await fetch(`/peliculas/${id}`);
        const pelicula = await response.json();

        form.id.value = pelicula.id;
        form.titulo.value = pelicula.titulo;
        form.descripcion.value = pelicula.descripcion;
        form.año.value = pelicula.año;
        form.calificacion.value = pelicula.calificacion;
        form.categoria.value = pelicula.categoria;
    };

    // Función para eliminar una película
    window.eliminarPelicula = async (id) => {
        await fetch(`/peliculas/${id}`, {
            method: 'DELETE'
        });
        cargarPeliculas();
    };

    // Cargar películas al iniciar
    cargarPeliculas();
});
