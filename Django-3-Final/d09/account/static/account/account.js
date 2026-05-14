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
                updatePage();
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
                // else {
                //     errorDiv.append(`<p style="color:red">Login failed</p>`);
                // }
            }
        },

        error: function(xhr) {
            console.error("Error:", xhr.responseText);
            alert("Error 403 : Bad CSRF Token");
        }
    });
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

        const loginForm = $("#login-form");
        const loginTitle = $(".login-title")
        const logoutContainer = $("#logout-container");
        const registerContainer = $(".register-container")

        logoutContainer.empty();

        if (data.logged_in || data.is_authenticated) {
            loginForm.hide();
            loginTitle.hide();
            registerContainer.hide();

            logoutContainer.html(`
                <p>Logged as ${data.username}</p>
                <button id="logout-btn" class="btn" >Logout</button>
            `);

            $("#logout-btn").on("click", logoutUser);
            logoutContainer.show();
        }
        else {
            loginForm.show();
            loginTitle.show();
            registerContainer.show();
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
        const errorDiv = $("#form-errors");
        errorDiv.html("");
        handleAccount(this);
    });
}

$(document).ready(function() {
    attachLoginHandler();
    updatePage();
});