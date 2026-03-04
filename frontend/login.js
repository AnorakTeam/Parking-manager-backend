const API = "http://127.0.0.1:8000";
let mode = "login";

function switchTab(tab) {
    mode = tab;
    document.getElementById("tab-login").classList.toggle("active", tab === "login");
    document.getElementById("tab-register").classList.toggle("active", tab === "register");
    document.getElementById("auth-btn").textContent = tab === "login" ? "Iniciar sesión" : "Crear cuenta";
    setMsg("");
}

function setMsg(text, type = "") {
    const el = document.getElementById("msg");
    el.textContent = text;
    el.className = type;
}

async function getCSRF() {
    const res = await fetch(`${API}/api/auth/csrf/`, { credentials: "include" });
    const data = await res.json();
    return data.csrfToken;
}

async function handleAuth() {
    const username = document.getElementById("input-username").value.trim();
    const password = document.getElementById("input-password").value.trim();

    if (!username || !password) { setMsg("Completa todos los campos", "error"); return; }

    if (mode === "register") {
        await doRegister(username, password);
    } else {
        await doLogin(username, password);
    }
}

async function doRegister(username, password) {
    try {
        const csrf = await getCSRF();
        const res = await fetch(`${API}/api/auth/register/`, {
            method: "POST", credentials: "include",
            headers: { "Content-Type": "application/json", "X-CSRFToken": csrf },
            body: JSON.stringify({ username, password })
        });
        const data = await res.json();
        if (res.ok) {
            sessionStorage.setItem("username", username);
            window.location.href = "dashboard.html";
        } else {
            setMsg(data.username?.[0] || "Error al registrar", "error");
        }
    } catch (e) {
        setMsg("Error de conexión", "error");
    }
}

async function doLogin(username, password) {
    try {
        const csrf = await getCSRF();
        const body = new URLSearchParams({ username, password });

        const res = await fetch(`${API}/accounts/login/`, {
            method: "POST", credentials: "include",
            redirect: "manual",
            headers: { "Content-Type": "application/x-www-form-urlencoded", "X-CSRFToken": csrf },
            body
        });

        if (res.status === 200) {
            setMsg("Usuario o contraseña incorrectos", "error");
        } else {
            sessionStorage.setItem("username", username);
            window.location.href = "dashboard.html";
        }
    } catch (e) {
        setMsg("Error de conexión", "error");
    }
}

document.getElementById("auth-btn").addEventListener("click", handleAuth);
document.getElementById("input-username").addEventListener("keydown", e => { if (e.key === "Enter") handleAuth(); });
document.getElementById("input-password").addEventListener("keydown", e => { if (e.key === "Enter") handleAuth(); });