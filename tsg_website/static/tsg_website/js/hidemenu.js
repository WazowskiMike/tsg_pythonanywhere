document.addEventListener('DOMContentLoaded', function () {
    // Select all navigation links within the navbar
    var navbarLinks = document.querySelectorAll('#navbar .nav-link');

    // Loop through each link and add an event listener
    navbarLinks.forEach(function (link) {
      link.addEventListener('click', function () {
        // Find the button with the ID 'close'
        var closeButton = document.getElementById('close');

        // If the button exists, simulate a click on it
        if (closeButton) {
          closeButton.click();
        }
      });
    });
  });