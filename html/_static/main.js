/* Adds custom search builder, positions elements */

$(document).ready( function () {
    $('table.datatable').DataTable({
      searchBuilder: {
        columns: [0,1,2,]
      },
      columnDefs: [{
        targets: [0, 1, 2,],
        searchBuilder: {
            defaultCondition: '='
        }
    }],
      dom: '<"top"Qrt><"bottom"flip><"clear">',
    });
} );
