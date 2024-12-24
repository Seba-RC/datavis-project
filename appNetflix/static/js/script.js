let chart; 
    

function fetchDataAndRenderChart(option, chartType, year) {
  let url;


  switch(option) {
    case 'dataSerie':
      url = `/datatipoSerie/${year}`; 
      labelKey = `tiposerie`;
      break;
    case 'dataPelicula':
      url = `/datatipoPelicula/${year}`;  
      labelKey = `tipopelicula`;
      break;
    default:
      return;
  }

  fetch(url)
    .then(response => response.json())
    .then(data => {

      const labels = data.map(item => item[labelKey]);

      const chartData = {
        labels: labels,
        datasets: [{
          label: 'Vistas',
          data: data.map(item => item.count),
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        }]
      };
      if (chart) {
        chart.destroy();  
      }


      chart = new Chart(document.getElementById('mainChart'), {
        type: chartType,
        data: chartData,
        options: {
          responsive: true,
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    })
}

document.getElementById('dataSelector').addEventListener('change', function() {
    const selectedOption = this.value;
    const selectedYear = document.getElementById('fechaSelector').value;
    fetchDataAndRenderChart(selectedOption, 'bar', selectedYear);
  });

document.getElementById('fechaSelector').addEventListener('change', function() {
    const selectedOption = document.getElementById('dataSelector').value;
    const selectedYear = this.value;
    fetchDataAndRenderChart(selectedOption, 'bar', selectedYear);
});