function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    xhrFields: {
        withCredentials: true
    },
    beforeSend: function(xhr, settings) {
        if (!(/^GET|HEAD|OPTIONS|TRACE$/.test(settings.type))) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

function handleAccount(formElement) {
    
    const freshToken = getCookie('csrftoken');
    const formData = new FormData(formElement);
    formData.set('csrfmiddlewaretoken', freshToken);

    $.ajax({
        url: "/account/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,

        headers: {
            "X-CSRFToken": freshToken
        },

        success: function(data) {
            if (data.success) {
                console.log("ICI")
                updatePage();
                // location.reload();
            }
            else {
                const errorDiv = $("#form-errors");
                errorDiv.html("");

                if (data.errors) {
                    for (let field in data.errors) {
                        data.errors[field].forEach(err => {
                            const message = err.message || err;
                            errorDiv.append(`<p style="color:red">${message}</p>`);
                        });
                    }
                } 
                else {
                    errorDiv.append(`<p style="color:red">Login failed</p>`);
                }
            }
        },

        error: function(xhr) {
            console.error("Détails erreur:", xhr.responseText);
            alert("Erreur 403 : Problème de jeton CSRF.");
        //     if (xhr.status === 403) {
        //         refreshCsrfToken();
        //         showError("Session expirée, réessaie.");
        //     }
        //     else {
        //         showError(`Erreur serveur (${xhr.status})`);
        //     }
        }
    });
}

function showError(message) {
    const errorDiv = document.getElementById("form-errors");
    if (!errorDiv)
        return;
    errorDiv.innerHTML = `<p style="color:red">${message}</p>`;
}

function attachLoginHandler() {
    const loginForm = document.getElementById("login-form");
    if (loginForm) {
        loginForm.addEventListener("submit", async function(e) {
            e.preventDefault();
            await handleAccount(e.target);
        });
    }
}

function updatePage() {
    $.get("/account/user-status/", function(data) {
        console.log("LOGOUT RESPONSE:", data);

        const loginForm = $("#login-form");
        const logoutContainer = $("#logout-container");
        logoutContainer.empty();

        if (data.logged_in || data.is_authenticated) {
            console.log("PAR ICI")

            loginForm.hide();
            

            logoutContainer.html(`
                <p>Logged as ${data.username}</p>
                <button id="logout-btn">Logout</button>
            `);

            $("#logout-btn").on("click", logoutUser);
            logoutContainer.show();

        }
        else {
            loginForm.show();
            logoutContainer.hide();
        }
    });
}

function logoutUser() {
    $.ajax({
        url: "/account/logout/",
        type: "POST",
        headers: { "X-CSRFToken": getCookie('csrftoken') },
        success: function(data) {
            if (data.success) {
                updatePage();
            }
        }
    });
}

function refreshCsrfToken() {
    $.get("/account/");
}

function attachLoginHandler() {
    $("#login-form").on("submit", function(e) {
        e.preventDefault();
        handleAccount(this);
    });
}

$(document).ready(function() {
    attachLoginHandler();
    updatePage();
});