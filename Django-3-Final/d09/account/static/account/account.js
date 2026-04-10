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

async function handleAccount(formElement) {
    
    const csrftoken = getCookie('csrftoken') || "";

    const formData = new FormData(formElement);
    const response = await fetch("/account/", {
        method: "POST",
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": csrftoken
        },
        body: formData
    });

    const contentType = response.headers.get("content-type") || "";
    
    if (!contentType.includes("application/json")) {
        const text = await response.text();
        console.error("Réponse non-JSON :", response.status, text);

        if (response.status === 403) {
            await refreshCsrfToken();
            showError("Session expirée, réessaie.");
        }
        else {
            showError(`Erreur serveur (${response.status})`);
        }
        return;
    }

    const data = await response.json();

    if (data.success) {
        await updatePage();
    }
    else {
        const errorDiv = document.getElementById("form-errors");
        errorDiv.innerHTML = "";

        for (let field in data.errors) {
            data.errors[field].forEach(err => {
                const p = document.createElement("p");
                p.textContent = err.message;
                p.style.color = "red";
                errorDiv.appendChild(p);
            });
        }
    }
}

function showError(message) {
    const errorDiv = document.getElementById("form-errors");
    if (!errorDiv) return;
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

async function updatePage() {

    const response = await fetch("/account/user-status/");
    const data = await response.json();
    const loginContainer = document.getElementById("login-container");
    const userInfo = document.getElementById("user-info");

    console.log(data.logged_in)
    if (data.logged_in) {
        loginContainer.style.display = "block";
        
        const p = document.createElement("p");
        p.textContent = `Logged as ${data.username}`;
    
        const btn = document.createElement("button");
        btn.textContent = "Logout";
        btn.addEventListener("click", logoutUser);
    
        loginContainer.appendChild(p);
        loginContainer.appendChild(btn);

    }
    else {
        loginContainer.style.display = "block";

    }
}

async function refreshCsrfToken() {
    try {
        const response = await fetch("/account/", {
            method: "GET",
            credentials: "same-origin",
        });

    } catch (e) {
        console.error("Cannot refresh CSRF token", e);
    }
}

async function logoutUser() {
    const csrftoken = getCookie('csrftoken');

    const response = await fetch("/account/logout/", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken
        }
    });
    const data = await response.json();

    if (data.success) {
        await fetch("/account/", {
            method: "GET",
            credentials: "same-origin",
        });
    }
    else {
        alert("Logout Failed");
    }
    await updatePage();
    await refreshCsrfToken();
}

updatePage();