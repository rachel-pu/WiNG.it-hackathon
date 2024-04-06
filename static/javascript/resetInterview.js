 document.addEventListener('DOMContentLoaded', function() {
         const resetButton = document.getElementById('reset-button');
         resetButton.addEventListener('click', function() {
             fetch('/clear_array', {
                 method: 'POST',
             })
             .then(response => response.json())
             .then(data => alert(data.message))
             .catch(error => console.error('Error:', error));
         });
     });

//document.addEventListener('DOMContentLoaded', function() {
//    const resetButton = document.getElementById('reset-button');
//    resetButton.addEventListener('click', function() {
//        fetch('/clear_array', {
//            method: 'POST',
//        })
//        .then(response => response.json())
//        .then(data => alert("Array cleared")) // Alert a message indicating array cleared
//        .catch(error => console.error('Error:', error));
//    });
//});
