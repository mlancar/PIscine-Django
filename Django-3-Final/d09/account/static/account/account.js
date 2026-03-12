document.getElementById("login-form").addEventListener("submit", function(e) {
    e.preventDefault(); //empeche reload

    const formData = new FormData(this);

    fetch("/account/", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.reload();
        }
    })
})