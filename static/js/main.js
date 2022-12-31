$(document).ready(function() {
  // Add an item to the registry
  $("#add-item-form").submit(function(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Get the form data
    var name = $("#name").val();
    var price = $("#price").val();
    console.log(name);
    console.log(price);

    // Send a POST request to the server
    $.post("/registry", { name: name, price: price }, function(data) {
      // Log the response and reload the page
      console.log(data);
      location.reload();
    });
  });

  // Mark an item as purchased
  $(".mark-purchased-btn").click(function() {
    // Get the item ID from the button's data attribute
    var itemId = $(this).data("item-id");

    // Send a PUT request to the server
    $.ajax({
      url: "/update-registry/" + itemId,
      type: "PUT",
      success: function(data) {
        // Log the response and reload the page
        console.log(data);
        location.reload();
      }
    });
  });

  // Delete an item from the registry
  $(".delete-item-btn").click(function() {
    // Get the item ID from the button's data attribute
    var itemId = $(this).data("item-id");

    // Send a DELETE request to the server
    $.ajax({
      url: "/update-registry/" + itemId,
      type: "DELETE",
      success: function(data) {
        // Log the response and reload the page
        console.log(data);
        location.reload();
      }
    });
  });
});
