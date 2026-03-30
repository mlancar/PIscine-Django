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

async function handleAccount() {
    
    const csrftoken = getCookie('csrftoken');

    const response = await fetch("/account/", {
        method: "POST",
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": csrftoken
        },
        body: new FormData(document.getElementById("login-form"))
    });

    const data = await response.json();

    if (data.success) {
        await updatePage();
    }
    else {
        const errorDiv = document.getElementById("form-errors");
        errorDiv.innerHTML = "";

        // afficher toutes les erreurs
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

async function updatePage() {

    const response = await fetch("/account/user-status/");

    const data = await response.json();

    const container = document.getElementById("form-container");
    container.innerHTML = "";

    if (data.logged_in) {
        const p = document.createElement("p");
        p.textContent = `Logged as ${data.username}`;

        const btn = document.createElement("button");
        btn.textContent = "Logout";
        btn.addEventListener("click", logoutUser);

        container.appendChild(p);
        container.appendChild(btn);
    }
    else {
        container.innerHTML = `
            <form id="login-form" method="post" class="div-overlay btn-no-hover d-flex flex-column">
                <input type="text" name="username" id="id_username" placeholder="Username">
                <input type="password" name="password" id="id_password" placeholder="Password">
                <div id="form-errors"></div>
                <button type="submit">Login</button>
            </form>
        `;
        attachLoginHandler();
    }

}

function attachLoginHandler() {
    const loginForm = document.getElementById("login-form");
    if (loginForm) {
        loginForm.addEventListener("submit", async function(e) {
            e.preventDefault();
            await handleAccount();
        });
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
        await updatePage();
    }
    else {
        alert("Logout Failed");
    }
}

updatePage();