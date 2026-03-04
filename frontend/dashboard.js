const API = "http://127.0.0.1:8000";

// Leer usuario guardado al hacer login
const username = sessionStorage.getItem("username");
if (!username) {
    window.location.href = "index.html";
}
document.getElementById("avatar").textContent = username[0].toUpperCase();
document.getElementById("username-display").textContent = username;

function toast(msg, type = "success") {
    const t = document.getElementById("toast");
    t.textContent = msg;
    t.className = `show ${type}`;
    setTimeout(() => t.className = "", 3000);
}

async function getCSRF() {
    const res = await fetch(`${API}/api/auth/csrf/`, { credentials: "include" });
    const data = await res.json();
    return data.csrfToken;
}

async function loadSlots() {
    try {
        const res = await fetch(`${API}/api/parking/slots/`, { credentials: "include" });
        if (!res.ok) {
            // Sesión expirada
            sessionStorage.removeItem("username");
            window.location.href = "index.html";
            return;
        }
        const data = await res.json();
        const free = data.filter(s => s.status === "FREE").length;
        document.getElementById("pills").innerHTML = `
            <span class="pill free">🟢 ${free} libres</span>
            <span class="pill occ">🔴 ${data.length - free} ocupados</span>
        `;
        const grid = document.getElementById("slots-grid");
        grid.innerHTML = "";
        data.forEach(slot => {
            const f = slot.status === "FREE";
            const card = document.createElement("div");
            card.className = `slot-card ${f ? "free" : "occ"}`;
            card.innerHTML = `
                <div class="slot-label">Espacio</div>
                <div class="slot-num">#${slot.id}</div>
                <div class="slot-badge ${f ? "free" : "occ"}">
                    <span class="dot"></span>${f ? "Disponible" : "Ocupado"}
                </div>
                <div class="slot-actions">
                    <button type="button" class="slot-btn occupy" onclick="occupy(${slot.id})">Ocupar</button>
                    <button type="button" class="slot-btn release" onclick="release(${slot.id})">Liberar</button>
                </div>
            `;
            grid.appendChild(card);
        });
    } catch (e) {
        toast("Error de conexión", "error");
    }
}

async function occupy(id) {
    try {
        const csrf = await getCSRF();
        const res = await fetch(`${API}/api/parking/slots/${id}/occupy/`, {
            method: "POST", credentials: "include",
            headers: { "Content-Type": "application/json", "X-CSRFToken": csrf },
            body: JSON.stringify({ vehicle_model: "Auto desde frontend" })
        });
        res.ok ? toast(`Espacio #${id} ocupado`) : toast("Error al ocupar", "error");
        loadSlots();
    } catch (e) { toast("Error de conexión", "error"); }
}

async function release(id) {
    try {
        const csrf = await getCSRF();
        const res = await fetch(`${API}/api/parking/slots/${id}/free/`, {
            method: "POST", credentials: "include",
            headers: { "X-CSRFToken": csrf }
        });
        res.ok ? toast(`Espacio #${id} liberado`) : toast("Error al liberar", "error");
        loadSlots();
    } catch (e) { toast("Error de conexión", "error"); }
}

async function doLogout() {
    try {
        const csrf = await getCSRF();
        await fetch(`${API}/accounts/logout/`, {
            method: "POST", credentials: "include",
            redirect: "manual",
            headers: { "X-CSRFToken": csrf }
        });
    } catch (e) {}
    sessionStorage.removeItem("username");
    window.location.href = "index.html";
}

document.getElementById("btn-logout").addEventListener("click", doLogout);
document.getElementById("btn-refresh").addEventListener("click", loadSlots);

loadSlots();