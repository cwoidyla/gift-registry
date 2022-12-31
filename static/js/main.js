function updateRegistry() {
    var items = [];
    $('input[name=purchased]').each(function() {
      if ($(this).is(':checked')) {
        items.push($(this).val());
      }
    });
  
    $.ajax({
      type: 'POST',
      url: '/update-registry',
      data: {
        items: items
      },
      success: function(response) {
        alert(response);
      }
    });
  }
  
  $(document).ready(function() {
    $('input[name=purchased]').change(updateRegistry);
  });
  