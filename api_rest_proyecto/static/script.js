document.addEventListener('DOMContentLoaded', () => {
    const peliculasSection = document.getElementById('peliculas-list');

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
            `;
            peliculasSection.appendChild(peliculaDiv);
        });
    };

    // Cargar películas al iniciar
    cargarPeliculas();
});
