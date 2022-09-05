$(function () {

    var $operationChart = $("#operation-chart");
    $.ajax({
      url: $operationChart.data("url"),
      success: function (data) {

        var ctx = $operationChart[0].getContext("2d");

        new Chart(ctx, {
          type: 'pie',
          data: {
            datasets: [{
              data: data.data,
              backgroundColor: [
                'bleu', 'red'
              ],
              label: 'Population'
            }],
            labels: data.labels
          },
          options: {
            responsive: true,
            title: {
              display: true,
              text: 'Représentation des opérations'
            }
          }
        });

      }
    });


    var $statutChart = $("#statut-chart");
    $.ajax({
      url: $statutChart.data("url"),
      success: function (data) {

        var ctx = $statutChart[0].getContext("2d");

        new Chart(ctx, {
          type: 'bar',
          data: {
            labels: data.labels,
            datasets: [{
              label: 'Statut',
              backgroundColor:['blue','green','yellow'],
              data: data.data
            }]          
          },
          options: {
            responsive: true,
            title: {
              display: true,
              text: 'Répresentation des statuts'
            }
          }
        });

      }
    });

  });