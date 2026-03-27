
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
