
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(function(alert) {
        // Wait 1000ms (1 second) before starting the fade
        setTimeout(function() {
            // Apply a smooth fade-out effect
            alert.style.transition = "opacity 0.5s ease";
            alert.style.opacity = "0";
            
            // Physically remove the element from the page after it fades out
            setTimeout(() => {
                alert.remove();
            }, 500);
            
        }, 1000); 
    });

    var toastElList = [].slice.call(document.querySelectorAll('.toast'))
    
    // Initialize Bootstrap Toast for each element with auto-hide enabled
    toastElList.forEach(function(toastEl) {
      var toast = new bootstrap.Toast(toastEl, {
        delay: 3000, // time in milliseconds before auto-hide (3s)
        autohide: true
      });
      toast.show(); // show the toast
    });