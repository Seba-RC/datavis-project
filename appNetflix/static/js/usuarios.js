
let chartCity;

function fetchDataAndRenderCharts() {
    fetch('/dataUsuario')  
        .then(response => response.json())
        .then(data => {
            displayUserInfo(data.usuarioJoven, data.usuarioViejo);
            const cityData = generateCityData(data.usuarios);
            renderPieChart(cityData);
        });
}

function displayUserInfo(youngest, oldest) {
    document.getElementById('masJoven').innerHTML = `
        <p><strong>Nombre:</strong> ${youngest.nombre}</p>
        <p><strong>Fecha de Nacimiento:</strong> ${youngest.fechanacimiento}</p>
        <p><strong>Ciudad:</strong> ${youngest.ciudad}</p>
    `;
    
    document.getElementById('masViejo').innerHTML = `
        <p><strong>Nombre:</strong> ${oldest.nombre}</p>
        <p><strong>Fecha de Nacimiento:</strong> ${oldest.fechanacimiento}</p>
        <p><strong>Ciudad:</strong> ${oldest.ciudad}</p>
    `;
}

function generateCityData(users) {
    const cityCounts = {};
    users.forEach(user => {
        cityCounts[user.ciudad] = (cityCounts[user.ciudad] || 0) + 1;
    });

    return Object.keys(cityCounts).map(city => ({
        label: city,
        value: cityCounts[city]
    }));
}


function renderPieChart(cityData) {
    const ctx = document.getElementById('cityChart').getContext('2d');
    chartCity = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: cityData.map(item => item.label),
            datasets: [{
                label: 'Usuarios por ciudad',
                data: cityData.map(item => item.value),
                backgroundColor: ['rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)', 'rgba(255, 159, 64, 0.6)', 'rgba(54, 162, 235, 0.6)'],
                borderColor: ['rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)', 'rgba(255, 159, 64, 1)', 'rgba(54, 162, 235, 1)'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true
        }
    });
}


document.addEventListener("DOMContentLoaded", function () {
    fetchDataAndRenderCharts();
});
